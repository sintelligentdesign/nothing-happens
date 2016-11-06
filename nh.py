import ioutil
import infoutil
import player
import room
import item
import npc

while True:
    ## Main game loop
    # Get the player's command
    command = raw_input("\n" + infoutil.name('room', infoutil.fetch('state', 'player', '0')['location']).upper() + " :: ").lower().split(' ')
    print player.do(command)