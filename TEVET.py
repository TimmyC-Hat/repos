######################################################################################
#CLASSES
######################################################################################
class Description:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Item(Description):
    def __init__(self, name, description, hydration, exhaustion, hunger, special = None):
        super().__init__(name, description)
        self.hydration = hydration
        self.exhaustion = exhaustion
        self.hunger = hunger
        self.special = special
    
    def use_special(self, player):
        if self.special:
            self.special(player)

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
        self.exhaustion += 5
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

######################################################################################
#LEVELS
######################################################################################
Threshold_1 = Level(
"Threshold Sublevel 1",
"An infinite labyrinth of sounds and smells. It absolutely reeks here, but you must push on."
)

Threshold_2 = Level(
"Threshold Sublevel 2",
"You wander aimlessly towards the only exit/entry you can find. More rooms can be seen further on and to the right. The exit doesn't seem that long from here."
)

Threshold_3 = Level(
"Threshold Sublevel 3",
"You continue on. What is with the monotone humming, you wonder. If only you can CHECK."
)

Threshold_4 = Level(
"Threshold Sublevel 4",
"A narrow corridor opens into a chamber of strange tapestries and a window into another room infront of you and a door to the left. The air feels heavier here and you can tell the way back is not the only path."
)

Threshold_5 = Level(
"Threshold Sublevel 5",
"The walls here hum softly and old door frames stand unused. It feels like a place where one must choose carefully between the onward path and the safer return."
)

Threshold_6 = Level(
"Threshold Sublevel 6",
"Entering the oncoming rooms has stung your eyes, you take a short break and spot a ladder propped up against the wall. Perhaps there is a way to TAKE it."
)

Threshold_7 = Level(
"Threshold Sublevel 7",
"A faint glow leaks through a crack in the ceiling. The walls are damp, and the path backward seems less certain than the right-hand route ahead."
)

Threshold_8 = Level(
"Threshold Sublevel 8",
"A window is seen to be on the walls, exposing the darkness outside. A crack can be seen going from corner to corner, maybe it can be broken."
)

Threshold_9 = Level(
"Threshold Sublevel 9",
"This passage narrows into a tight space, the air growing colder. Ahead is another turn, and behind you is the room that led you here."
)

Threshold_10 = Level(#maze
"Threshold Sublevel 10",
"A dark room unfolds before you. At first you see nothing. As your eyes adjust you realise the walls close around you. You look up and see a hole, maybe it could be accessed by a ladder."
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

######################################################################################
#EXITS
######################################################################################
Threshold_1.add_exit("forward", Threshold_2)

Threshold_2.add_exit("backward", Threshold_1)
Threshold_2.add_exit("forward", Threshold_4)
Threshold_2.add_exit("right", Threshold_3)

Threshold_3.add_exit("left", Threshold_2)

Threshold_4.add_exit("backward", Threshold_2)
Threshold_4.add_exit("left", Threshold_5)

Threshold_5.add_exit("right", Threshold_4)
Threshold_5.add_exit("forward", Threshold_8)

Threshold_6.add_exit("forward", Threshold_7)

Threshold_7.add_exit("backward", Threshold_6)
Threshold_7.add_exit("right", Threshold_8)

Threshold_8.add_exit("left", Threshold_7)
Threshold_8.add_exit("backward", Threshold_5)
Threshold_8.add_exit("right", Threshold_9)

Threshold_9.add_exit("left", Threshold_8)
Threshold_9.add_exit("right", Threshold_10)

Threshold_10.add_exit("left", Threshold_9)

######################################################################################
#ITEM SPECIAL FUNCTIONS
######################################################################################
def Ladder_special(player):
    if player.location == Threshold_10:
        Threshold_10.add_exit("up", Habitble_Zone)
        player.location = Habitble_Zone
        print("You prop the Ladder up and climb to the next zone.")
    else:
        print("You can't use the Ladder here!")


######################################################################################
#ITEMS
######################################################################################
almond_water = Item(
"Almond Water",
"A fresh bottle of water that has a hint of almond.",
20, 10, 5
)

cashew_water = Item(#QUESTION, THIS IS A HARMFUL THING, WILL NEGATIVES WORK?)
"Cashew Water",
"Reminds you of something familiar, with a hint of cashew.",
5, 20, 0
)

marshmallow = Item( #NEXT 2 ITEMS ALSO NEED HELP
"Marshmallow",
"A soft and squishy cylinder, looks tasty. Also creates a huge mess on your hands, reminder to wash it.",
0, -5, 5
)

greasy_marshmallow = Item(#special: NA
"Greasy Marshmallow",
"How the hell is a marshmallow greasy?",
-1, 10, 10
)

candy = Item(#special: NA
"Candy",
"A sweet treat to fill your teeth.",
0, 15, 5
)

stove = Item(#Merging system with almond water to create greasy marshmallow?!?!?
"Stovepot",
"A pot with an intense heat, maybe it can be used to cook something?",
0, 0, 0
)

key = Item(#special: for a door i presume?
"Key",
"Best you keep this incase locks appear",
0, 0, 0
)

ladder = Item(#special: go from level 0 to 1 if threshold_1 == p1.location
"Ladder",
"Its a ladder",
0, 0, 0,
Ladder_special
)

hammer = Item(#special: break window????
"Hammer",
"Seems like it can be used to break something",
0, 0, 0
)

######################################################################################
#ADDING ITEMS
######################################################################################
Threshold_3.add_item(almond_water)
Threshold_5.add_item(candy)
Threshold_6.add_item(ladder)
Threshold_8.add_item(marshmallow)

Habitble_Zone.add_item(cashew_water)

Sublimity.add_item(hammer)


######################################################################################
#MAIN PROGRAM
######################################################################################
if __name__ == "__main__":

    playername = input("What is your name? ")
    p1 = Player(playername, Threshold_1)

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
        
        choice = input("\nWhat will you do? (move [direction]/ quit): ").lower().split()
        
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
                found_item.use_special(p1)
                p1.inventory.remove(found_item)
            else:
                print(f"You aren't carrying '{target}'.")

        elif action == "check":
            if len(choice) > 1 and choice[1] in ("inv", "inventory"):
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