from functions import TypeWriterEffect
from functions import wait
from functions import DrawFrame
from functions import ShowPlayerStats
from functions import SkipLines
from functions import Pause
from functions import InputName
from functions import ChooseInput

#importing classes
from entities import player

#initializing classes
plr = player()

DrawFrame()
InputName(plr)
DrawFrame()
ShowPlayerStats(plr)
print(ChooseInput("Enter 1 To Continue: ", [1]))

