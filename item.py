import infoutil

def name(itemID): return infoutil.fetch('info', 'item', itemID)['name']
def describe(itemID): return infoutil.fetch('info', 'item', itemID)['description']
def synonyms(itemID): return infoutil.fetch('info', 'item', itemID)['synonyms'].split(', ')

def commands(itemID): return infoutil.fetch('info', 'item', itemID)['actions']

# todo: get started on item commands
def state_value(itemID, state): pass

def describe_state(itemID, state, value): pass

def change_state_value(itemID, state, newValue): pass