from functions import CentreAlignTypewriter
from functions import Advance

#Scene Class
class Scene:
    def __init__(self, name):
        self.name = name
        self.links = []

#Specific Scene Functions

def PlayScene(plr):

    if plr.Location == "Bridge":

        CentreAlignTypewriter("You step forward, navigating the old, creaking wooden planks of the bridge...")
        Advance(plr)
        CentreAlignTypewriter("Suddenly, the structure violently sways. You freeze, gripping the frayed ropes with all your might.")
        Advance(plr)
        CentreAlignTypewriter("Through the mist, a small silhouette drops onto the center of the bridge, stepping slowly toward you...")
        Advance(plr)
        CentreAlignTypewriter("As the figure steps into view, your blood runs cold. It's a Troll!")
        Advance(plr)


    if plr.Location == "Cave":
        pass

    if plr.Location == "Forest":
        pass
        
