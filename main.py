import random
import time

debug = True
locations = {"House": "5",
             "Cabin": "2",
             "Two-Story": "6",
             "Department Store": "4",
             "Gas Station": "2",
             "Apartment": "3"}


items = ["Bandage","Bat","Crowbar"]
weapons = {"Bat": 20,
           "Crowbar": 35}
class Base:
    def __init__(self,health,nightDamage):
        self.health = health
        self.nightDamage = nightDamage
    def setHealth(self, newHealth):
        self.health = newHealth
class Location:
    def __init__(self, name, rarity, value):
        self.name = name
        self.rarity = rarity
        self.value = value
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
    choice = ""
    choices = ["s","f","r"]
    while choice not in choices:
        choice = input("Would you like to Scout, Forage, or Repair? S / F / R\n").lower()

    print()
    return choice
def chooseLocation():
    num = 1

    for i in user.knownLocations:
        selectDict = {num: i}

        print("[{}] {}".format(num, i))
        num += 1

    choiceNum = int(input("Where would you like to go?\n"))


    print(selectDict[choiceNum])
    return selectDict[choiceNum]

def foundLocation():

    location = random.choice(list(locations.keys()))
    print()
    print("------Location Found------")
    print("         ",location)
    print("--------------------------")
    return location
def foundRandomItem():
    item = random.choice(list(items))
    addItem(item)
def addItem(item):
    print(f"You found one {item}!")
    if item in user.items.keys():
        if user.items[item] >= 5:
            print("You can only carry 5 {}.".format(item))
            return
        user.items[item] += 1
    else:
        user.items[item] = 1
    print("You now have {}.".format(user.items[item]))
def displayHealth(opponentHealth):
    health = int(opponentHealth)
    print("----------HEALTH----------")
    print("  ",(('\U00002665' + " ") * health ),(('\U00002661' + " ")*(health - 10)))
    print("---        {}HP        ---".format(opponentHealth))
    print("--------------------------")

    delay(1)
def useItem():
    num = 1
    choiceNum = 0
    if not user.items:
        print("You have no items to use.\n")
        delay(1)
        return
    delay(1)
    for item in user.items:
        selectDict = {num: item}

        print(f"[{num}] {item} ({user.items[item]})")
        num += 1
    nums = list(selectDict.keys())
    print(nums)
    while choiceNum not in nums:

        choiceNum = input("Would you like to use an item?\n")
        print(choiceNum)
        print("Press Enter if you do not want to use an item.")
        if choiceNum == "":
            return





    item = int(selectDict[choiceNum])
    delay(1)
    if item == 'Bandage':
        useBandage()
    elif item in weapons:
        oldDamage = user.damage
        if user.weapon != None:
            print("Now Throwing away your {}.\n".format(user.weapon))
            user.damage -= weapons[user.weapon]
            user.weapon = None
            delay(1)
        print("Now using the {} for your weapon.\n".format(item))

        user.weapon = item
        user.items[item] -= 1
        user.damage = weapons[item]
        print(f"You now have {user.damage} Damage, before you had {oldDamage} Damage")
    else:
        return
    if user.items[item] < 1:
        user.items.pop(item)


def useBandage():
    bandageCount = user.items["Bandage"]
    if user.health == 100:
        print("You do not need to use a bandage right now...")
    if bandageCount == 0:
        print("No bandages to use.")
    else:
        if user.health > 90:
            bandage = 100 - user.health
            user.health += bandage
            user.items["Bandage"] = bandageCount
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
    if debug == True:
        print("- # debug -# {} #-".format(value))
def simulateFight():
    opponentHealth = day + 9
    xpEarned = 0
    lastHitChance = 100
    while opponentHealth > 0 and user.health > 0:
        hitChance = random.randint(1, 100) + user.accuracy
        oHitChance = random.randint(1, 100)
        # Checks if the last hit chance is below 50, if it is a slight buff is applied.
        if lastHitChance < 50:
            hitChance += 15 * (day/2)
        lastHitChance = hitChance
        # Executes a hit
        if hitChance > 50:
            damageDone = random.randint(1, 3) + (user.damage / 10)
            critChance = random.randint(1, 100) + ((user.accuracy + user.stamina) / 8)
            if critChance < 15:
                damageDone = damageDone * 1.5
                xpEarned += 2
            opponentHealth -= damageDone

            xpEarned += 2
            if opponentHealth < 0:
                print("**************************")
                print("    Zombie was killed")
                print("**************************")
                if random.randint(1,2) == 2:
                    addItem("Bandage")
                return
            displayHealth(opponentHealth)

            ### add XP EARNED##
        if oHitChance > 40:
            oHitDamage = random.randint(int(day/2),day+6)
            user.health -= oHitDamage
