# I/O Utility
# For interacting with .zip files and the filesystem
import os
import shutil
import zipfile
import json

from config import filecfg

def load_save():
    with zipfile.ZipFile(filecfg['saveFile'] + '.zip') as saveFile:
        playerState = json.loads(saveFile.read('_SAVE/playerState.json'))
        roomStates = json.loads(saveFile.read('_SAVE/roomStates.json'))
        itemStates = json.loads(saveFile.read('_SAVE/itemStates.json'))
        npcStates = json.loads(saveFile.read('_SAVE/npcStates.json'))
    return playerState, roomStates, itemStates, npcStates

def save_game(playerState, roomStates, itemStates, npcStates):
    print "Saving..."
    # Create a temporary save folder
    os.makedirs('_SAVE')

    # Put our save data in the folder
    with open('_SAVE/playerState.json', 'w') as statesFile: json.dump(playerState, statesFile)
    with open('_SAVE/roomStates.json', 'w') as statesFile: json.dump(roomStates, statesFile)
    with open('_SAVE/itemStates.json', 'w') as statesFile: json.dump(itemStates, statesFile)
    with open('_SAVE/npcStates.json', 'w') as statesFile: json.dump(npcStates, statesFile)

    # Create a zip archive and add our save data
    with zipfile.ZipFile(filecfg['saveFile'] + '.zip', 'w') as saveFile:
        saveFile.write('_SAVE/playerState.json')
        saveFile.write('_SAVE/roomStates.json')
        saveFile.write('_SAVE/itemStates.json')
        saveFile.write('_SAVE/npcStates.json')

    # Delete the temporary save folder
    shutil.rmtree('_SAVE')
    print "Game saved."

def load_game_data():
    with zipfile.ZipFile(filecfg['gameFile'] + '.zip') as gameFile:
        rooms = json.loads(gameFile.read(filecfg['gameFile'] + '/rooms.json'))
        items = json.loads(gameFile.read(filecfg['gameFile'] + '/items.json'))
        npcs = json.loads(gameFile.read(filecfg['gameFile'] + '/npcs.json'))
        playerState = json.loads(gameFile.read(filecfg['gameFile'] + '/states/playerState.json'))
        roomStates = json.loads(gameFile.read(filecfg['gameFile'] + '/states/roomStates.json'))
        itemStates = json.loads(gameFile.read(filecfg['gameFile'] + '/states/itemStates.json'))
        npcStates = json.loads(gameFile.read(filecfg['gameFile'] + '/states/npcStates.json'))
    return rooms, items, npcs, playerState, roomStates, itemStates, npcStates