import infoutil

directionLongcodes = {
    "n": "North", "s": "South", "e": "East", "w": "West", 
    "ne": "North-East", "nw": "North-West", "se": "South-East", "sw": "South-West",
    "u": "up", "d": "down", "i": "in", "o": "out"
}

def list_inventory(roomID):
    # Returns (itemID, item name) for item in room
    inventory = []
    for itemID in infoutil.fetch('state', 'room', roomID)['inventory']:
        inventory.append((itemID, infoutil.name('item', itemID)))
    return inventory

def list_npcs(roomID):
    # Returns (npcID, npc name) for npc in room
    npcs = []
    for npc in infoutil.npcStates:
        if npc['location'] == roomID:
            npcs.append((npc['ID'], infoutil.name('npc', npc['ID'])))
    return npcs

def list_connections(roomID):
    # Returns (roomID, room name, direction shortcode, direction longcode) for connections in room
    connections = []
    for connection in infoutil.fetch('info', 'room', roomID)['connections']:
        connections.append((connection['room'], infoutil.name('room', connection['room']), connection['direction'], directionLongcodes[connection['direction']]))
    return connections

def describe(roomID):
    ## Create and return a description of the roomID in argument
    # Get the room's name and description
    name = infoutil.name('room', roomID).upper()
    description = infoutil.fetch('info', 'room', roomID)['description']

    # Get inventory, NPCs, and connections for the room
    inventory = list_inventory(roomID)
    npcs = list_npcs(roomID)
    connections = list_connections(roomID)

    # Format the room information as a string
    inventoryentence = u""
    for count, item in enumerate(inventory):
        inventoryentence += item[1]
        if len(inventory) - 2 == count: inventoryentence += u", and "
        elif len(inventory) - 1 != count: inventoryentence += u", "
        elif len(inventory) - 1 == count: inventoryentence += u" are here."

    npcSentence = u""
    for count, npc in enumerate(npcs):
        npcSentence += npc[1]
        if len(npcs) - 2 == count: npcSentence += u", and "
        elif len(npcs) - 1 != count: npcSentence += u", "
        if len(npcs) > 1 and len(npcs) - 1 == count: npcSentence += u" are here."
        elif len(npcs) == 1 and len(npcs) - 1 == count: npcSentence += u" is here."

    connectionSentence = u""
    if len(connections) > 1: connectionSentence += u"There is "
    for count, connection in enumerate(connections):
        connectionSentence += u"a " + connection[1] + u" to the " + connection[3]
        if len(connections) - 2 == count: connectionSentence += u", and "
        elif len(connections) - 1 != count: connectionSentence += u", "
        elif len(connections) - 1 == count: connectionSentence += u"."

    directionList = u"You can go "
    for count, connection in enumerate(connections):
        directionList += connection[3]
        if len(connections) - 2 == count: directionList += u", and "
        elif len(connections) - 1 != count: directionList += u", "
        elif len(connections) - 1 == count: directionList += u"."

    passageList = [description, inventoryentence, npcSentence, connectionSentence]
    passageStr = u""
    for sentence in passageList:
        if sentence != u"": passageStr += sentence[0].upper() + sentence[1:] + u" "
    return u"\n" + name + u"\n\n" + passageStr + u"\n\n" + directionList