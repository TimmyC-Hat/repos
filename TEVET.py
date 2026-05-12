class Description:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Item(Description):
    def __init__(self, name, description, hydration, exhaustion, hunger):
        super().__init__(name, description)
        self.hydration = hydration
        self.exhaustion = exhaustion
        self.hunger = hunger

class Level(Description):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.exits = {}
        self.items = []

    def describe(self):
        print(f"""
{self.name}
{self.description}""")
        
    def add_item(self, item: Item):
        self.items.append(item)

    def add_exit(self, direction, room: "Level"):
        self.exits[direction] = room
                  
class Puzzle(Description):
    def __init__(self, name, description):
        super().__init__(name, description)

    def puzzle1_maze(self):
        pass

class Player():
    def __init__(self, name, location: Level):
        self.name = name
        self.hydration = 100
        self.exhaustion = 0
        self.hunger = 100
        self.location = location
        self.inventory = []
        self.is_alive = True

    def _drain_status_(self):
        self.hydration -= 5
        self.exhaustion += 10
        self.hunger -= 5
        if self.hunger <= 0 or self.exhaustion >= 100 or self.hunger <= 0:
            self.is_alive = False
    
    def use(self, item):
        self.hydration = min(100, self.hydration + item.hydration)
        self.exhaustion = max(0, self.exhaustion - item.exhaustion)
        self.hunger = min(100, self.hunger + item.hunger)

        print(f"You used {item.name}.")

    def move(self, direction):
        self.location = self.location.exits[direction]

Threshold = Level(#maze
"Level 0 : Threshold",
"An infinite labyrinth of sounds and smells. It absolutely reeks here, but you must push on.")

Threshold_1 = Level(
"Threshold Sublevel 1"
"desc"
)

Threshold_2 = Level(
"Threshold Sublevel 2"
"desc"
)

Threshold_3 = Level(
"Threshold Sublevel 3"
"desc"
)

Threshold_4 = Level(
"Threshold Sublevel 4"
"desc"
)

Threshold_5 = Level(
"Threshold Sublevel 5"
"desc"
)

Threshold_6 = Level(
"Threshold Sublevel 6"
"desc"
)

Threshold_7 = Level(
"Threshold Sublevel 7"
"desc"
)

Threshold_8 = Level(
"Threshold Sublevel 8"
"desc"
)

Threshold_9 = Level(
"Threshold Sublevel 9"
"desc"
)

Habitble_Zone = Level(#safe zone - puzzles
"Level 1 : Habitable Zone",
"You feel this place is somewhat safe. Best not to wander off to the dark parts, though, you hear ominous sounds in the unforseen.")

Office = Level(#'harder' puzzles
"Level 4 : Abandoned Office",
"An infinite and empty office. It's a bit creepy here but nothing to worry about.")

Level_FUN = Level(#mainline entity
"Level FUN =)",
"This place is awful, the music here sucks and the cake is stale. You swear you hear children having fun, but you're probably going crazy.")

Sublimity = Level(#meant to be a break - puzzle to find a fire exit hammer
"Level 37 : Sublimity",
"After such a journey, you're on edge, you can barely even sit down without feeling like something is right behind you, but seeing the water around you and the extra bottles of almond water make you feel relief.")

Window = Level(#could entity
"Level 188 : The Windows",
"The trip here has been nothing but exhausting, you just want to sit down and forget about everything, maybe even go home, but alas, you open another door and see that you're still trapped in this nightmare, just in a different scene. You look up to see almost endless hotel rooms, some that are blacked out, and some that have actual activity inside, but no human life. You're in for another wonderful adventure.")



Threshold.add_exit("up", Habitble_Zone)#add usage for ladder
Habitble_Zone.add_exit("down", Threshold)
Threshold.add_exit("left", Office)
Office.add_exit("down", Level_FUN)
Level_FUN.add_exit("up", Office)
Sublimity.add_exit("forward", Window)#break a window with hammer
Window.add_exit("backward", Sublimity)


almond_water = Item(
"Almond Water",
"A fresh bottle of water that has a hint of almond.",
20, 10, 5
)

