# Game Variable & State Information Utility
# Stores and updates game vars and states for other modules to access and use
import os
import sys
import zipfile
import json

import ioutil
from config import filecfg

def fetch(dataType, objectType, thingID):
    ## Returns the state of or info for (as specified in args) a thing (room, item, or NPC) of type and ID specified in args
    thingList = []
    if dataType == 'state': thingList = get_state_for_objtype(objectType)
    elif dataType == 'info':
        # todo: get_info_for_objtype()??
        if objectType == 'item': thingList = gameItems
        elif objectType == 'npc': thingList = gameNpcs
        elif objectType == 'room': thingList = gameRooms

    for thing in thingList:
        if thing["ID"] == thingID:
            return thing

def update_state(objectType, objectID, state, status):
    # Updates the state of the given object
    thingList = get_state_for_objtype(objectType)
    for count, thing in enumerate(thingList):
        if thing["ID"] == objectID: thing[state] = status

def get_state_for_objtype(objectType):
    if objectType == 'item': return itemStates
    elif objectType == 'npc': return npcStates
    elif objectType == 'room': return roomStates
    elif objectType == 'player': return playerState

def add_item(holderObjectType, holderID, itemID):
    # Adds item with ID itemID to a holder with ID holderID
    inventory = fetch('state', holderObjectType, holderID)['inventory']
    inventory.append(itemID)
    update_state(holderObjectType, holderID, 'inventory', inventory)

def remove_item(holderObjectType, holderID, itemID):
    # Removes item with ID itemID from its holder with ID holderID
    inventory = fetch('state', holderObjectType, holderID)['inventory']
    inventory.remove(itemID)
    update_state(holderObjectType, holderID, 'inventory', inventory)

def name(objectType, thingID):
    # Returns as string the name of whatever the thingID specified in args
    return fetch('info', objectType, thingID)['name']

def save(): ioutil.save_game(playerState, roomStates, itemStates, npcStates)

def quit(): sys.exit()

print "Loading game data..."
# Load game data
gameRooms, gameItems, gameNpcs, playerState, roomStates, itemStates, npcStates =  ioutil.load_game_data()

print "Checking for save file..."
if not os.path.isfile(filecfg['saveFile'] + '.zip'):
    print "Save file not found. Creating a new save file..."
    save()
else: print "Save file found."

# Load save data
playerState, roomStates, itemStates, npcStates = ioutil.load_save()