import time
import subprocess
import shutil

## variables 
TerminalSize = shutil.get_terminal_size()
columns = TerminalSize.columns
lines = TerminalSize.lines

## sub functions
def ClearTerminal():
   subprocess.run("cls", shell = True)

def DrawLine(char):
   for i in range(columns):
        print(char, end = "")
   print()    

def SkipLines(lines):
   print("\n"*lines)


def CentreAlignText(text):
      length = len(text)
      n = int((columns - length)/2)
      print(" " * n, end = "", flush  = True)
      print(text)

def CentreAlignTypewriter(text):
    length = len(text)
    n = int((columns - length)/2)
    print(" " * n, end = "", flush  = True)
    TypeWriterEffect(text)

def CustomAlignText(n, text):
      print(" " * n, end = "", flush  = True)
      print(text)

def WriteHeading(text):
    CentreAlignText("-"*len(text))
    CentreAlignText(text)
    CentreAlignText("-"*len(text))

def LengthOfList(list):
    sum = 0
    for i in list:
        sum += len(i)
    return sum

def PrintList(list, gap, n):
    print(" "*n, end = "")
    for i in list:
        if gap:
            print(i, end = "")
            print(" "*gap, end = "")
        else:
            print(i)

## main functions
def wait(seconds): 
    time.sleep(seconds)

def TypeWriterEffect(text):
  for i in text:
     print(i, end = "", flush  = True)
     if i == '.' or i == ',':
        wait(0.7)
     else:
        wait(0.05)
  print()

def DrawFrame(loc = ""):
   ClearTerminal()
   DrawLine('=')
   CentreAlignText("THE GAUNTLET")
   DrawLine('=')
   if loc!="":
       CentreAlignText(loc)
   print()

def ShowPlayerStats(plr):
   WriteHeading(plr.Name)
   n = int((columns - len(plr.Name))/2)
   CustomAlignText(n, "Health = " + str(plr.Health))
   CustomAlignText(n, "Light Attack = " + str(plr.L_Attack))
   CustomAlignText(n, "Heavy Attack = " + str(plr.H_Attack))
   CustomAlignText(n, "Stamina = " + str(plr.Stamina))

def ShowPlayerStats(plr):
    WriteHeading(plr.Name)
    gap = 2   
    Attributes = ["HEALTH: "+str(plr.Health), "MANA: "+str(plr.Mana), "STAMINA: "+str(plr.Stamina)]
    Attacks = ["LIGHT ATTACK: "+str(plr.L_Attack), "HEAVY ATTACK: "+str(plr.H_Attack)]
    n_Attributes = int((columns-(LengthOfList(Attributes)+len(Attributes)*gap))/2)
    n_Attacks = int((columns-(LengthOfList(Attacks)+len(Attacks)*gap))/2)
    PrintList(Attributes, gap, n_Attributes)
    print()
    PrintList(Attacks, gap, n_Attacks)

def InputName(plr):
    text = "Enter Your Name: "
    length = len(text)
    n = int((columns - length)/2)
    print(" " * n, end = "", flush  = True)
    print(text, end = "")
    name = str(input())
    plr.Name = name

def ChooseInput(Range = [1] ,text = "Enter Choice: "):
    print()
    print("\033[999B", end="")
    Option = ""
    while Option not in Range:
        try:
            Option = int(input(text))
        except ValueError:
            print("Invalid Input")
            continue

        if Option not in Range:
            print("Invalid Input")

    return Option
         
class Choice:
    def Choose(options):
        for i, v in enumerate(options):
                CentreAlignText(v + "["+str(i+1)+"]")
        return ChooseInput(list(range(1,len(options)+1)))

def EnterScene(SceneName, plr):
    DrawFrame()
    CentreAlignTypewriter("You Entered the " + SceneName + "...")
    plr.Location = SceneName
    wait(0.2)

def Walk(plr,Scenes):
    options = []
    Scene = Scenes[plr.Location]
    for i in Scene.links:
        if plr.P_Location == i.name:
            options.append("Return to " + i.name)
        else:
            options.append("Enter " + i.name)

    c = Choice.Choose(options)
    NewScene = Scene.links[c-1].name
    plr.P_Location = plr.Location
    plr.Location = NewScene
    EnterScene(NewScene, plr)


def Advance(plr):
    ChooseInput([1], "Enter 1 To Continue: ")
    DrawFrame(plr.Location)