cashew_water = Item(#QUESTION, THIS IS A HARMFUL THING, WILL NEGATIVES WORK?)
"Cashew Water",
"Reminds you of something familiar, with a hint of cashew.",
5, -20, 0
)

marshmallow = Item( #NEXT 2 ITEMS ALSO NEED HELP
"Marshmallow",
"A soft and squishy cylinder, looks tasty. Also creates a huge mess on your hands, reminder to wash it.",
0, -5, 5
)

greasy_marshmallow = Item(
"Greasy Marshmallow",
"How the hell is a marshmallow greasy?",
-1, 10, 10
)

candy = Item(
"Candy",
"A sweet treat to fill your teeth.",
0, 15, 5
)

stove = Item(#Merging system with almond water to create greasy marshmallow
"Stovepot",
"A pot with an intense heat, maybe it can be used to cook something?",
0, 0, 0
)

key = Item(
"Key",
"Best you keep this incase locks appear",
0, 0, 0
)

ladder = Item(#go from level 0 to 1
"Ladder",
"Its a ladder",
0, 0, 0
)

hammer = Item(
"Hammer",
"Seems like it can be used to break something",
0, 0, 0
)

Threshold.add_item(ladder)
Threshold.add_item(marshmallow)
Habitble_Zone.add_item(cashew_water)
Office.add_item(almond_water)
Sublimity.add_item(hammer)



if __name__ == "__main__":

    playername = input("What is your name?")
    p1 = Player(playername, Threshold)

    print("""
THE BACKROOMS - A Text Adventure
=================================
Escape the liminal spaces. Watch your hunger, thirst, and exhaustion.
Don't wander too long. Don't make noise. Don't look behind you.
"""
)
    while p1.is_alive:
        p1.location.describe()
        print(f"[ Stats - Hunger: {p1.hunger} | Hydration: {p1.hydration} | Exhaustion: {p1.exhaustion} ]")
        
        choice = input("\nWhat will you do? (move [direction]/ take [item] / use [item] / check [inv/room] / quit): ").lower().split()
        
        if not choice:
            continue

        action = choice[0]
        target = " ".join(choice[1:]) 

        if action == "move":
            if len(choice) > 1:
                direction = choice[1]
                if direction in p1.location.exits:
                    p1.move(direction)
                    p1._drain_status_() # Movement drains energy!
                    print(f"You moved {direction}.")
                else:
                    print(f"You can't go {direction} from here.")
            else:
                print("Move where? (e.g., 'move left')")

        elif action == "take":
            found_item = None
            # Search room for item
            for item in p1.location.items:
                if item.name.lower() == target:
                    found_item = item
                    break
            
            if found_item:
                p1.inventory.append(found_item)
                p1.location.items.remove(found_item)
                print(f"You picked up the {found_item.name}.")
            else:
                print(f"There is no '{target}' here.")
        
        elif action == "use":
            found_item = None
            # Search inventory for item
            for item in p1.inventory:
                if item.name.lower() == target:
                    found_item = item
                    break
            
            if found_item:
                p1.use(found_item)
                # If it's a ladder or hammer, you might not want to remove it
                if found_item.name not in ["Ladder", "Hammer", "Stovepot"]:
                    p1.inventory.remove(found_item)
            else:
                print(f"You aren't carrying '{target}'.")

        elif action == "check":
            if len(choice) > 1 and choice[1:] == "inv" or choice[1:] == "inventory":
                if p1.inventory:
                    print("\n--- Inventory ---")
                    for item in p1.inventory:
                        print(f"- {item.name}: {item.description}")
            elif len(choice) == 1:
                print("\n- Items in Room -")
                for i in p1.location.items:
                    print(f"- {i.name}")
            else:
                print("\nYour pockets are empty.")
       
        elif action == "quit":
            print("You gave up on finding the exit...")
            p1.is_alive = False
            break
        
        else:
            print(f"You whisper {''.join(choice)} to yourself. The walls fail to answer.")

        # Check if the player died during the last turn
        if not p1.is_alive:
            print("\nYou collapsed from exhaustion and faded away into the carpet...")
































































































'''print("""
Credits:
    Vedh Sudhesh 11SEN1
    Timmy Cheung 11SEN1
    Eden Li 11SEN1
    Gambler Timmy Friend
""")#TBR(to be removed)'''