def fight():


    opponentHealth = day + 9
    print("--------------------------")
    print("***ENCOUNTERED A ZOMBIE***")
    print("--------------------------\n\n")
    xpEarned = 0
    lastHitChance = 100
    while opponentHealth > 0 and user.health > 0:
        userInput = input("Fight? Use a Bandage or Run? ( F / B / R )\n")
        userInput = userInput.lower().strip()
        if userInput == 'f':

            hitChance = random.randint(1,100) + user.accuracy

            debugVal(hitChance)
            debugVal(lastHitChance)


            # Checks if the last hit chance is below 50, if it is a slight buff is applied.
            if lastHitChance < 50:
                hitChance += 15
            lastHitChance = hitChance
            # Executes a hit
            if hitChance > 50:
                damageDone = random.randint(1,3) + (user.damage / 10)
                critChance = random.randint(1,100) + ((user.accuracy+user.stamina)/8)
                if critChance < 15:
                    damageDone = damageDone * 1.5
                    print("**************************")
                    print("!!!    CRITICAL HIT    !!!")
                    print("**************************")
                    xpEarned += 2
                else:
                    print("**************************")
                    print("!!!        Hit!         !!!")
                    print("**************************")

                opponentHealth -= damageDone
                print("--Zombie was hit for {} HP--\n".format(damageDone))

                xpEarned += 2
                if opponentHealth < 0:
                    print("**************************")
                    print("    Zombie was killed")
                    print("**************************")
                    if random.randint(1, 2) == 2:
                        addItem("Bandage")

                    return
                displayHealth(opponentHealth)

            ### add XP EARNED##


        elif userInput == "b":
            useBandage()
        elif userInput == 's':
            simulateFight()
        else:
            if random.randint(1, 10) > 3:
                print("**** Successfully Escaped ****")
                return

        delay(1)
        oHitChance = random.randint(1,100)
        if opponentHealth > 1:

        # Opponent Hits user
            if oHitChance > 40:
                oHitDamage = random.randint(int(day/2),day+6)
                user.health -= oHitDamage
                print("<<<<<<<<<<<<<>>>>>>>>>>>>>")
                print(f"Zombie hit you for {oHitDamage} HP!")
                print("<<<<<<<<<<<<<>>>>>>>>>>>>>")
            delay(1)
            print(f"You now have {user.health} HP")
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



            if reward > 35:

                print("Found a location to Forage!")
                delay(1)
                location = foundLocation()
                user.knownLocations.append(location)
                delay(1)
                if risk < 20:
                    fight()
                activityLoop = False

            else:
                print("No luck finding a location to forage...")
                delay(1)
                if risk < 5:
                    fight()
                activityLoop = False
        elif choice =="f":
            delay(1)
            if len(user.knownLocations) == 0:
                print("No Known Locations to Forage.\n")
                activityLoop = False
                return
            location = chooseLocation()
            print("Travelling to the {}".format(location))
            delay(2)
            if risk < 30:
                fight()
                if risk < 5:
                    fight()

            if reward > 50:
                foundRandomItem()
            else:
                print("No luck finding any items here..")
            user.knownLocations.remove(location)
            activityLoop = False


        elif choice == "r":


            activityLoop = False

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
    print("Here you will start each of your days. You have the choice to complete 2 activities during your daylight hours.")
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
# Skips setup and begins first day with name test.
def skipSetup():

    return ("Test")

#choose the activity loop.
def chooseTwo():
    for i in range(2):
        if i == 0:
            print("You have 12 hours to complete 2 activities.")
        else:
            print("You have 6 hours to complete 1 activity.")
        choice = chooseActivity()
        doActivity(choice)

#after main loop you can choose to look at items locations or continue.
def postActivity():
    
    ActivityLoop = True
    while ActivityLoop:
        userInput = input("Would you like to see your items, known locations, or continue? ( i, l, c)\n").lower()
        if userInput == "i":
            useItem()
        elif userInput == "l":
            printKnownLocations()
        elif userInput == "c" or "":
            ActivityLoop = False
    delay(1)
    print()
def night(day):
    zombies = day * 2.5
    oHitChance = random.randint(1, 100)

    if oHitChance > 40:
        base.nightDamage = random.randint(int(day/2),day+6)
        base.setHealth(base.health-base.nightDamage)

    if base.health < 0:
        for i in range(zombies):
            simulateFight()
if __name__ == "__main__":
    if debug == True:
        name = skipSetup()
    else:
        name = setupGame()

    day = 1
    user = Character(name, 0, 100, 10, 10, 10, [], {"Bandage": 1}, None)
    if debug == True:
        addItem("Bat")
    base = Base(20,0)
    GameLoop = True
    DayLoop = True

while GameLoop:
    while DayLoop and base.health > 0:

        print("Day ", day)
        print("--------------------------\n")
        print("Good Morning, {}\n".format(user.name))
        delay(1)
        if day > 1:
            print(f"Base sustained {base.nightDamage} HP during the night hours.")
        print("Base Health is", base.health, " HP.")
        delay(1)

        chooseTwo()
        postActivity()
        night(day)

        day += 1








