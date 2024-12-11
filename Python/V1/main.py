#im not nativ speaker i dont used translator this is why english is bad in this code :)
#this version of codes was make for be as easy to red as poisble && and to be easy to make
#not to be as fast as posible (they will be more version of this code in python and other progrtaming launge ) (maybe i hate my self becouse of this code)
#i know you can make big code comends but i dont like using that 

import os #for clear console
import platform #for check system info
import time #for sleep
import random #for random numbers

safe_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
list2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
list3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#-------------
#ik i can automate that one but no i will not automate that one maybe i will autmate that one when i will add cosutomization suport for this code maybe i will :(
spritepos = ["   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   "] #i need tor enemy position
enemysprite = ["  /-\\  ", "<| O |>", "  \-/  ", "  /-\\  ", "<| X |>", "  \-/  ", "  /-\\  ", "<|   |>", "  \-/  "]#first 3 full hp mid 3 half hp last 3 one hp
enemyhpnormalmax = 3 #hp for enemy on normal mode
curentenemyhp = 3 #hp for enemy (code will change hp on max after dificulty selection) code only suports number taht can be divene by 3
enemypos = 8 #map mid maybe mid smt like that enemy is 3 haracter long
enemycupo = enemypos # curent enemy position
failcheck1 = ["1", "2", "3"] #check for avalibe characters this is for dificulty important
ListNumber = ""
ListLetter = ""
idk = False
move = "Player" #Player or Enemy
aniamtion_is_playing = False #to handling animations

#select dificulty option difiulty selection is blocked at this moment
print("Select your difuculty")
print("1.Easy")
print("2.Normal")
#print("3.Hard")
#print("4.Hard+")
#print("5.Imposible")

#terminal tytle
try:
    os.system("title " + "Ship-Game")
except Exception as e:
    pass

#clear terminal
def cls():
    debugingtime = 0 #for debuging this disable cls funcion
    if debugingtime != 1:
        system_name = platform.system() #system info
        if system_name == "Windows": #if windows use cls
            os.system("cls")
        else: #if linux use clear
            try:
                os.system("clear")
            except Exception as e:
                print("Error while cls function")

def resetthefspriteforenemy():
    global spritepos
    spritepos = ["   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   "]

def ResetToBasic():
    #load evry var to global that allows for modyfaing var as global in entire code
    global safe_list
    global list
    global list2
    global list3
    global spritepos
    global enemyhpnormalmax
    global curentenemyhp
    global enemypos
    global enemycupo
    global failcheck1
    global ListNumber
    global ListLetter
    global idk
    global move
    global aniamtion_is_playing
    #reset evrything to def value
    safe_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] #for new game
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] #lev 1 alfabet
    list2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] #lev 2 alfabet
    list3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] #lev 3 alfabet
    spritepos = ["   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   "]
    enemyhpnormalmax = 3 #hp for enemy on normal mode
    curentenemyhp = 3 #hp for enemy (code will change hp on max after dificulty selection) code only suports number taht can be divene by 3
    enemypos = 5 #map mid maybe mid smt like that enemy is 3 haracter long
    enemycupo = enemypos # curent enemy position
    failcheck1 = ["1", "2", "3", "4"]
    ListNumber = ""
    ListLetter = ""
    idk = False
    move = "Player"
    aniamtion_is_playing = False
    maingamelogic()
