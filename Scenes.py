from functions import CentreAlignTypewriter
from functions import Advance

from functions import BridgeQuest
from functions import DrawFrame

#Scene Class
class Scene:
    def __init__(self, name):
        self.name = name
        self.links = []


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

        print()
        CentreAlignTypewriter("TROLL: HALT, LITTLE HUMAN!")
        Advance(plr)

        CentreAlignTypewriter("TROLL: Not another step. This bridge belongs to ME!")
        Advance(plr)

        CentreAlignTypewriter("TROLL: Hundreds have crossed this river. Few have earned the privilege.")
        Advance(plr)

        CentreAlignTypewriter("TROLL: But perhaps... JUST perhaps... you possess something those fools lacked.")
        Advance(plr)

        CentreAlignTypewriter("TROLL: WITS!")
        Advance(plr)

        CentreAlignTypewriter("TROLL: Answer my question, little one, and I'll let you pass.")
        Advance(plr)

        CentreAlignTypewriter("TROLL: Answer incorrectly... and you'll become fish food.")
        Advance(plr)

        CentreAlignTypewriter("TROLL: Now, LISTEN CAREFULLY!")
        Advance(plr)

        CentreAlignTypewriter("TROLL: What has cities, but no houses; forests, but no trees; and rivers, but no water?")
        print()

        if BridgeQuest():
            DrawFrame()
            CentreAlignTypewriter("TROLL: ...")
            Advance(plr)

            CentreAlignTypewriter("TROLL: A MAP?!")
            Advance(plr)

            CentreAlignTypewriter("TROLL: Hmph. Clever little human.")
            Advance(plr)

            CentreAlignTypewriter("TROLL: Very well. A promise is a promise.")
            Advance(plr)

            CentreAlignTypewriter("TROLL: Go on, then. Before I change my mind!")
            Advance(plr)

            CentreAlignTypewriter("TROLL: And do try not to fall. I HATE fishing out corpses.")
            Advance(plr)

        else:
            DrawFrame()
            CentreAlignTypewriter("TROLL: BAHAHAHAHA!")
            Advance(plr)

            CentreAlignTypewriter("TROLL: Is THAT the best your tiny brain could produce?!")
            Advance(plr)

            CentreAlignTypewriter("TROLL: WRONG ANSWER!")
            Advance(plr)

            CentreAlignTypewriter("TROLL: Now... let's see how well you swim!")
            Advance(plr)

            CentreAlignTypewriter("TROLL: PREPARE YOURSELF, HUMAN!")
            Advance(plr)

    
    if plr.Location == "Cave":

        CentreAlignTypewriter("You cautiously approach the mouth of the cave...")
        Advance(plr)

        CentreAlignTypewriter("A chilling gust of wind escapes from within, carrying a strange, unfamiliar scent.")
        Advance(plr)

        CentreAlignTypewriter("You draw your sword and take your first steps into the darkness.")
        Advance(plr)

        CentreAlignTypewriter("The faint light from the entrance slowly disappears behind you.")
        Advance(plr)

        CentreAlignTypewriter("Drip... Drip... Drip...")
        Advance(plr)

        CentreAlignTypewriter("Water echoes somewhere deep within the cave.")
        Advance(plr)

        CentreAlignTypewriter("Suddenly, you hear something moving in the darkness ahead...")
        Advance(plr)

        CentreAlignTypewriter("You tighten your grip around your sword.")
        Advance(plr)

        CentreAlignTypewriter("Two glowing eyes appear in the darkness.")
        Advance(plr)

        CentreAlignTypewriter("Then another pair... and another!")
        Advance(plr)

        CentreAlignTypewriter("Three small figures slowly emerge from the shadows.")
        Advance(plr)

        CentreAlignTypewriter("Their twisted faces, sharp teeth and crude weapons leave little doubt.")
        Advance(plr)

        CentreAlignTypewriter("GOBLINS!")
        Advance(plr)

        CentreAlignTypewriter("GOBLIN 1: GRAAAK! KEE-KEE-KEE!")
        Advance(plr)

        CentreAlignTypewriter("GOBLIN 2: HURK! NAK NAK NAK!")
        Advance(plr)

        CentreAlignTypewriter("GOBLIN 3: SKRIIK! GRUKK GRUKK!")
        Advance(plr)

        CentreAlignTypewriter("The three goblins begin chattering furiously in their strange language.")
        Advance(plr)

        CentreAlignTypewriter("One of them points its rusty dagger at you.")
        Advance(plr)

        CentreAlignTypewriter("The other two respond with a series of excited squeals.")
        Advance(plr)

        CentreAlignTypewriter("Whatever they're saying, it certainly doesn't sound friendly.")
        Advance(plr)

        CentreAlignTypewriter("The goblins spread out, blocking your way.")
        Advance(plr)

        CentreAlignTypewriter("You raise your sword. There is no way around this.")
        Advance(plr)


