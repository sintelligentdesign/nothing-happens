# Game Package Builder
# Basically takes game src and stuffs it into a .zip so we don't have to. Very similar to ioutil but only has build-related stuff
import zipfile

from config import buildcfg

print "Building game from ./" + buildcfg['buildFile'] + "..."
# Create a zip archive and add the game data
with zipfile.ZipFile(buildcfg['buildFile'] + '.zip', 'w') as buildFile:
    buildFile.write('./' + buildcfg['buildFile'] + '/items.json')
    buildFile.write('./' + buildcfg['buildFile'] + '/npcs.json')
    buildFile.write('./' + buildcfg['buildFile'] + '/rooms.json')
    buildFile.write('./' + buildcfg['buildFile'] + '/states/itemStates.json')
    buildFile.write('./' + buildcfg['buildFile'] + '/states/npcStates.json')
    buildFile.write('./' + buildcfg['buildFile'] + '/states/roomStates.json')
    buildFile.write('./' + buildcfg['buildFile'] + '/states/playerState.json')
print "Done."