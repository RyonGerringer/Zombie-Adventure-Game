import random, math, time
import character, items, locations, activities

# This skips the intro scene and gives the player a bat,
# although they have to equip it.

debug = True





class Base:
    def __init__(self, health, nightDamage):
        self.health = health
        self.nightDamage = nightDamage

    def setHealth(self, newHealth):
        self.health = newHealth


#-------------------#
# Display Functions
#-------------------#

def displayHealth(opponentHealth):
    health = int(opponentHealth)
    print("----------HEALTH----------")
    print("  ", (('\U00002665' + " ") * health), (('\U00002661' + " ") * (health - 10)))
    print("---        {}HP        ---".format(opponentHealth))
    print("--------------------------")

    delay(1)
def printStats():
    print("\n\n----------STATS----------")
    print(f"Total Fights: {user.stats.fights}")
    print(f"Total Trapped Fights: {user.stats.trappedFights}\n\n")
    input("Press Enter to continue...")
def printKnownLocations():
    if len(user.knownLocations) == 0:
        print("No known locations.\n")
        return
    print("-----Known Locations:-----")
    for i in user.knownLocations:
        print(i)
    print()
    delay(2)

def chooseLocation():
    num = 1

    # makes the selection Dictionary
    selectDict = {}
    for i in user.knownLocations:
        selectDict[num] = i
        print("[{}] {}".format(num, i))
        num += 1


    choiceNum = int(input("Where would you like to go?\n"))



    return selectDict[choiceNum]
def displayCurrentItems(selectDict):
    print()
    print("--------------------------")
    for i in selectDict:
        item = selectDict[i]
        print(f"[{i}] {item} ({user.items[item]})")
    print("--------------------------")






#-------------------#
# Items Functions
#-------------------#
def foundRandomItem():
    item = random.choice(list(items.items))
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

def useItem():
    num = 1
    choiceNum = 0
    if not user.items:
        print("You have no items to use.\n")
        delay(1)
        return
    delay(1)


    #makes the selection Dictionary
    selectDict = {}
    for item in user.items:


        selectDict[num] = item
        num += 1


    nums = list(selectDict.keys())


    while choiceNum not in nums:
        try:
            displayCurrentItems(selectDict)
            choiceNum = input(f"\nPlease enter {nums} and press enter:\n")
            if choiceNum == "":
                return

            choiceNum = int(choiceNum)

        except:
            inpt = input("Press Enter if you do not want to use an item.\n")
            if inpt == "":
                return
            print("Try again")
    item = selectDict[int(choiceNum)]

    delay(1)
    if item == 'Bandage':
        useBandage()
    elif item in items.weapons:
        oldDamage = user.damage
        if user.weapon != None:
            print("Now Throwing away your {}.\n".format(user.weapon))
            user.damage -= items.weapons[user.weapon]
            user.weapon = None
            delay(1)

        print("\n--------------------------\n"
              "Now using the {} for your weapon.\n".format(item))
        delay(2)
        user.weapon = item
        user.items[item] -= 1
        user.damage = items.weapons[item]
        print(f"You now have {user.damage} Damage, before you had {oldDamage} Damage\n\n")
        delay(1)
    else:
        return
    if user.items[item] == 0:
        user.items.pop(item)

def useBandage():
    bandageCount = user.items["Bandage"]
    if user.health == 100:
        print("You do not need to use a bandage right now...")
        return
    if bandageCount == 0:
        print("No bandages to use.")
        return
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
        user.items["Bandage"] = bandageCount - 1

        if bandageCount == 1:
            user.items.pop("Bandage")







#-------------------#
# Location Functions
#-------------------#
def foundLocation():

    location = random.choice(list(locations.locations.keys()))
    print()
    print("------Location Found------")
    print("         ",location)
    print("--------------------------")
    return location





#-------------------#
# Activities Functions
#-------------------#
def simulateFight():
    opponentHealth = day.count + 9
    xpEarned = 0
    lastHitChance = 100
    while opponentHealth > 0 and user.health > 0:
        hitChance = random.randint(1, 100) + user.accuracy
        oHitChance = random.randint(1, 100)
        # Checks if the last hit chance is below 50, if it is a slight buff is applied.
        if lastHitChance < 50:
            hitChance += 15 * (day.count / 2)
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
                if random.randint(1, 2) == 2:
                    addItem("Bandage")
                return
            displayHealth(opponentHealth)

            ### add XP EARNED##
        if oHitChance > 40:
            oHitDamage = random.randint(int(day.count / 2), day.count + 6)
            user.health -= oHitDamage
