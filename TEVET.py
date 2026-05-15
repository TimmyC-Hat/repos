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

class Riddle(Description):
    def __init__(self, name, description, question, answer):
        super().__init__(name, description)
        self.question = question
        self.answer = answer.lower()

    def ask_riddle(self):
        print(f"\n{self.description}\n{self.question}")
        user_answer = input("Your answer: ").lower().strip()
        return user_answer == self.answer

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
"An infinite labyrinth of sounds and smells. It absolutely reeks here, but you must go FORWARD."
)

Threshold_2 = Level(
"Threshold Sublevel 2",
"You wander aimlessly towards the only exit/entry you can find. More rooms can be seen further on and to the RIGHT. You could always go BACKWARD but the exit doesn't seem that long from here."
)

Threshold_3 = Level(
"Threshold Sublevel 3",
"You continue on. What is with the monotone humming, you wonder. If only you can CHECK."
)

Threshold_4 = Level(
"Threshold Sublevel 4",
"A narrow corridor opens into a chamber of strange tapestries and a window into another room infront of you and a door to the LEFT. The air feels heavier here and you can tell the way back is not the only path."
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

Habitable_1 = Level(
"Habitable Sublevel 1",
"A serene area with soft lighting. Paths lead in multiple directions, but you sense safety here."
)

Habitable_2 = Level(
"Habitable Sublevel 2",
"The air is fresh, and you can hear distant echoes. Forward seems inviting."
)

Habitable_3 = Level(
"Habitable Sublevel 3",
"Comfortable surroundings with subtle hums. You can go left or right."
)

Habitable_4 = Level(
"Habitable Sublevel 4",
"A quiet chamber. The way ahead feels promising."
)

Habitable_5 = Level(
"Habitable Sublevel 5",
"You notice an inscription on the left wall. Perhaps you can READ it."
)

Habitable_6 = Level(
"Habitable Sublevel 6",
"Continuing through the safe zones. The path branches."
)

Habitable_7 = Level(
"Habitable Sublevel 7",
"A restful spot with gentle breezes."
)

Habitable_8 = Level(
"Habitable Sublevel 8",
"The environment feels stable. Forward or backward?"
)

Habitable_9 = Level(
"Habitable Sublevel 9",
"Nearing the end of this zone. A sense of accomplishment."
)

Habitable_10 = Level(
"Habitable Sublevel 10",
"The final sublevel. Another inscription awaits on the left."
)

Final_Level = Level(
"Escape Point",
"You have reached the end of the Habitable Zone. Freedom awaits!"
)
######################################################################################
#Threshold EXITS
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
#HABITABLE ZONE EXITS
######################################################################################
Habitble_Zone.add_exit("forward", Habitable_1)

Habitable_1.add_exit("backward", Habitble_Zone)
Habitable_1.add_exit("right", Habitable_2)
Habitable_1.add_exit("left", Habitable_4)

Habitable_2.add_exit("right", Habitable_3)
Habitable_2.add_exit("left", Habitable_1)


Habitable_3.add_exit("left", Habitable_2)

Habitable_4.add_exit("right", Habitable_1)
Habitable_4.add_exit("left", Habitable_5)

Habitable_5.add_exit("right", Habitable_4)
# Forward exit will be added after riddle

Habitable_6.add_exit("backward", Habitable_5)
Habitable_6.add_exit("forward", Habitable_7)

Habitable_7.add_exit("backward", Habitable_6)
Habitable_7.add_exit("right", Habitable_8)

Habitable_8.add_exit("left", Habitable_7)
Habitable_8.add_exit("right", Habitable_9)

Habitable_9.add_exit("left", Habitable_8)
Habitable_9.add_exit("right", Habitable_10)

Habitable_10.add_exit("left", Habitable_9)
# Forward exit will be added after riddle

Final_Level.add_exit("backward", Habitable_10)

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
10, 20, 0
)

marshmallow = Item( #NEXT 2 ITEMS ALSO NEED HELP
"Marshmallow",
"A soft and squishy cylinder, looks tasty. Also creates a huge mess on your hands, reminder to wash it.",
5, 5, 10
)

greasy_marshmallow = Item( #special: NA
"Greasy Marshmallow",
"How the hell is a marshmallow greasy?",
-1, 10, 10
)

candy = Item(
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
Threshold_9.add_item(marshmallow)

Habitble_Zone.add_item(cashew_water)
Habitable_3.add_item(candy)
Habitable_7.add_item(marshmallow)
Habitable_10.add_item(candy)

######################################################################################
#RIDDLES
######################################################################################
riddle_5 = Riddle(
"Wall Inscription",
"An ancient riddle etched into the wall.",
"What has keys but can't open locks?",
"piano"
)

riddle_10 = Riddle(
"Glowing Text",
"A mysterious glowing inscription.",
"What comes once in a minute, twice in a moment, but never in a thousand years?",
"m"
)


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
        
        if p1.location == Final_Level:
            print("\nCongratulations! You have escaped the Backrooms!")
            break
        
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
        
        elif action == "read":
            if target == "left" and p1.location == Habitable_5:
                if riddle_5.ask_riddle():
                    print("Correct! A path forward opens.")
                    Habitable_5.add_exit("forward", Habitable_6)
                else:
                    print("Incorrect. Try again.")
            elif target == "left" and p1.location == Habitable_10:
                if riddle_10.ask_riddle():
                    print("Correct! A path forward opens.")
                    Habitable_10.add_exit("forward", Final_Level)
                else:
                    print("Incorrect. Try again.")
            else:
                print("Nothing to read here.")
       
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
    Vedh Sudhesh 1COMP1
    Timmy Cheung 11SEN1
    Eden Li 11SEN1
    Gambler Timmy Friend
""")#TBR(to be removed)'''