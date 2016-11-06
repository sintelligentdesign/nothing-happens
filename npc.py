import infoutil

def name(npcID):
    return infoutil.fetch('info', 'npc', npcID)['name']
    
def describe(npcID):
    return infoutil.fetch('info', 'npc', npcID)['description']
