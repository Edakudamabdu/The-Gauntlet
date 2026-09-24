from functions import TypeWriterEffect
from functions import wait
from functions import DrawFrame
from functions import ShowPlayerStats
from functions import InputName
from functions import ChooseInput
from functions import Choice

#importing classes
from entities import player

#initializing classes
plr = player()

DrawFrame()
InputName(plr)
DrawFrame()
ShowPlayerStats(plr)
ChooseInput([1], "Enter 1 To Continue: ")
DrawFrame()
Choice(["Enter Forest", "Enter Cave"])