def trappedFight():
    user.stats.trappedFights += 1
    opponentHealth = day.count + 9 + random.randint(-4,4)
    print("--------------------------")
    print("***ENCOUNTERED A ZOMBIE***")
    print("--------------------------\n\n")
    print("OH NO ! THIS ZOMBIE HAS YOU TRAPPED\nYOU CANNOT RUN.")
    

    
def fight():
    user.stats.fights += 1
    opponentHealth = day.count + 9 + random.randint(-4,4)
    print("--------------------------")
    print("***ENCOUNTERED A ZOMBIE***")
    print("--------------------------\n\n")
    xpEarned = 0
    lastHitChance = 100
    while opponentHealth > 0 and user.health > 0:
        userInput = input("Fight? Use a Bandage or Run? ( F / B / R )\n")
        userInput = userInput.lower().strip()
        if userInput == 'f':

            hitChance = random.randint(1, 100) + user.accuracy

            debugVal(hitChance)
            debugVal(lastHitChance)

            # Checks if the last hit chance is below 50, if it is a slight buff is applied.
            if lastHitChance < 50:
                hitChance += 15
            lastHitChance = hitChance
            # Executes a hit
            if hitChance > 50:
                damageDone = random.randint(1, 3) + (user.damage / 10)
                critChance = random.randint(1, 100) + ((user.accuracy + user.stamina) / 8)
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
                if opponentHealth <= 0:
                    delay(1)
                    print("**************************")
                    print("    Zombie was killed")
                    print("**************************")
                    if random.randint(1, 2) == 2:
                        addItem("Bandage")
                    delay(1)

                    inpt = ''
                    while inpt not in ["y","n"]:
                        inpt = input("Would you like to use a bandage? y/n?")

                        if inpt == "y":
                            useBandage()
                        elif inpt == "n":
                            pass








                    return
                displayHealth(opponentHealth)
            else:
                print("\n\n\nYou Missed!\n\n\n")
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
        oHitChance = random.randint(1, 100)
        if opponentHealth > 0:
            # Opponent Hits user
            if oHitChance > 40:
                oHitDamage = random.randint(int(day.count / 2), day.count + 6)
                user.health -= oHitDamage
                print("<<<<<<<<<<<<<>>>>>>>>>>>>>")
                print(f"Zombie hit you for {oHitDamage} HP!")
                print("<<<<<<<<<<<<<>>>>>>>>>>>>>")
            delay(1)
            print(f"You now have {user.health} HP")
    print()
def chooseActivity():

    if day.count == 1:
        choice = input("\n\nWould you like to Scout, Forage, or Repair? S / F / R\nType S, F or R and press enter\n Hint: Choose scout to begin.\n").lower()
    else:
        choice = input("\n\nWould you like to Scout, Forage, or Repair? S / F / R\n").lower()

    print()
    return choice
def doActivity(choice):
    activityLoop = True

    reward = random.randint(1, 100)
    risk = random.randint(1, 100)
    if choice == "s":

        print("Scouting nearby areas for materials...")
        delay(3)

        # make decision
        debugVal(reward)
        if reward > 35:

            print("Found a location to Forage!")
            delay(1)
            location = foundLocation()
            user.knownLocations.append(location)
            delay(1)
            if risk < 5:
                trappedFight()
            elif risk < 20 or debug:
                fight()
            

            return True

        else:
            print("No luck finding a location to forage...")
            delay(1)
            if risk < 5:
                fight()

            return True
    elif choice == "f":
        delay(1)
        if len(user.knownLocations) == 0:
            print("No Known Locations to Forage.\n")
            return False


        location = chooseLocation()
        print("Travelling to the {}".format(location))
        delay(2)
        if risk < 30:
            fight()
            if risk < 5 * (day.count / 2):
                fight()

        if reward > 50:
            foundRandomItem()
        else:
            print("No luck finding any items here..")
        user.knownLocations.remove(location)

        return True


    elif choice == "r":


        return True

    else:

        return False
        pass
# choose the activity loop.
def chooseTwo():

    while day.hour > 0:
        
        if day.hour == 12:
            print("You have 12 hours to complete 2 activities.")
        else:
            print("You have 6 hours to complete 1 activity.")
        
        choice = chooseActivity()
        activity = doActivity(choice)
        if activity:
            day.setHour(day.hour - 6)
        



