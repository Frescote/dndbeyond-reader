#dndbeyond-reader

This project is meant to use the /json representation of the character pages to get information useful for the DM.

## Setting up

This project requires a .config folder on root with a dndbeyond.json file like:

```
{
    "cookie": "",
    "base_url": "https://www.dndbeyond.com/",
    "character_urls": [
        "profile/Frescote/characters/5041786/json"
    ]
}
```

The cookie parameter is retrieved from logging in to DnDBeyond from your browser and checking the request headers when asking for a charater's JSON. 

## Running

```
py .\src\main.py
```