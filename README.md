# Thanksgiving TV Playlists

Curated Thanksgiving episodes of TV comedies, cartoons and dramas — from *Bewitched* (1967) to *Bob's Burgers* (2022) — grouped by genre and by decade, in original air-date order.

Every episode was matched against [TVMaze](https://www.tvmaze.com/) for correct season/episode numbers and IMDb IDs.

## Download

| File | What it is |
|---|---|
| [`all-episodes.csv`](all-episodes.csv) | Every episode, one row each — opens in Excel / Google Sheets |
| [`all-episodes.json`](all-episodes.json) | Same, as JSON |
| [`playlists/`](playlists/) | One JSON file per playlist, in watch order |

Each entry has the show, season/episode, episode title, original air date, genre and IMDb ID. The `stremio_id` field is the standard Stremio episode id (`{imdbId}:{season}:{episode}`).

## Use it in Stremio

Install the add-on by pasting `https://kquizz.github.io/thanksgiving-tv-playlists/manifest.json` into Stremio's add-on search box. The playlists appear as rows on the Board and under Discover → Series. This add-on only lists episodes — playback comes from whatever stream add-ons you already use.

## Rebuilding the add-on

`python3 scripts/build_addon.py` regenerates `docs/` from `playlists/`.

## Playlists

- [Comedies — all](#thanksgiving-comedies) — 43
- [Comedies — Classic (pre-2000)](#thanksgiving-comedies-classic) — 18
- [Comedies — Modern (2000+)](#thanksgiving-comedies-modern) — 25
- [Animation](#thanksgiving-animation) — 22
- [Dramas](#thanksgiving-dramas) — 17
- [1960s–80s](#thanksgiving-60s-80s) — 6
- [1990s](#thanksgiving-90s) — 22
- [2000s](#thanksgiving-2000s) — 17
- [2010s–20s](#thanksgiving-2010s-20s) — 37

<a id="thanksgiving-comedies"></a>

### Comedies — all (43)

[JSON](playlists/thanksgiving-comedies.json)

| # | Aired | Show | Ep | Title |
|---|---|---|---|---|
| 1 | 1967-11-23 | [Bewitched](https://www.imdb.com/title/tt0057733/) | S4E12 | Samantha's Thanksgiving to Remember |
| 2 | 1975-11-22 | [The Bob Newhart Show](https://www.imdb.com/title/tt0068049/) | S4E11 | Over the River and Through the Woods |
| 3 | 1978-10-30 | [WKRP in Cincinnati](https://www.imdb.com/title/tt0077097/) | S1E7 | Turkeys Away |
| 4 | 1986-11-27 | [Cheers](https://www.imdb.com/title/tt0083399/) | S5E9 | Thanksgiving Orphans |
| 5 | 1991-11-26 | [Roseanne](https://www.imdb.com/title/tt0094540/) | S4E10 | Thanksgiving '91 |
| 6 | 1994-11-17 | [Friends](https://www.imdb.com/title/tt0108778/) | S1E9 | The One Where Underdog Gets Away |
| 7 | 1994-11-17 | [Seinfeld](https://www.imdb.com/title/tt0098904/) | S6E8 | The Mom & Pop Store |
| 8 | 1996-11-21 | [Friends](https://www.imdb.com/title/tt0108778/) | S3E9 | The One With the Football |
| 9 | 1996-11-22 | [Everybody Loves Raymond](https://www.imdb.com/title/tt0115167/) | S1E10 | Turkey or Fish |
| 10 | 1996-11-22 | [Boy Meets World](https://www.imdb.com/title/tt0105958/) | S4E10 | Turkey Day |
| 11 | 1996-11-26 | [Frasier](https://www.imdb.com/title/tt0106004/) | S4E7 | A Lilith Thanksgiving |
| 12 | 1997-11-20 | [Friends](https://www.imdb.com/title/tt0108778/) | S4E8 | The One With Chandler in a Box |
| 13 | 1998-11-19 | [Friends](https://www.imdb.com/title/tt0108778/) | S5E8 | The One With All the Thanksgivings |
| 14 | 1998-11-22 | [That '70s Show](https://www.imdb.com/title/tt0165598/) | S1E9 | Thanksgiving |
| 15 | 1998-11-24 | [Mad About You](https://www.imdb.com/title/tt0103484/) | S7E7 | The Thanksgiving Show |
| 16 | 1999-11-22 | [Everybody Loves Raymond](https://www.imdb.com/title/tt0115167/) | S4E9 | No Thanks |
| 17 | 1999-11-25 | [Friends](https://www.imdb.com/title/tt0108778/) | S6E9 | The One Where Ross Got High |
| 18 | 1999-11-25 | [Will & Grace](https://www.imdb.com/title/tt0157246/) | S2E7 | Homo for the Holidays |
| 19 | 2001-11-22 | [Friends](https://www.imdb.com/title/tt0108778/) | S8E9 | The One With the Rumor |
| 20 | 2001-11-22 | [Will & Grace](https://www.imdb.com/title/tt0157246/) | S4E9 | Moveable Feast (1) |
| 21 | 2001-11-22 | [Will & Grace](https://www.imdb.com/title/tt0157246/) | S4E10 | Moveable Feast (2) |
| 22 | 2002-11-21 | [Friends](https://www.imdb.com/title/tt0108778/) | S9E8 | The One With Rachel's Other Sister |
| 23 | 2002-11-26 | [Gilmore Girls](https://www.imdb.com/title/tt0238784/) | S3E9 | A Deep-Fried Korean Thanksgiving |
| 24 | 2003-11-20 | [Friends](https://www.imdb.com/title/tt0108778/) | S10E8 | The One With the Late Thanksgiving |
| 25 | 2005-11-21 | [How I Met Your Mother](https://www.imdb.com/title/tt0460649/) | S1E9 | Belly Full of Turkey |
| 26 | 2007-11-19 | [How I Met Your Mother](https://www.imdb.com/title/tt0460649/) | S3E9 | Slapsgiving |
| 27 | 2009-11-25 | [The Middle](https://www.imdb.com/title/tt1442464/) | S1E8 | Thanksgiving |
| 28 | 2011-11-15 | [New Girl](https://www.imdb.com/title/tt1826940/) | S1E6 | Thanksgiving |
| 29 | 2012-11-20 | [Happy Endings](https://www.imdb.com/title/tt1587678/) | S3E4 | More Like Stanksgiving |
| 30 | 2012-11-20 | [The Mindy Project](https://www.imdb.com/title/tt2211129/) | S1E6 | Thanksgiving |
| 31 | 2013-03-07 | [Community](https://www.imdb.com/title/tt1439629/) | S4E5 | Cooperative Escapism in Familial Relations |
| 32 | 2013-11-26 | [Brooklyn Nine-Nine](https://www.imdb.com/title/tt2467372/) | S1E10 | Thanksgiving |
| 33 | 2014-11-19 | [Modern Family](https://www.imdb.com/title/tt1442437/) | S6E8 | Three Turkeys |
| 34 | 2014-11-19 | [The Goldbergs](https://www.imdb.com/title/tt2712740/) | S2E7 | A Goldberg Thanksgiving |
| 35 | 2015-11-17 | [Fresh Off the Boat](https://www.imdb.com/title/tt3551096/) | S2E8 | Huangsgiving |
| 36 | 2016-11-10 | [Superstore](https://www.imdb.com/title/tt4477976/) | S2E9 | Black Friday |
| 37 | 2016-11-15 | [Fresh Off the Boat](https://www.imdb.com/title/tt3551096/) | S3E5 | No Thanks-giving |
| 38 | 2016-11-16 | [black-ish](https://www.imdb.com/title/tt3487356/) | S3E7 | Auntsgiving |
| 39 | 2016-11-16 | [Modern Family](https://www.imdb.com/title/tt1442437/) | S8E7 | Thanksgiving Jamboree |
| 40 | 2017-05-12 | [Master of None](https://www.imdb.com/title/tt4635276/) | S2E8 | Thanksgiving |
| 41 | 2017-11-14 | [Fresh Off the Boat](https://www.imdb.com/title/tt3551096/) | S4E7 | The Day After Thanksgiving |
| 42 | 2017-11-15 | [Modern Family](https://www.imdb.com/title/tt1442437/) | S9E7 | Winner Winner Turkey Dinner |
| 43 | 2019-11-20 | [Modern Family](https://www.imdb.com/title/tt1442437/) | S11E7 | The Last Thanksgiving |

<a id="thanksgiving-comedies-classic"></a>

### Comedies — Classic (pre-2000) (18)

[JSON](playlists/thanksgiving-comedies-classic.json)

| # | Aired | Show | Ep | Title |
|---|---|---|---|---|
| 1 | 1967-11-23 | [Bewitched](https://www.imdb.com/title/tt0057733/) | S4E12 | Samantha's Thanksgiving to Remember |
| 2 | 1975-11-22 | [The Bob Newhart Show](https://www.imdb.com/title/tt0068049/) | S4E11 | Over the River and Through the Woods |
| 3 | 1978-10-30 | [WKRP in Cincinnati](https://www.imdb.com/title/tt0077097/) | S1E7 | Turkeys Away |
| 4 | 1986-11-27 | [Cheers](https://www.imdb.com/title/tt0083399/) | S5E9 | Thanksgiving Orphans |
| 5 | 1991-11-26 | [Roseanne](https://www.imdb.com/title/tt0094540/) | S4E10 | Thanksgiving '91 |
| 6 | 1994-11-17 | [Friends](https://www.imdb.com/title/tt0108778/) | S1E9 | The One Where Underdog Gets Away |
| 7 | 1994-11-17 | [Seinfeld](https://www.imdb.com/title/tt0098904/) | S6E8 | The Mom & Pop Store |
| 8 | 1996-11-21 | [Friends](https://www.imdb.com/title/tt0108778/) | S3E9 | The One With the Football |
| 9 | 1996-11-22 | [Everybody Loves Raymond](https://www.imdb.com/title/tt0115167/) | S1E10 | Turkey or Fish |
| 10 | 1996-11-22 | [Boy Meets World](https://www.imdb.com/title/tt0105958/) | S4E10 | Turkey Day |
| 11 | 1996-11-26 | [Frasier](https://www.imdb.com/title/tt0106004/) | S4E7 | A Lilith Thanksgiving |
| 12 | 1997-11-20 | [Friends](https://www.imdb.com/title/tt0108778/) | S4E8 | The One With Chandler in a Box |
| 13 | 1998-11-19 | [Friends](https://www.imdb.com/title/tt0108778/) | S5E8 | The One With All the Thanksgivings |
| 14 | 1998-11-22 | [That '70s Show](https://www.imdb.com/title/tt0165598/) | S1E9 | Thanksgiving |
| 15 | 1998-11-24 | [Mad About You](https://www.imdb.com/title/tt0103484/) | S7E7 | The Thanksgiving Show |
| 16 | 1999-11-22 | [Everybody Loves Raymond](https://www.imdb.com/title/tt0115167/) | S4E9 | No Thanks |
| 17 | 1999-11-25 | [Friends](https://www.imdb.com/title/tt0108778/) | S6E9 | The One Where Ross Got High |
| 18 | 1999-11-25 | [Will & Grace](https://www.imdb.com/title/tt0157246/) | S2E7 | Homo for the Holidays |

<a id="thanksgiving-comedies-modern"></a>

### Comedies — Modern (2000+) (25)

[JSON](playlists/thanksgiving-comedies-modern.json)

| # | Aired | Show | Ep | Title |
|---|---|---|---|---|
| 1 | 2001-11-22 | [Friends](https://www.imdb.com/title/tt0108778/) | S8E9 | The One With the Rumor |
| 2 | 2001-11-22 | [Will & Grace](https://www.imdb.com/title/tt0157246/) | S4E9 | Moveable Feast (1) |
| 3 | 2001-11-22 | [Will & Grace](https://www.imdb.com/title/tt0157246/) | S4E10 | Moveable Feast (2) |
| 4 | 2002-11-21 | [Friends](https://www.imdb.com/title/tt0108778/) | S9E8 | The One With Rachel's Other Sister |
| 5 | 2002-11-26 | [Gilmore Girls](https://www.imdb.com/title/tt0238784/) | S3E9 | A Deep-Fried Korean Thanksgiving |
| 6 | 2003-11-20 | [Friends](https://www.imdb.com/title/tt0108778/) | S10E8 | The One With the Late Thanksgiving |
| 7 | 2005-11-21 | [How I Met Your Mother](https://www.imdb.com/title/tt0460649/) | S1E9 | Belly Full of Turkey |
| 8 | 2007-11-19 | [How I Met Your Mother](https://www.imdb.com/title/tt0460649/) | S3E9 | Slapsgiving |
| 9 | 2009-11-25 | [The Middle](https://www.imdb.com/title/tt1442464/) | S1E8 | Thanksgiving |
| 10 | 2011-11-15 | [New Girl](https://www.imdb.com/title/tt1826940/) | S1E6 | Thanksgiving |
| 11 | 2012-11-20 | [Happy Endings](https://www.imdb.com/title/tt1587678/) | S3E4 | More Like Stanksgiving |
| 12 | 2012-11-20 | [The Mindy Project](https://www.imdb.com/title/tt2211129/) | S1E6 | Thanksgiving |
| 13 | 2013-03-07 | [Community](https://www.imdb.com/title/tt1439629/) | S4E5 | Cooperative Escapism in Familial Relations |
| 14 | 2013-11-26 | [Brooklyn Nine-Nine](https://www.imdb.com/title/tt2467372/) | S1E10 | Thanksgiving |
| 15 | 2014-11-19 | [Modern Family](https://www.imdb.com/title/tt1442437/) | S6E8 | Three Turkeys |
| 16 | 2014-11-19 | [The Goldbergs](https://www.imdb.com/title/tt2712740/) | S2E7 | A Goldberg Thanksgiving |
| 17 | 2015-11-17 | [Fresh Off the Boat](https://www.imdb.com/title/tt3551096/) | S2E8 | Huangsgiving |
| 18 | 2016-11-10 | [Superstore](https://www.imdb.com/title/tt4477976/) | S2E9 | Black Friday |
| 19 | 2016-11-15 | [Fresh Off the Boat](https://www.imdb.com/title/tt3551096/) | S3E5 | No Thanks-giving |
| 20 | 2016-11-16 | [black-ish](https://www.imdb.com/title/tt3487356/) | S3E7 | Auntsgiving |
| 21 | 2016-11-16 | [Modern Family](https://www.imdb.com/title/tt1442437/) | S8E7 | Thanksgiving Jamboree |
| 22 | 2017-05-12 | [Master of None](https://www.imdb.com/title/tt4635276/) | S2E8 | Thanksgiving |
| 23 | 2017-11-14 | [Fresh Off the Boat](https://www.imdb.com/title/tt3551096/) | S4E7 | The Day After Thanksgiving |
| 24 | 2017-11-15 | [Modern Family](https://www.imdb.com/title/tt1442437/) | S9E7 | Winner Winner Turkey Dinner |
| 25 | 2019-11-20 | [Modern Family](https://www.imdb.com/title/tt1442437/) | S11E7 | The Last Thanksgiving |

<a id="thanksgiving-animation"></a>

### Animation (22)

[JSON](playlists/thanksgiving-animation.json)

| # | Aired | Show | Ep | Title |
|---|---|---|---|---|
| 1 | 1973-11-20 | [A Charlie Brown Thanksgiving](https://www.imdb.com/title/tt0068359/) | special | (TV special) |
| 2 | 1990-11-22 | [The Simpsons](https://www.imdb.com/title/tt0096697/) | S2E7 | Bart vs. Thanksgiving |
| 3 | 1997-10-21 | [Rugrats](https://www.imdb.com/title/tt0101188/) | S4E22 | The Turkey Who Came to Dinner |
| 4 | 1997-11-19 | [South Park](https://www.imdb.com/title/tt0121955/) | S1E8 | Starvin' Marvin |
| 5 | 1998-11-18 | [Hey Arnold!](https://www.imdb.com/title/tt0115200/) | S3E14 | Arnold's Thanksgiving |
| 6 | 1999-11-21 | [King of the Hill](https://www.imdb.com/title/tt0118375/) | S4E7 | The Hank's Giving Episode |
| 7 | 2011-11-09 | [South Park](https://www.imdb.com/title/tt0121955/) | S15E13 | A History Channel Thanksgiving |
| 8 | 2011-11-20 | [Family Guy](https://www.imdb.com/title/tt0182576/) | S10E6 | Thanksgiving |
| 9 | 2012-11-18 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S3E5 | An Indecent Thanksgiving Proposal |
| 10 | 2012-11-25 | [The Cleveland Show](https://www.imdb.com/title/tt1195935/) | S4E4 | Turkey Pot Die |
| 11 | 2013-11-24 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S4E5 | Turkey in a Can |
| 12 | 2013-11-24 | [American Dad!](https://www.imdb.com/title/tt0397306/) | S10E5 | Kung Pao Turkey |
| 13 | 2013-11-25 | [Regular Show](https://www.imdb.com/title/tt1710308/) | S5E12 | The Thanksgiving Special |
| 14 | 2014-11-16 | [Family Guy](https://www.imdb.com/title/tt0182576/) | S13E5 | Turkey Guys |
| 15 | 2014-11-23 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S5E4 | Dawn of the Peck |
| 16 | 2015-11-08 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S6E4 | Gayle Makin' Bob Sled |
| 17 | 2017-11-19 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S8E5 | Thanks-Hoarding |
| 18 | 2018-11-18 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S9E7 | I Bob Your Pardon |
| 19 | 2019-11-24 | [The Simpsons](https://www.imdb.com/title/tt0096697/) | S31E8 | Thanksgiving of Horror |
| 20 | 2019-11-24 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S10E8 | Now We're Not Cooking with Gas |
| 21 | 2021-07-25 | [Rick and Morty](https://www.imdb.com/title/tt2861424/) | S5E6 | Rick & Morty's Thanksploitation Spectacular |
| 22 | 2022-11-20 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S13E8 | Putts-giving |

<a id="thanksgiving-dramas"></a>

### Dramas (17)

[JSON](playlists/thanksgiving-dramas.json)

| # | Aired | Show | Ep | Title |
|---|---|---|---|---|
| 1 | 1973-11-15 | [The Waltons](https://www.imdb.com/title/tt0068149/) | S2E10 | The Thanksgiving Story |
| 2 | 1994-11-14 | [Party of Five](https://www.imdb.com/title/tt0108894/) | S1E10 | Thanksgiving |
| 3 | 1998-11-24 | [Felicity](https://www.imdb.com/title/tt0134247/) | S1E9 | Thanksgiving |
| 4 | 1999-11-23 | [Buffy the Vampire Slayer](https://www.imdb.com/title/tt0118276/) | S4E8 | Pangs |
| 5 | 2000-11-22 | [The West Wing](https://www.imdb.com/title/tt0200276/) | S2E8 | Shibboleth |
| 6 | 2001-04-15 | [The Sopranos](https://www.imdb.com/title/tt0141842/) | S3E8 | He is Risen |
| 7 | 2002-11-25 | [Everwood](https://www.imdb.com/title/tt0318883/) | S1E11 | A Thanksgiving Tale |
| 8 | 2005-11-20 | [Grey's Anatomy](https://www.imdb.com/title/tt0413573/) | S2E9 | Thanks for the Memories |
| 9 | 2006-11-16 | [Ugly Betty](https://www.imdb.com/title/tt0805669/) | S1E8 | Four Thanksgivings and a Funeral |
| 10 | 2007-11-28 | [Gossip Girl](https://www.imdb.com/title/tt0397442/) | S1E9 | Blair Waldorf Must Pie! |
| 11 | 2009-11-22 | [Dexter](https://www.imdb.com/title/tt0773262/) | S4E9 | Hungry Man |
| 12 | 2009-11-30 | [Gossip Girl](https://www.imdb.com/title/tt0397442/) | S3E11 | The Treasure of Serena Madre |
| 13 | 2010-02-10 | [Friday Night Lights](https://www.imdb.com/title/tt0758745/) | S4E13 | Thanksgiving |
| 14 | 2010-11-23 | [Parenthood](https://www.imdb.com/title/tt1416765/) | S2E10 | Happy Thanksgiving |
| 15 | 2016-11-22 | [This Is Us](https://www.imdb.com/title/tt5555260/) | S1E8 | Pilgrim Rick |
| 16 | 2018-07-01 | [Succession](https://www.imdb.com/title/tt7660850/) | S1E5 | I Went to Market |
| 17 | 2018-11-20 | [This Is Us](https://www.imdb.com/title/tt5555260/) | S3E8 | Six Thanksgivings |

<a id="thanksgiving-60s-80s"></a>

### 1960s–80s (6)

[JSON](playlists/thanksgiving-60s-80s.json)

| # | Aired | Show | Ep | Title |
|---|---|---|---|---|
| 1 | 1967-11-23 | [Bewitched](https://www.imdb.com/title/tt0057733/) | S4E12 | Samantha's Thanksgiving to Remember |
| 2 | 1973-11-15 | [The Waltons](https://www.imdb.com/title/tt0068149/) | S2E10 | The Thanksgiving Story |
| 3 | 1973-11-20 | [A Charlie Brown Thanksgiving](https://www.imdb.com/title/tt0068359/) | special | (TV special) |
| 4 | 1975-11-22 | [The Bob Newhart Show](https://www.imdb.com/title/tt0068049/) | S4E11 | Over the River and Through the Woods |
| 5 | 1978-10-30 | [WKRP in Cincinnati](https://www.imdb.com/title/tt0077097/) | S1E7 | Turkeys Away |
| 6 | 1986-11-27 | [Cheers](https://www.imdb.com/title/tt0083399/) | S5E9 | Thanksgiving Orphans |

<a id="thanksgiving-90s"></a>

### 1990s (22)

[JSON](playlists/thanksgiving-90s.json)

| # | Aired | Show | Ep | Title |
|---|---|---|---|---|
| 1 | 1990-11-22 | [The Simpsons](https://www.imdb.com/title/tt0096697/) | S2E7 | Bart vs. Thanksgiving |
| 2 | 1991-11-26 | [Roseanne](https://www.imdb.com/title/tt0094540/) | S4E10 | Thanksgiving '91 |
| 3 | 1994-11-14 | [Party of Five](https://www.imdb.com/title/tt0108894/) | S1E10 | Thanksgiving |
| 4 | 1994-11-17 | [Friends](https://www.imdb.com/title/tt0108778/) | S1E9 | The One Where Underdog Gets Away |
| 5 | 1994-11-17 | [Seinfeld](https://www.imdb.com/title/tt0098904/) | S6E8 | The Mom & Pop Store |
| 6 | 1996-11-21 | [Friends](https://www.imdb.com/title/tt0108778/) | S3E9 | The One With the Football |
| 7 | 1996-11-22 | [Everybody Loves Raymond](https://www.imdb.com/title/tt0115167/) | S1E10 | Turkey or Fish |
| 8 | 1996-11-22 | [Boy Meets World](https://www.imdb.com/title/tt0105958/) | S4E10 | Turkey Day |
| 9 | 1996-11-26 | [Frasier](https://www.imdb.com/title/tt0106004/) | S4E7 | A Lilith Thanksgiving |
| 10 | 1997-10-21 | [Rugrats](https://www.imdb.com/title/tt0101188/) | S4E22 | The Turkey Who Came to Dinner |
| 11 | 1997-11-19 | [South Park](https://www.imdb.com/title/tt0121955/) | S1E8 | Starvin' Marvin |
| 12 | 1997-11-20 | [Friends](https://www.imdb.com/title/tt0108778/) | S4E8 | The One With Chandler in a Box |
| 13 | 1998-11-18 | [Hey Arnold!](https://www.imdb.com/title/tt0115200/) | S3E14 | Arnold's Thanksgiving |
| 14 | 1998-11-19 | [Friends](https://www.imdb.com/title/tt0108778/) | S5E8 | The One With All the Thanksgivings |
| 15 | 1998-11-22 | [That '70s Show](https://www.imdb.com/title/tt0165598/) | S1E9 | Thanksgiving |
| 16 | 1998-11-24 | [Mad About You](https://www.imdb.com/title/tt0103484/) | S7E7 | The Thanksgiving Show |
| 17 | 1998-11-24 | [Felicity](https://www.imdb.com/title/tt0134247/) | S1E9 | Thanksgiving |
| 18 | 1999-11-21 | [King of the Hill](https://www.imdb.com/title/tt0118375/) | S4E7 | The Hank's Giving Episode |
| 19 | 1999-11-22 | [Everybody Loves Raymond](https://www.imdb.com/title/tt0115167/) | S4E9 | No Thanks |
| 20 | 1999-11-23 | [Buffy the Vampire Slayer](https://www.imdb.com/title/tt0118276/) | S4E8 | Pangs |
| 21 | 1999-11-25 | [Friends](https://www.imdb.com/title/tt0108778/) | S6E9 | The One Where Ross Got High |
| 22 | 1999-11-25 | [Will & Grace](https://www.imdb.com/title/tt0157246/) | S2E7 | Homo for the Holidays |

<a id="thanksgiving-2000s"></a>

### 2000s (17)

[JSON](playlists/thanksgiving-2000s.json)

| # | Aired | Show | Ep | Title |
|---|---|---|---|---|
| 1 | 2000-11-22 | [The West Wing](https://www.imdb.com/title/tt0200276/) | S2E8 | Shibboleth |
| 2 | 2001-04-15 | [The Sopranos](https://www.imdb.com/title/tt0141842/) | S3E8 | He is Risen |
| 3 | 2001-11-22 | [Friends](https://www.imdb.com/title/tt0108778/) | S8E9 | The One With the Rumor |
| 4 | 2001-11-22 | [Will & Grace](https://www.imdb.com/title/tt0157246/) | S4E9 | Moveable Feast (1) |
| 5 | 2001-11-22 | [Will & Grace](https://www.imdb.com/title/tt0157246/) | S4E10 | Moveable Feast (2) |
| 6 | 2002-11-21 | [Friends](https://www.imdb.com/title/tt0108778/) | S9E8 | The One With Rachel's Other Sister |
| 7 | 2002-11-25 | [Everwood](https://www.imdb.com/title/tt0318883/) | S1E11 | A Thanksgiving Tale |
| 8 | 2002-11-26 | [Gilmore Girls](https://www.imdb.com/title/tt0238784/) | S3E9 | A Deep-Fried Korean Thanksgiving |
| 9 | 2003-11-20 | [Friends](https://www.imdb.com/title/tt0108778/) | S10E8 | The One With the Late Thanksgiving |
| 10 | 2005-11-20 | [Grey's Anatomy](https://www.imdb.com/title/tt0413573/) | S2E9 | Thanks for the Memories |
| 11 | 2005-11-21 | [How I Met Your Mother](https://www.imdb.com/title/tt0460649/) | S1E9 | Belly Full of Turkey |
| 12 | 2006-11-16 | [Ugly Betty](https://www.imdb.com/title/tt0805669/) | S1E8 | Four Thanksgivings and a Funeral |
| 13 | 2007-11-19 | [How I Met Your Mother](https://www.imdb.com/title/tt0460649/) | S3E9 | Slapsgiving |
| 14 | 2007-11-28 | [Gossip Girl](https://www.imdb.com/title/tt0397442/) | S1E9 | Blair Waldorf Must Pie! |
| 15 | 2009-11-22 | [Dexter](https://www.imdb.com/title/tt0773262/) | S4E9 | Hungry Man |
| 16 | 2009-11-25 | [The Middle](https://www.imdb.com/title/tt1442464/) | S1E8 | Thanksgiving |
| 17 | 2009-11-30 | [Gossip Girl](https://www.imdb.com/title/tt0397442/) | S3E11 | The Treasure of Serena Madre |

<a id="thanksgiving-2010s-20s"></a>

### 2010s–20s (37)

[JSON](playlists/thanksgiving-2010s-20s.json)

| # | Aired | Show | Ep | Title |
|---|---|---|---|---|
| 1 | 2010-02-10 | [Friday Night Lights](https://www.imdb.com/title/tt0758745/) | S4E13 | Thanksgiving |
| 2 | 2010-11-23 | [Parenthood](https://www.imdb.com/title/tt1416765/) | S2E10 | Happy Thanksgiving |
| 3 | 2011-11-09 | [South Park](https://www.imdb.com/title/tt0121955/) | S15E13 | A History Channel Thanksgiving |
| 4 | 2011-11-15 | [New Girl](https://www.imdb.com/title/tt1826940/) | S1E6 | Thanksgiving |
| 5 | 2011-11-20 | [Family Guy](https://www.imdb.com/title/tt0182576/) | S10E6 | Thanksgiving |
| 6 | 2012-11-18 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S3E5 | An Indecent Thanksgiving Proposal |
| 7 | 2012-11-20 | [Happy Endings](https://www.imdb.com/title/tt1587678/) | S3E4 | More Like Stanksgiving |
| 8 | 2012-11-20 | [The Mindy Project](https://www.imdb.com/title/tt2211129/) | S1E6 | Thanksgiving |
| 9 | 2012-11-25 | [The Cleveland Show](https://www.imdb.com/title/tt1195935/) | S4E4 | Turkey Pot Die |
| 10 | 2013-03-07 | [Community](https://www.imdb.com/title/tt1439629/) | S4E5 | Cooperative Escapism in Familial Relations |
| 11 | 2013-11-24 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S4E5 | Turkey in a Can |
| 12 | 2013-11-24 | [American Dad!](https://www.imdb.com/title/tt0397306/) | S10E5 | Kung Pao Turkey |
| 13 | 2013-11-25 | [Regular Show](https://www.imdb.com/title/tt1710308/) | S5E12 | The Thanksgiving Special |
| 14 | 2013-11-26 | [Brooklyn Nine-Nine](https://www.imdb.com/title/tt2467372/) | S1E10 | Thanksgiving |
| 15 | 2014-11-16 | [Family Guy](https://www.imdb.com/title/tt0182576/) | S13E5 | Turkey Guys |
| 16 | 2014-11-19 | [Modern Family](https://www.imdb.com/title/tt1442437/) | S6E8 | Three Turkeys |
| 17 | 2014-11-19 | [The Goldbergs](https://www.imdb.com/title/tt2712740/) | S2E7 | A Goldberg Thanksgiving |
| 18 | 2014-11-23 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S5E4 | Dawn of the Peck |
| 19 | 2015-11-08 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S6E4 | Gayle Makin' Bob Sled |
| 20 | 2015-11-17 | [Fresh Off the Boat](https://www.imdb.com/title/tt3551096/) | S2E8 | Huangsgiving |
| 21 | 2016-11-10 | [Superstore](https://www.imdb.com/title/tt4477976/) | S2E9 | Black Friday |
| 22 | 2016-11-15 | [Fresh Off the Boat](https://www.imdb.com/title/tt3551096/) | S3E5 | No Thanks-giving |
| 23 | 2016-11-16 | [black-ish](https://www.imdb.com/title/tt3487356/) | S3E7 | Auntsgiving |
| 24 | 2016-11-16 | [Modern Family](https://www.imdb.com/title/tt1442437/) | S8E7 | Thanksgiving Jamboree |
| 25 | 2016-11-22 | [This Is Us](https://www.imdb.com/title/tt5555260/) | S1E8 | Pilgrim Rick |
| 26 | 2017-05-12 | [Master of None](https://www.imdb.com/title/tt4635276/) | S2E8 | Thanksgiving |
| 27 | 2017-11-14 | [Fresh Off the Boat](https://www.imdb.com/title/tt3551096/) | S4E7 | The Day After Thanksgiving |
| 28 | 2017-11-15 | [Modern Family](https://www.imdb.com/title/tt1442437/) | S9E7 | Winner Winner Turkey Dinner |
| 29 | 2017-11-19 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S8E5 | Thanks-Hoarding |
| 30 | 2018-07-01 | [Succession](https://www.imdb.com/title/tt7660850/) | S1E5 | I Went to Market |
| 31 | 2018-11-18 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S9E7 | I Bob Your Pardon |
| 32 | 2018-11-20 | [This Is Us](https://www.imdb.com/title/tt5555260/) | S3E8 | Six Thanksgivings |
| 33 | 2019-11-20 | [Modern Family](https://www.imdb.com/title/tt1442437/) | S11E7 | The Last Thanksgiving |
| 34 | 2019-11-24 | [The Simpsons](https://www.imdb.com/title/tt0096697/) | S31E8 | Thanksgiving of Horror |
| 35 | 2019-11-24 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S10E8 | Now We're Not Cooking with Gas |
| 36 | 2021-07-25 | [Rick and Morty](https://www.imdb.com/title/tt2861424/) | S5E6 | Rick & Morty's Thanksploitation Spectacular |
| 37 | 2022-11-20 | [Bob's Burgers](https://www.imdb.com/title/tt1561755/) | S13E8 | Putts-giving |

## Sources

Episode picks draw on published lists from [SlashFilm](https://www.slashfilm.com/2029276/best-thanksgiving-tv-episodes-ranked/), [Collider](https://collider.com/thanksgiving-tv-episodes-ranked/), [TheWrap](https://www.thewrap.com/best-thanksgiving-episodes-specials-of-all-time/), [Screen Rant](https://screenrant.com/thanksgiving-turkey-day-episodes-animated-series-tv-ranked/) and [CBR](https://www.cbr.com/best-cartoon-thanksgiving-episodes/). Episode data from [TVMaze](https://www.tvmaze.com/) (CC BY-SA).
