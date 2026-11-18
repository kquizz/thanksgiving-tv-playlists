#!/usr/bin/env python3
"""Build the static Stremio catalog add-on into docs/ from playlists/*.json."""
import argparse, hashlib, json, re, sys, time, urllib.error, urllib.request
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "scripts" / ".cache"
UA = "thanksgiving-tv-playlists-builder"
API = "https://api.tvmaze.com"
IMG = "https://images.metahub.space"

CATALOGS = [
    ("thanksgiving-comedies", "Thanksgiving Comedies"),
    ("thanksgiving-comedies-classic", "Thanksgiving Comedies: Classic"),
    ("thanksgiving-comedies-modern", "Thanksgiving Comedies: Modern"),
    ("thanksgiving-animation", "Thanksgiving Animation"),
    ("thanksgiving-dramas", "Thanksgiving Dramas"),
    ("thanksgiving-60s-80s", "Thanksgiving: 60s–80s"),
    ("thanksgiving-90s", "Thanksgiving: 90s"),
    ("thanksgiving-2000s", "Thanksgiving: 2000s"),
    ("thanksgiving-2010s-20s", "Thanksgiving: 2010s–20s"),
]


# Playlists use IMDb/Cinemeta numbering, because that is what stream add-ons
# match on. Where TVMaze numbers an episode differently, map it here so the
# metadata lookup still finds the right episode.
TVMAZE_NUMBERING = {
    "tt0101188:4:22": (4, 13),  # Rugrats – The Turkey Who Came to Dinner
    "tt0397306:10:5": (9, 5),   # American Dad! – Kung Pao Turkey
}


def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def fetch(url):
    """GET json with disk cache, rate limiting, one 429 retry. Returns None on 404."""
    CACHE.mkdir(parents=True, exist_ok=True)
    cf = CACHE / (hashlib.sha1(url.encode()).hexdigest() + ".json")
    if cf.exists():
        return json.loads(cf.read_text())
    for attempt in (1, 2):
        time.sleep(0.6)
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=15) as r:
                data = json.loads(r.read().decode("utf-8"))
            cf.write_text(json.dumps(data))
            return data
        except urllib.error.HTTPError as e:
            if e.code == 404:
                cf.write_text("null")
                return None
            if e.code == 429 and attempt == 1:
                print("  429, sleeping 10s", flush=True)
                time.sleep(10)
                continue
            raise
    return None


def strip_html(s):
    if not s:
        return None
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", s))).strip() or None


_shows = {}


def show_for(imdb):
    if imdb not in _shows:
        _shows[imdb] = fetch(f"{API}/lookup/shows?imdb={imdb}")
    return _shows[imdb]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default="1.0.0")
    args = ap.parse_args()

    files = {p.stem: p for p in (ROOT / "playlists").glob("*.json")}
    expected = {s for s, _ in CATALOGS}
    if set(files) != expected:
        sys.exit(f"playlist mismatch: missing={sorted(expected - set(files))} extra={sorted(set(files) - expected)}")

    docs = ROOT / "docs"
    docs.mkdir(exist_ok=True)
    (docs / ".nojekyll").write_text("")

    write_json(docs / "manifest.json", {
        "id": "community.thanksgiving-tv-playlists",
        "version": args.version,
        "name": "Thanksgiving TV Playlists",
        "description": "Curated Thanksgiving episodes of TV comedies, cartoons and dramas, by genre and decade. Catalog only — streams come from your other add-ons.",
        "resources": ["catalog", {"name": "meta", "types": ["series"], "idPrefixes": ["tgv_"]}],
        "types": ["series", "movie"],
        "idPrefixes": ["tgv_"],
        "catalogs": [{"type": "series", "id": s, "name": n} for s, n in CATALOGS],
        "behaviorHints": {"configurable": False, "configurationRequired": False},
    })

    failures, warnings, done = [], [], set()
    for slug, _ in CATALOGS:
        pl = json.loads(files[slug].read_text(encoding="utf-8"))
        metas = []
        print(f"== {slug} ({len(pl['items'])})", flush=True)
        for it in pl["items"]:
            imdb = it["imdb_id"]
            if it["type"] == "movie":
                metas.append({"id": imdb, "type": "movie", "name": it["show"],
                              "poster": f"{IMG}/poster/medium/{imdb}/img",
                              "releaseInfo": it["air_date"][:4]})
                continue
            s, e = it["season"], it["episode"]
            tid = f"tgv_{imdb}_{s}_{e}"
            vid = f"{imdb}:{s}:{e}"
            name = f"{it['show']}: {it['episode_title']}"
            year = it["air_date"][:4]
            poster = f"{IMG}/poster/medium/{imdb}/img"
            summary = None
            if tid not in done:
                show = show_for(imdb)
                ts, te = TVMAZE_NUMBERING.get(vid, (s, e))
                ep = fetch(f"{API}/shows/{show['id']}/episodebynumber?season={ts}&number={te}") if show else None
                if not show or not ep:
                    failures.append(vid)
                    print(f"  FAIL {vid} {name}", flush=True)
                    continue
                summary = strip_html(ep.get("summary"))
                eimg = ep.get("image") or {}
                simg = show.get("image") or {}
                background = eimg.get("original") or simg.get("original") or f"{IMG}/background/medium/{imdb}/img"
                thumb = eimg.get("medium")
                if not summary:
                    warnings.append(f"{vid} no summary")
                if not thumb:
                    warnings.append(f"{vid} no episode image")
                released = f"{it['air_date']}T00:00:00.000Z"
                desc = f"{it['show']} · Season {s}, Episode {e} · aired {it['air_date']}"
                if summary:
                    desc += "\n\n" + summary
                write_json(docs / "meta" / "series" / f"{tid}.json", {"meta": {
                    "id": tid, "type": "series", "name": name, "poster": poster,
                    "background": background, "description": desc,
                    "releaseInfo": year, "released": released,
                    "videos": [{"id": vid, "title": it["episode_title"], "season": s, "episode": e,
                                "released": released, "thumbnail": thumb, "overview": summary}],
                    "behaviorHints": {"defaultVideoId": vid},
                }})
                done.add(tid)
                print(f"  ok {vid} {name}", flush=True)
            short = f"{it['show']} · S{s}E{e} · aired {it['air_date']}"
            metas.append({"id": tid, "type": "series", "name": name, "poster": poster,
                          "posterShape": "poster", "description": short, "releaseInfo": year})
        write_json(docs / "catalog" / "series" / f"{slug}.json", {"metas": metas})

    for w in warnings:
        print("WARN", w)
    if failures:
        sys.exit(f"unresolved episodes: {failures}")
    print(f"done: {len(done)} meta files")


if __name__ == "__main__":
    main()
