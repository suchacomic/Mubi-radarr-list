# Mubi-radarr-list

<p align="left">
	<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

Scrapes [Mubi](https://www.mubi.com/showing) for movies and produces a StevenLu type list for radarr.
> This was inspired by Steven Lu's list (https://github.com/sjlu/popular-movies).

Uses beautifulsoup4 library for scraping and omdbapi library for movie metadata

# Radarr
This list uses a structure that is compatible with the StevenLuImport (https://github.com/Radarr/Radarr/wiki/Supported-NetImports#stevenluimport).
so you can just plug this list in the url field.

# Open Movie Database ([OMDb](https://www.omdbapi.com))

Uses the OMDB api, so needs a api key.
[genrate a key.](https://www.omdbapi.com/apikey.aspx)

# Dependencies
1. [omdbapi](https://pypi.org/project/omdbapi/)
2. [tqdm](https://pypi.org/project/tqdm/)
3. [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
4. [requests](https://pypi.org/project/requests/)

 or just
```
pip install requirements.txt
```
 also minimum python version 3.8 is required.

# Initializing

just paste your OMDB api in main.py

# FYI
+ This is my first ever useful (and working) script, so it's sloppy
+ you'll need to host the output file somewhere as the url field for lists in radarr only accepts suprisingly, urls and not local adresses.
