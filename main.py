from functions import DrawFrame
from functions import ShowPlayerStats
from functions import InputName
from functions import ChooseInput
from functions import Walk
from functions import wait

#importing classes
from entities import player
from Scenes import Scene

#initializing entity classes
plr = player()

#initializing scene classes
Lobby = Scene("Lobby")

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

def Advance():
    ChooseInput([1], "Enter 1 To Continue: ")
    DrawFrame()

DrawFrame()
InputName(plr)
DrawFrame()
ShowPlayerStats(plr)
Advance()
plr.Location = "Forest"
game = True

while(game):
    Walk(plr,Scenes)
    Advance()