def maingamelogic():
    try:
        global idk #load varable intro global in def funcion that allows for modyfaing var as global in entire code
        global move
        global enemycupo
        global curentenemyhp
        global aniamtion_is_playing
        #ennemy data load before start
        index = enemycupo
        spritepos[index] = enemysprite[0]
        index += 1
        spritepos[index] = enemysprite[1]
        index += 1
        spritepos[index] = enemysprite[2]
        while True: # game loop
            ship()
            if aniamtion_is_playing == False:
                while True: #make a loop for checking some things
                    if ListNumber in failcheck1: #check if listnumber is in failcheck list
                        idk = True
                        ListN = int(ListNumber) #convert listnumber intro number for listn
                        break
                    elif ListNumber == "4":
                        idk = True
                        ListN = 4
                        break
                    else:
                        cls()
                        print("This needs to be a level number")
                        time.sleep(0.75) #time out for pgram to have some break ;-;
                        ship()
                
                while True: #loop for idk just loop for smt
                    cls()
                    ship()
                    if move == "Player":
                        if ListN == 1:
                            # .upper() make for code letter a as A that allow for user to dont need for type capital letter
                            if ListLetter.upper() in list: # check if leter is in list
                                index = list.index(str(ListLetter.upper()))
                                list[index] = " "
                                move = "Enemy"
                                break
                            else: #if smt is in wrong input let player type againt we talk about if player typed a in lev 1 when a in level 1 is destroyed already
                                idk = False
                                move = "Player"
                                break
                        elif ListN == 2:
                            if ListLetter.upper() in list2 and ListLetter.upper() not in list: #check if leter is in list and if is isnt in the list before 
                                index = list2.index(str(ListLetter.upper()))
                                list2[index] = " "
                                move = "Enemy"
                                break
                            else: #if smt is in wrong input let player type againt we talk about if player typed a in lev 1 when a in level 1 is destroyed already
                                idk = False
                                move = "Player"
                                break
                        elif ListN == 3:
                            if ListLetter.upper() in list3 and ListLetter.upper() not in list2: #check if leter is in list and if is isnt in the list before 
                                index = list3.index(str(ListLetter.upper()))
                                list3[index] = " "
                                move = "Enemy"
                                break
                            else: #if smt is in wrong input let player type againt we talk about if player typed a in lev 1 when a in level 1 is destroyed already
                                idk = False
                                move = "Player"
                                break
                        elif ListN == 4:
                            if ListLetter.upper() in safe_list and ListLetter.upper() not in list3: #logic for enemy demage ;-;
                                number = safe_list.index(ListLetter.upper())
                                if number == enemycupo:
                                    curentenemyhp -= 1
                                    if curentenemyhp == 0:
                                        raise Exception("END ALL LOPS")
                                if number == (enemycupo+1):
                                    curentenemyhp -= 1
                                    if curentenemyhp == 0:
                                        raise Exception("END ALL LOPS")
                                if number == (enemycupo+2):
                                    curentenemyhp -= 1
                                    if curentenemyhp == 0:
                                        raise Exception("END ALL LOPS")
                                move = "Enemy"
                                break
                            else: #the same but player can miss when enymi isnt in range
                                idk = False
                                move = "Player"
                                break
                    else:
                        pass
                idk = False
                if aniamtion_is_playing == False:
                    while move == "Enemy":
                        if move == "Enemy": #when enemy turn ENEMY CANT SHOT ON NORMAL MODE
                            if curentenemyhp == enemyhpnormalmax:
                                if enemycupo == 0:#bro 0 is the up enemy shuldn't go up
                                    randomdirection = 2 #set direction to down
                                elif (enemycupo-2) < 0: #when enemy curent position - how many steps if < 0 then force to go down
                                    randomdirection = 2
                                elif (enemycupo+4) > 25: #when enemy curent position + 2 height + how many steps is mor ethat 25 force to go up
                                    randomdirection = 1 #to do: swtch this to 2 steps 
                                else:
                                    randomdirection = random.randint(1,2) #1 for up 2 for down in this state only 2 step at the time
                                if randomdirection == 1: #to understand hy look at def ship(): and on spritepos[]
                                    #i use index var becouse i like it
                                    posenemy = enemycupo-2 #this is hanlding how many steps in state he can take
                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want 
                                    #time to clearn enemy old sprite
                                    resetthefspriteforenemy()
                                    #time to draw enemy sprite
                                    index = posenemy
                                    spritepos[index] = enemysprite[0]
                                    index += 1
                                    spritepos[index] = enemysprite[1]
                                    index += 1
                                    spritepos[index] = enemysprite[2]
                                elif randomdirection == 2:
                                    #i use index var becouse i like it
                                    posenemy = enemycupo+2 #this is hanlding how many steps in state he can take
                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want 
                                    #time to clearn enemy old sprite
                                    resetthefspriteforenemy()
                                    #time to draw enemy sprite
                                    index = posenemy
                                    spritepos[index] = enemysprite[0]
                                    index += 1
                                    spritepos[index] = enemysprite[1]
                                    index += 1
                                    spritepos[index] = enemysprite[2]
                            elif curentenemyhp == ((enemyhpnormalmax/3)*2):
                                if enemycupo == 0:#bro 0 is the up enemy shuldn't go up
                                    randomdirection = 2 #set direction to down
                                elif (enemycupo-3) < 0: #when enemy curent position - how many steps if < 0 then force to go down
                                    randomdirection = 2
                                elif (enemycupo+5) == 25: #when enemy curent position + 2 height + how many steps is mor ethat 25 force to go up
                                    randomdirection = 1 #to do: swtch this to 2 steps 
                                else:
                                    randomdirection = random.randint(1,2) #1 for up 2 for down in this state only 3 step at the time
                                if randomdirection == 1: #to understand hy look at def ship(): and on spritepos[]
                                    #i use index var becouse i like it
                                    posenemy = enemycupo-3 #this is hanlding how many steps in state he can take
                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want 
                                    #time to clearn enemy old sprite
                                    resetthefspriteforenemy()
                                    #time to draw enemy sprite
                                    index = posenemy
                                    spritepos[index] = enemysprite[3]
                                    index += 1
                                    spritepos[index] = enemysprite[4]
                                    index += 1
                                    spritepos[index] = enemysprite[5]
                                elif randomdirection == 2:
                                    #i use index var becouse i like it
                                    posenemy = enemycupo+3 #this is hanlding how many steps in state he can take
                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want 
                                    #time to clearn enemy old sprite
                                    resetthefspriteforenemy()
                                    #time to draw enemy sprite
                                    index = posenemy
                                    spritepos[index] = enemysprite[3]
                                    index += 1
                                    spritepos[index] = enemysprite[4]
                                    index += 1
                                    spritepos[index] = enemysprite[5]
                            elif curentenemyhp == (enemyhpnormalmax/3):
                                if enemycupo == 0:#bro 0 is the up enemy shuldn't go up
                                    randomdirection = 2 #set direction to down
                                elif (enemycupo-4) < 0: #when enemy curent position - how many steps if < 0 then force to go down
                                    randomdirection = 2
                                elif (enemycupo+6) > 25: #when enemy curent position + 2 height + how many steps is mor ethat 25 force to go up
                                    randomdirection = 1 #to do: swtch this to 2 steps 
                                else:
                                    randomdirection = random.randint(1,2) #1 for up 2 for down in this state only 4 step at the time
                                if randomdirection == 1: #to understand hy look at def ship(): and on spritepos[]
                                    #i use index var becouse i like it
                                    posenemy = enemycupo-4 #this is hanlding how many steps in state he can take
                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want 
                                    #time to clearn enemy old sprite
                                    resetthefspriteforenemy()
                                    #time to draw enemy sprite
                                    index = posenemy
                                    spritepos[index] = enemysprite[6]
                                    index += 1
                                    spritepos[index] = enemysprite[7]
                                    index += 1
                                    spritepos[index] = enemysprite[8]
                                elif randomdirection == 2:
                                    #i use index var becouse i like it
                                    posenemy = enemycupo+4 #this is hanlding how many steps in state he can take
                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want 
                                    #time to clearn enemy old sprite
                                    resetthefspriteforenemy()
                                    #time to draw enemy sprite
                                    index = posenemy
                                    spritepos[index] = enemysprite[6]
                                    index += 1
                                    spritepos[index] = enemysprite[7]
                                    index += 1
                                    spritepos[index] = enemysprite[8]
                        else: 
                            move = "Player"
                        move = "Player"
                else:
                    pass
            elif aniamtion_is_playing == True:
                pass
    except Exception as e:
        while True:
            cls()
            print("Wanna play again? (Type yes or no or number)")
            print("1.Yes")
            print("2.No")
            gameoverevit = str(input("> "))
            if gameoverevit.upper() == "YES":
                ResetToBasic()
                break
            elif gameoverevit.upper() == "NO":
                exit()
            elif gameoverevit.upper() == "N0":
                exit()
            elif gameoverevit.upper() == "1":
                ResetToBasic()
                break
            elif gameoverevit.upper() == "2":
                exit()
            else:
                print("Random Error try again")
                time.sleep(0.75)

