# dndbeyond-reader

This project is meant to use the /json representation of the character pages to get information useful for the DM.

## Setting up

This project requires a .config folder on root with a dndbeyond.json file with the following format:

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

## TODO

* Try using the DM account to get all the characters in a campaign. Non-DM account only seem to be able to retrieve their own characters.
* Attempt to integrate with Twitch Auth API instead of copy pasting the request header.