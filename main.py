from functions import DrawFrame
from functions import ShowPlayerStats
from functions import InputName
from functions import Advance
from functions import Walk
from functions import CentreAlignTypewriter

#importing classes
from entities import player
from Scenes import Scene
from Scenes import PlayScene

#initializing entity classes
plr = player()

#initializing scene classes
Lobby = Scene("")

Forest = Scene("Forest")
Cave = Scene("Cave")
Bridge = Scene("Bridge")

Scenes = {

        "Lobby":Lobby,
        "Forest":Forest,
        "Cave":Cave,
        "Bridge":Bridge

        }

Forest.links.append(Cave)
Forest.links.append(Bridge)

Cave.links.append(Forest)

Bridge.links.append(Forest)

DrawFrame()
InputName(plr)
DrawFrame()

ShowPlayerStats(plr)

plr.Location = "Forest"
game = True

Advance(plr)

CentreAlignTypewriter("You awaken on the cold forest floor, clutching nothing but a bare sword...")
Advance(plr)
CentreAlignTypewriter("The dense, suffocating trees seem to stretch on forever, until the canopy suddenly breaks...")
Advance(plr)
CentreAlignTypewriter("Before you lies a quiet clearing. To your left, a yawning cave dips into total darkness. To your right, a weathered stone bridge spans a rushing river. Where will you go?")
Advance(plr)

while(game):
    Walk(plr,Scenes)
    Advance(plr)
    PlayScene(plr)











