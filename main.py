import random
import time

locations = {"House": "5",
             "Cabin": "2",
             "Two-Story": "6",
             "Department Store": "4",
             "Gas Station": "2",
             "Apartment": "3"}
items = ["Bandage","Bat","Crowbar"]
weapons = {"Bat": 20,
           "Crowbar": 35}


class Character:
    def __init__(self, name, money, health, damage, accuracy, stamina, knownLocations, items, weapon):
        self.name = name
        self.money = money
        self.health = health
        self.damage = damage
        self.accuracy = accuracy
        self.stamina = stamina
        self.knownLocations = []
        self.items = {}
        self.weapon = weapon
def delay(d):
    time.sleep(d)
def chooseActivity():
    choice = input("Would you like to Scout, Forage, or Repair? S / F / R\n")
    print()
    return choice
def chooseLocation():
    num = 1
    for i in user.knownLocations:
        selectDict = {num: i}

        print("[{}] {}".format(num, i))
        num += 1
    choiceNum = int(input("Where would you like to go?\n"))



    return selectDict[choiceNum]

def foundLocation():

    location = random.choice(list(locations.keys()))
    print()
    print("------Location Found------")
    print("         ",location)
    print("--------------------------")
    return location
def foundItem():
    item = random.choice(list(items))
    if item in user.items.keys():
        if user.items[item] >= 5:
            print("You can only carry 5 {}.".format(item))
            return
        user.items[item] += 1
        print("Found another {} you now have {}.".format(item, user.items[item]))
    else:
        user.items[item] = 1
def displayHealth(opponentHealth):
    health = int(opponentHealth)
    print("----------HEALTH----------")
    print("  ",(('\U00002665' + " ") * health ),(('\U00002661' + " ")*(health - 10)))
    print("---        {}HP        ---".format(opponentHealth))
    print("--------------------------")

    delay(1)
def useItem():
    num = 1
    if not user.items:
        print("You have no items to use.\n")
        delay(1)
        return
    delay(1)
    for i in user.items:
        selectDict = {num: i}

        print("[{}] {}".format(num, i))
        num += 1

    choiceNum = int(input("Would you like to use an item?\n"))
    item = selectDict[choiceNum]
    delay(1)
    if item == 'Bandage':
        useBandage()
    elif item in weapons:
        if user.weapon != None:
            print("Now Throwing away your {}.\n".format(user.weapon))
            user.damage -= weapons[user.weapon]
            user.weapon = None
            delay(1)
        print("Now using the {} for your weapon.\n".format(item))
        user.weapon = item
        user.damage = weapons[item]
    else:
        return
def useBandage():
    bandageCount = user.items["Bandage"]
    if bandageCount == 0:
        print("No bandages to use.")
    else:
        if user.health > 90:
            bandage = 100 - user.health
            user.health += bandage
        else:
            user.health += 10
        print("Applying bandage...")
        delay(3)
        print(f"Player now has {user.health} health.\n")


def printKnownLocations():

    if len(user.knownLocations) == 0:
        print("No known locations.\n")
        return
    print("-----Known Locations:-----")
    for i in user.knownLocations:
        print(i)
    print()
    delay(2)
def debugVal(value):
    print("- # debug -# {} #-".format(value))
def fight():
    opponentHealth = 10
    print("--------------------------")
    print("***ENCOUNTERED A ZOMBIE***")
    print("--------------------------\n\n")
    xpEarned = 0
    lastHitChance = 100
    while opponentHealth > 0:

        displayHealth(opponentHealth)


        userInput = input("Fight? Use a Bandage or Run? ( F / B / R )\n")
        userInput = userInput.lower().strip()



        if userInput == 'f':

            hitChance = random.randint(1,100) + user.accuracy
            debugVal(hitChance)
            debugVal(lastHitChance)

            if lastHitChance < 50:
                hitChance += 15

            if hitChance > 50:
                damageDone = random.randint(1,3) + (user.damage / 10)
                critChance = random.randint(1,100) + ((user.accuracy+user.stamina)/8)
                if critChance < 15:
                    damageDone = damageDone * 1.25
                    print("**************************")
                    print("!!!    CRITICAL HIT    !!!")
                    xpEarned += 2
                else:
                    print("!!! Hit !!!")



                opponentHealth -= damageDone
                print("--Zombie was hit for {} HP--\n".format(damageDone))

                xpEarned += 2

            ### add XP EARNED##


            lastHitChance = hitChance

        elif userInput == "b":
            useBandage()
        else:
            if random.randint(1, 10) > 4:
                print("**** Successfully Escaped ****")
                return
        delay(1)
    print("**************************")
    print("    Zombie was killed")
    print("**************************")








    print()