def ship(): #game board dont make sens ik
    if aniamtion_is_playing == True:
        pass
    else:
        cls()
        #####("----------------------------------------------------------------------------------------")-just leve this 
        print("|                                                                                    |1|2|3|Enemy[4]| |  Information   |")
        print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|-=-=-|=-=-=-=-| |=-=-=-=-=-=-=-=-|")
        print("|                                                                                    ", list[0] , list2[0] , list3[0] , spritepos[0] ,safe_list[0],"|Gamemode: Easy  |")
        print("|                                                                                    ", list[1] , list2[1] , list3[1] , spritepos[1] ,safe_list[1],"|----------------|")
        print("|                                                                                    ", list[2] , list2[2] , list3[2] , spritepos[2] ,safe_list[2],"|Your hp:  inf   |") 
        print("|                                                                                    ", list[3] , list2[3] , list3[3] , spritepos[3] ,safe_list[3],"|Your amo: inf   |")#am = amunition
        print("|                                                                                    ", list[4] , list2[4] , list3[4] , spritepos[4] ,safe_list[4],"|Shield hp: 0    |")
        print("|                                                                                    ", list[5] , list2[5] , list3[5] , spritepos[5] ,safe_list[5],"|----------------|")
        print("|                                                                                    ", list[6] , list2[6] , list3[6] , spritepos[6] ,safe_list[6],"|Enemy hp:",curentenemyhp,"    |")
        print("|                                                                                    ", list[7] , list2[7] , list3[7] , spritepos[7] ,safe_list[7],"|Enemy am: 0     |")#am = amunition
        print("|                                                                                    ", list[8] , list2[8] , list3[8] , spritepos[8] ,safe_list[8],"|Shield hp: 0    |")
        print("|                                                                                    ", list[9] , list2[9] , list3[9] , spritepos[9] ,safe_list[9],"|----------------|")
        print("|                                                                                    ", list[10], list2[10], list3[10], spritepos[10] ,safe_list[10])
        print("|                                                                                    ", list[11], list2[11], list3[11], spritepos[11] ,safe_list[11])
        print("|                                                                                    ", list[12], list2[12], list3[12], spritepos[12] ,safe_list[12])
        print("|                                                                                    ", list[13], list2[13], list3[13], spritepos[13] ,safe_list[13])
        print("|                                                                                    ", list[14], list2[14], list3[14], spritepos[14] ,safe_list[14])
        print("|                                                                                    ", list[15], list2[15], list3[15], spritepos[15] ,safe_list[15])
        print("|                                                                                    ", list[16], list2[16], list3[16], spritepos[16] ,safe_list[16])
        print("|                                                                                    ", list[17], list2[17], list3[17], spritepos[17] ,safe_list[17])
        print("|                                                                                    ", list[18], list2[18], list3[18], spritepos[18] ,safe_list[18])
        print("|                          )___(                                                     ", list[19], list2[19], list3[19], spritepos[19] ,safe_list[19])
        print("|                    _______\__\_                                                    ", list[20], list2[20], list3[20], spritepos[20] ,safe_list[20])
        print("|              ___   |===========\     ___                                           ", list[21], list2[21], list3[21], spritepos[21] ,safe_list[21])
        print("|        __   [///]__|____________\___[\\\\\]    __       ____                         ", list[22], list2[22], list3[22], spritepos[22] ,safe_list[22])
        print("|     __[//]__/                            \__[//]_____/   /                         ", list[23], list2[23], list3[23], spritepos[23] ,safe_list[23])
        print("|    |                                                    /                          ", list[24], list2[24], list3[24], spritepos[24] ,safe_list[24])
        print("|     \__________________________________________________/                           ", list[25], list2[25], list3[25], spritepos[25] ,safe_list[25])
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~","/===============\\")
        global ListNumber
        global ListLetter
        # dont make sense
        if move == "Player":
            if idk == False:
                ListNumber = str(input("Select a level: "))
            else:
                ListLetter = str(input("Select a letter: "))

maingamelogic()