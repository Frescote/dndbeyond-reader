import requests
import json
from enum import Enum

class Stat(Enum):
    STR = 0
    DEX = 1
    CON = 2
    INT = 3
    WIS = 4
    CHA = 5

def getPerception(character):
    character = character['character']
    return { character['name']: character['stats'][Stat.WIS.value]['value'] + (character['bonusStats'][Stat.WIS.value]['value'] or 0) }

def getCharacterFromDndBeyond(cookie, characterLink):
    headers = {'cookie': cookie }

    return json.loads(requests.get(characterLink, headers=headers).content)

def loadConfig(configPath):
    with open(configPath) as configJson:
        data = json.load(configJson)
    return { 'cookie': data['cookie'], 'character_urls': list(map(lambda character_url: data['base_url'] + character_url, data['character_urls']))}

config = loadConfig('.config/dndbeyond.json')

characters = list(map(lambda url: getCharacterFromDndBeyond(config['cookie'], url), config['character_urls']))

print('Passive Perception: ' + str(list(map(lambda character: getPerception(character), characters))))