def doActivity(choice):
    activityLoop = True
    while activityLoop:
        reward = random.randint(1, 100)
        risk = random.randint(1, 100)
        if choice == "s":

            print("Scouting nearby areas for materials...")
            delay(3)

            # make decision



            if reward > 40:

                print("Found a location to Forage!")
                delay(1)
                location = foundLocation()
                user.knownLocations.append(location)
                delay(1)
                if risk < 20:
                    fight()
                activityLoop = False

            elif reward < 40:
                print("No luck finding a location to forage...")
                delay(1)
                if risk < 5:
                    fight()
                activityLoop = False
        elif choice =="f":
            delay(1)
            location = chooseLocation()
            print("Travelling to the {}".format(location))
            delay(2)
            if risk < 30:
                fight()
                if risk < 5:
                    fight()

            if reward > 60:
                foundItem()
            elif reward < 60:
                print("No luck finding any items here..")
            user.knownLocations.remove(location)
            activityLoop = False


        elif choice == "r":
            activityLoop = False
            pass
        else:
            activityLoop = True
            pass

# Sets up the game with name and instructions on how to play.
def setupGame():
    print()
    print("Welcome to\n")
    delay(1)
    print("*********************************")
    delay(.7)
    print("*********************************\n")
    delay(.7)
    print("__________            ___.   .__ ")
    delay(1)
    print("\____    /____   _____\_ |__ |__|")
    delay(.7)
    print("  /     //  _ \ /     \| __ \|  |")
    delay(.7)
    print(" /  ___/(  <_> )  Y Y  \ \_\ \  |")
    delay(.7)
    print("/_______ \____/|__|_|  /___  /__|")
    delay(.7)
    print("        \/           \/    \/    \n")
    delay(.7)
    print("*********************************")
    delay(.7)
    print("*********************************")
    print("\n\n")
    delay(1)
    print("\n\n")
    delay(1)

    name = input("What is your characters name?\nType Here: ")
    delay(1)
    print("Nice to meet you, {}.".format(name))
    delay(1)
    print("The names is J for Johnny, Knoxville.\n\n")
    print()
    delay(1)
    print("Here you will start each of your days. You have the choice to complete 3 activities during your daylight hours.")
    delay(3)
    print("These choices will impact your day to day experience as well as defending the base from zombies at night.")
    delay(3)
    print("Try to survive the longest that you can!")
    delay(3)
    print("Game starting...")
    delay(3)
    print("Get ready!\n\n")
    delay(1)
    return name
name = setupGame()
day = 1
user = Character(name, 0, 100, 10, 10, 10, [], {"Bandage": 1}, None)
GameLoop = True
DayLoop = True

#choose the activity loop.
def chooseTwo():
    for i in range(2):
        choice = chooseActivity()
        doActivity(choice)

#after main loop you can choose to look at items locations or continue.
def postActivity():
    
    ActivityLoop = True
    while ActivityLoop:
        userInput = input("Would you like to see your items, known locations, or continue? ( i, l, c)\n")
        if userInput == "i":
            useItem()
        elif userInput == "l":
            printKnownLocations()
            
        else:
            ActivityLoop = False
    delay(1)
    print()


while GameLoop:

    while DayLoop:

        print("Day ", day)
        print("--------------------------\n")
        print("Good Morning, {}".format(user.name))
        delay(1)
        print("You have 12 hours to complete 2 activities.")
        delay(1)
        chooseTwo()

        postActivity()


        day += 1