# after main loop you can choose to look at items locations or continue.
def postActivity():
    ActivityLoop = True
    while ActivityLoop:
        userInput = input("Would you like to see your items, known locations, see your stats, or press enter to continue? ( i, l, s)\n").lower()
        if userInput == "i":
            useItem()
        elif userInput == "l":
            printKnownLocations()
        elif userInput == "s":
            printStats()
        elif userInput == "":
            ActivityLoop = False
    delay(1)
    print()



#-------------------#
# Main Game Functions
#-------------------#

def delay(d):
    time.sleep(d)
def debugVal(value):
    if debug == True:
        print("- # debug -# {} #-".format(value))
# Sets up the game with name and instructions on how to play.


def printIntro(line):
    intro = {1:"Welcome to\n",
            2:"*********************************",
            3:"*********************************\n",
            4:"__________            ___.   .__ ",
            5:"\____    /____   _____\_ |__ |__|",
            6:"  /     //  _ \ /     \| __ \|  |",
            7:" /  ___/(  <_> )  Y Y  \ \_\ \  |",
            8:"/_______ \____/|__|_|  /___  /__|",
            9:"        \/           \/    \/    \n",
            10:"*********************************",
            11:"*********************************\n\n\n\n",}
    
    print(intro[line])
def setupGame():
    if debug:
        skipSetup()
    
    
    
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
    delay(2)
    print("The names is R for Ryon.\n\n")
    delay(3)


    
    print("--------------------------\n")
    print("Day 0")
    print("--------------------------")
    print("Good Morning, {}\n".format(name))
    print("\nBase Health is 20  HP.\nYou have 12 hours to complete 2 activities.\nWould you like to Scout, Forage, or Repair? S / F / R\n")
    print("\nThis is where you will choose how you spend your day, you will start by scouting areas to forage.\n")
    delay(3)
    print("Once you start venturing out and being active, the undead will start to attack.\n")
    delay(3.5)
    print("At night the undead will begin to attack the base, you better hope you have good materials and stats.\n")
    input("Press Enter to continue...")
    delay(.5)

    
    print(
        "Here you will start each of your days. You have the choice to complete 2 activities during your daylight hours.")
    delay(3)
    print("These choices will impact your day to day experience as well as defending the base from zombies at night.\n\n")
    delay(3)
    print("Try to survive the longest that you can!\n")
    delay(3)
    print("Game starting...")
    delay(3)
    print("Get ready!\n\n")
    delay(1)
    input("Press Enter to continue...")
    user = character.Character(name, 0, 100, 10, 10, 10, [], {"Bandage": 1})
    return user


# Skips setup and begins first day with name test.
def skipSetup():
    user = character.Character("Test", 0, 100, 10, 10, 10, [], {"Bandage": 3})

    return user


def night(day):
    for i in range(10):
        print()
        delay(.5)
    zombies = day.count * 2.5
    oHitChance = random.randint(1, 100)

    if oHitChance > 40:
        base.nightDamage = random.randint(int(math.floor(day.count / 4)), math.floor(day.count + 2))
        base.setHealth(base.health - base.nightDamage)

    if base.health < 0:
        for i in range(zombies):
            simulateFight()



if __name__ == "__main__":
        class Day:
            def __init__(self, count, hour):
                self.count = count
                self.hour = hour

            def setCount(self, count):
                self.count = count

            def setHour(self, hour):
                self.hour = hour
        if debug == True:
            user = skipSetup()
        else:
            user = setupGame()



        if debug == True:
                addItem("Bat")
                addItem("Bandage")
        base = Base(20, 0)
        GameLoop = True
        DayLoop = True
        day = Day(1, 12)

while GameLoop:



    while DayLoop and base.health > 0:
        day.setHour(12)
        print("--------------------------\n")
        print("Day ", day.count)
        print("--------------------------")
        print("Good Morning, {}\n".format(user.name))
        delay(1)
        if day.count > 1:
            print(f"Base sustained {base.nightDamage} HP during the night hours.")
            delay(1)
        print("Base Health is", base.health, " HP.")
        delay(1)

        chooseTwo()
        delay(2)
        postActivity()

        night(day)

        day.setCount(day.count + 1)
