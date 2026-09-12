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

def CenterAlignedText(text):
   length = len(text)
   n = int((columns - length)/2)
   print(" " * n, end = "", flush  = True)
   print(text)


## main functions
def wait(seconds): 
    time.sleep(seconds)

def TypeWriterEffect(text):
  for i in text:
     if i == '.':
        wait(0.7)
     else:
        wait(0.05)
     print(i, end = "", flush  = True)
  print()

def DrawFrame():
   ClearTerminal()
   DrawLine('=')
   CenterAlignedText("THE GAUNTLET")
   DrawLine('=')
   print()

