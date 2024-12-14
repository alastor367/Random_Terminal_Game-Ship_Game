#im not nativ speaker i dont used translator this is why english is bad in this code :)
#this version of codes was make for be as easy to red as poisble && and to be easy to make
#not to be as fast as posible (they will be more version of this code in python and other progrtaming launge ) (maybe i hate my self becouse of this code)
#i know you can make big code comends but i dont like using that 

#this code is programing war crime

#v2
#more levels - done
#enemy better si - 
#amunition system - 50%
#hp system -
#player shield system - 


#as far ik you dont need to instal aditcional pacpage to use this imports
import os #for clear console
import platform #for check system info
import time #for sleep
import random #for random numbers

#change only var where coments says you cna change you cna change where coments dont say that but you do it on your own risk and for own fun not all var alre made for customization
safe_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
list = safe_list.copy()
list2 = safe_list.copy()
list3 = safe_list.copy()
list4 = safe_list.copy()
#-------------
#ik i can automate that one but no i will not automate that one maybe i will autmate that one when i will add cosutomization suport for this code maybe i will :(
spritepos = ["   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   "] #i need tor enemy position
enemysprite = ["  /-\\  ", "<| O |>", "  \-/  ", "  /-\\  ", "<| X |>", "  \-/  ", "  /-\\  ", "<|   |>", "  \-/  "]#first 3 full hp mid 3 half hp last 3 one hp
enemyhpnormalmax = 3 #hp for enemy on normal mode
curentenemyhp = enemyhpnormalmax #hp for enemy (code will change hp on max after dificulty selection) code only suports number taht can be divene by 3
enemypos = 8 #map mid maybe mid smt like that enemy is 3 haracter long
enemycupo = enemypos # curent enemy position
failcheck1 = ["1", "2", "3"] #check for avalibe characters this is for dificulty important
ListNumber = ""
ListLetter = ""
idk = False
move = "Player" #Player or Enemy
aniamtion_is_playing = False #to handling animations
dificulty = 1
oldenemypos = enemypos
############"|                |"
lastaction ="|                |"
lastaction2 ="|                |"
amunition = 70 #normal 70
el = 3
er = ""
playermaxhp = 100
playerhp = 100
playermaxshield = 10 #first why i cannot make // coments in python second this is for the hard and above dificulty (i hate pong symbol idk if this is caled # pong) and i will not make ahk scrypt for changing // to #
playermaxshield5 = 5
playershield = 5
enemyamunition = 200 # he he i still want to make coments with // :(
enemyshieldhp = 5

#you cannot change that one 
enemymovN = { #N = normal dificulty numbers for procentes
    "Fire": 20,
    "Heal": 5,
    "Nothing": 80
}


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

def idsk(): #for random loot form destroing letters
    global playerhp
    global playershield
    global lastaction2
    global amunition
    if dificulty == 2:
        randomef = {
            "hel": 10,
            "not": 60,
            "amo": 15,
            "shi": 10
        }
    else:
        randomef = {
            "i": 1
        }
    nah = [] #var for moves
    for text, percent in randomef.items(): #magic :) this shuld makes a long list
        nah.extend([text]*percent)
        endchoice = random.choice(nah) #randomize what enemy will do from long list (for any dificulty above normal this will be dont in other way)
    if endchoice == "not":
        lastaction2 ="|                |"
        pass
    elif endchoice == "hel":
        if playerhp >= playermaxhp:
            lastaction2 ="|You res shield  |"
            playershield += 1
        else:
            #lastaction ="|Atacked Enemy   |"
            lastaction2 ="|You res hp      |"
            playerhp += random.randint(1,5)
    elif endchoice == "amo":
        amunition += random.randint(1,2)
    elif endchoice == "shi":
        playershield += 1


def main_menu():
    while True:
        cls()
        print("Ship Game")
        print("")
        print("1.Play")
        print("2.Options")
        print("3.Exit")
        playl = ["1","PLAY","PILAY"]
        optl = ["2","OPTIONS","OPTLONS"]
        exitl = ["3","EXIT", "EXLT"]
        option = str(input("> "))
        if option.upper() in playl:
            Play()
            break
        elif option.upper() in optl:
            print("Options menu is comming soon")
            time.sleep(0.75)
        elif option.upper() in exitl:
            exit()


def Play():
    global enemyhpnormalmax
    global curentenemyhp
    global dificulty
    global amunition
    global playershield
    global enemy75p
    global enemy50p
    global playerhp
    global enemyamunition
    global enemyshieldhp
    while True:
        cls()
        print("Select your difuculty")
        print("1.Easy")
        print("2.Normal")
        try:
            dificulty = int(input("> "))
            if dificulty == 1:
                amunition = 100000 #in easy mode amunition is inf code dont count amunition at all
                enemyhpnormalmax = 3 #max enymy hp
                curentenemyhp = enemyhpnormalmax #set enemi hp to max at game start
                playershield = playermaxshield5
                playerhp = 100
                break
            elif dificulty == 2:
                amunition = 70
                enemyhpnormalmax = 12
                curentenemyhp = enemyhpnormalmax
                playershield = playermaxshield5
                playerhp = playermaxhp
                enemyamunition = 200
                enemyshieldhp = 1
                break
            else:
                cls() #nah
                print("This need to be a existing dificulty number")
                time.sleep(0.75) #i like this number i also like 3 dont ask why i like 3 or why im teling in coment i like 3 i just like that number :)
        except ValueError as ve:
            print("This need to be an number")
    enemy75p = int((enemyhpnormalmax/3)*2)-1
    enemy50p = int(enemyhpnormalmax/2)-1
    maingamelogic()
#print("3.Hard")
#print("4.Hard+")
#print("5.Imposible")


enemy75p = int((enemyhpnormalmax/3)*2)-1
enemy50p = int(enemyhpnormalmax/2)-1

def resetthefspriteforenemy():
    global spritepos
    #i will add/or i added suport for custom ones
    spritepos = ["   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   "]

def ResetToBasic():
    #load evry var to global that allows for modyfaing var as global in entire code
    global list
    global list2
    global list3
    global list4
    global spritepos
    global enemyhpnormalmax
    global curentenemyhp
    global enemypos
    global enemycupo
    global ListNumber
    global ListLetter
    global idk
    global move
    global aniamtion_is_playing
    global oldenemypos
    global lastaction
    global playerhp
    #reset evrything to def value
    list = safe_list.copy()
    list2 = safe_list.copy()
    list3 = safe_list.copy()
    list4 = safe_list.copy()
    spritepos = ["   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   "]
    enemyhpnormalmax = 3 #hp for enemy on normal mode
    curentenemyhp = 3 #hp for enemy (code will change hp on max after dificulty selection) code only suports number taht can be divene by 3
    enemypos = 8 #map mid maybe mid smt like that enemy is 3 haracter long
    enemycupo = enemypos # curent enemy position
    ListNumber = ""
    ListLetter = ""
    idk = False
    move = "Player"
    aniamtion_is_playing = False
    oldenemypos = enemypos
    lastaction ="|                |"
    playerhp = playermaxhp
    main_menu()

def maingamelogic():
    global el
    global er
    global idk #load varable intro global in def funcion that allows for modyfaing var as global in entire code
    global move
    global enemycupo
    global curentenemyhp
    global aniamtion_is_playing
    global lastaction
    global amunition
    global enemyshieldhp
    global playerhp
    global playershield
    if dificulty == 1 or dificulty == 2:
        try:
            global idk #load varable intro global in def funcion that allows for modyfaing var as global in entire code
            global move
            global enemycupo
            global curentenemyhp
            global aniamtion_is_playing
            global lastaction
            global amunition
            global enemyshieldhp
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
                        elif ListNumber == "5" and dificulty == 2:
                            idk = True
                            ListN = 5
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
                                    if dificulty >= 2:
                                        amunition -= 1
                                        idsk()
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
                                    if dificulty >= 2:
                                        amunition -= 1
                                        idsk()
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
                                    if dificulty >= 2:
                                        amunition -= 1
                                        idsk()
                                    break
                                else: #if smt is in wrong input let player type againt we talk about if player typed a in lev 1 when a in level 1 is destroyed already
                                    idk = False
                                    move = "Player"
                                    break
                            elif ListN == 4:
                                if dificulty == 1:
                                    if ListLetter.upper() in safe_list and ListLetter.upper() not in list3: #logic for enemy demage ;-;
                                        number = safe_list.index(ListLetter.upper())
                                        if number == enemycupo or number == (enemycupo+1) or number == (enemycupo+2):
                                            curentenemyhp -=1
                                            lastaction ="|Atacked Enemy   |"
                                            move = "Enemy"
                                            if dificulty >= 2:
                                                amunition -= 1
                                                idsk()
                                            if curentenemyhp == 0:
                                                er = "enemy ded"
                                                raise Exception("Enemy ded")
                                        move = "Enemy"
                                        break
                                    else: #the same but player can miss when enymi isnt in range
                                        idk = False
                                        move = "Player"
                                        break
                                elif dificulty == 2:
                                    if ListLetter.upper() in list4 and ListLetter.upper() not in list3: #check if leter is in list and if is isnt in the list before 
                                        index = list4.index(str(ListLetter.upper()))
                                        list4[index] = " "
                                        move = "Enemy"
                                        if dificulty >= 2:
                                            amunition -= 1
                                            idsk()
                                        break
                                    else: #if smt is in wrong input let player type againt we talk about if player typed a in lev 1 when a in level 1 is destroyed already
                                        idk = False
                                        move = "Player"
                                        break
                            elif ListN == 5:
                                if ListLetter.upper() in safe_list and ListLetter.upper() not in list4: #logic for enemy demage ;-;
                                        number = safe_list.index(ListLetter.upper())
                                        if number == enemycupo or number == (enemycupo+1) or number == (enemycupo+2):
                                            if enemyshieldhp > 0:
                                                enemyshieldhp -= 1
                                            else:
                                                curentenemyhp -=1
                                            lastaction ="|Atacked Enemy   |"
                                            move = "Enemy"
                                            if dificulty >= 2:
                                                amunition -= 1
                                            if curentenemyhp == 0:
                                                er = "Enemy ded"
                                                raise Exception("Enemy ded")
                                        move = "Enemy"
                                        break
                                else: #the same but player can miss when enymi isnt in range
                                    idk = False
                                    move = "Player"
                                    break
                        else:
                            pass
                    idk = False
                    while True:
                        if move == "Enemy": #when enemy turn ENEMY CANT SHOT ON NORMAL MODE
                            if curentenemyhp > enemy75p:
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
                            elif curentenemyhp > enemy50p:
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
                            elif curentenemyhp > 1:
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
                        #--------------------------------------------------
                        #-------------------enemy things to do-------------
                        #--------------------------------------------------
                        if move == "Enemy":
                            if amunition > 0 and dificulty >= 2:
                                nah = [] #var for moves
                                for text, percent in enemymovN.items(): #magic :) this shuld makes a long list
                                    nah.extend([text]*percent)
                                endchoice = random.choice(nah) #randomize what enemy will do from long list (for any dificulty above normal this will be dont in other way)
                                #"Fire": x,"Heal": x,"Nothing": x  x=precents + names all this are write in enemymovN
                                if endchoice == "Fire":
                                    #lastaction ="|Atacked Enemy   |" i need that to make lastaction
                                    lastaction ="|Enemy Atacked   |"
                                    if playershield > 0:
                                        playershield -= random.randint(1,2)#randomzie shield dmg
                                    else:
                                        playerhp -= random.randint(1,8) #randomize dmg
                                        if playerhp < 1:
                                            er = "hp down"
                                            raise Exception("hp down")
                                    #here will be animation handler i will do that in the futere
                                elif endchoice == "Heal":
                                    if curentenemyhp == enemyhpnormalmax:
                                        lastaction ="|Enemy res shield|"
                                        enemyshieldhp += 1
                                    else:
                                        lastaction ="|Enemy healed    |" #idk how to say that
                                        howmuch = random.randint(1,3) #randomize how much heal fell free to modify
                                        curentenemyhp += howmuch
                                elif endchoice == "Nothing":
                                    lastaction ="|                |"
                                    pass #what did you encepted ;-; pass = skip this thing im trying not to swear in coments ok?
                        move = "Player"
                        break
                elif aniamtion_is_playing == True:
                    pass
                if amunition <= 0:
                    er = "Ammo out"
                    raise Exception("Ammo out")
        except Exception as e:
            if er == "Ammo out":
                el = 0 #0 lose 1 win
                errormes = "Because you have no more ammo" #mesage after W or L 
            elif er == "Enemy ded":
                el = 1
                errormes = "You defeated the \"enemy\"" #enemy will be replaced witch var to name enemy
            elif er == "hp down":
                el = 0
                errormes = "Because you died" #no more to explain ecplain idk i just idk
            while True:
                cls()
                if el == 1:
                    print("You Win")
                elif el == 0:
                    print("You Lost")
                    print(errormes)
                print("Wanna go to the menu? (Type yes or no or number)")
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
    else:
        print(";-;")

def ship(): #game board dont make sens ik
    global ListNumber
    global ListLetter
    if dificulty == 1:
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
        print("|                                                                                    ", list[6] , list2[6] , list3[6] , spritepos[6] ,safe_list[6],f"|Enemy hp: {curentenemyhp:<6}|")#f  string allow for less spaces in code + more control over formating
        print("|                                                                                    ", list[7] , list2[7] , list3[7] , spritepos[7] ,safe_list[7],"|Enemy am: 0     |")#am = amunition
        print("|                                                                                    ", list[8] , list2[8] , list3[8] , spritepos[8] ,safe_list[8],"|Shield hp: 0    |")
        print("|                                                                                    ", list[9] , list2[9] , list3[9] , spritepos[9] ,safe_list[9],"|----------------|")
        print("|                                                                                    ", list[10], list2[10], list3[10], spritepos[10] ,safe_list[10],lastaction)
        print("|                                                                                    ", list[11], list2[11], list3[11], spritepos[11] ,safe_list[11],"|________________|")
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
        # dont make sense
        if move == "Player":
            if idk == False:
                ListNumber = str(input("Select a level: "))
            else:
                ListLetter = str(input("Select a letter: "))
    elif dificulty == 2:
        if amunition > 999:
            amutext = 999
        else:
            amutext = amunition
        cls()
        #ps i used in this one f formating becouse i just get bored witch using scrol bar to see smt ;-;
        #f"|{blank:<82}" evry f foramting have {} where you put var and you can put some thinkgs i put :<82 that means var needs to be min 82 characters long i didnt specifay with what character
        #that means formating will fill print var with blank spaces
        blank = ""
        #####("----------------------------------------------------------------------------------------")-just leve this 
        print("|                                                                                  |1|2|3|4|Enemy[5]| |  Information   |")
        print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|-=-=-=-|=-=-=-=-| |=-=-=-=-=-=-=-=-|")
        print(f"|{blank:<82}", list[0] , list2[0] , list3[0] ,list4[0] , spritepos[0] ,safe_list[0],f"|Gamemode: Normal|")#16 characters
        print(f"|{blank:<82}", list[1] , list2[1] , list3[1] ,list4[1] , spritepos[1] ,safe_list[1],f"|----------------|")
        print(f"|{blank:<82}", list[2] , list2[2] , list3[2] ,list4[2] , spritepos[2] ,safe_list[2],f"|Your hp: {playerhp:<7}|") 
        print(f"|{blank:<82}", list[3] , list2[3] , list3[3] ,list4[3] , spritepos[3] ,safe_list[3],f"|Your amo: {amutext:<6}|")#am = amunition + f string allow for less spaces in code + more control over formating
        print(f"|{blank:<82}", list[4] , list2[4] , list3[4] ,list4[4] , spritepos[4] ,safe_list[4],f"|Shield hp: {playershield:<5}|")
        print(f"|{blank:<82}", list[5] , list2[5] , list3[5] ,list4[5] , spritepos[5] ,safe_list[5],f"|----------------|")
        print(f"|{blank:<82}", list[6] , list2[6] , list3[6] ,list4[6] , spritepos[6] ,safe_list[6],f"|Enemy hp: {curentenemyhp:<6}|")
        print(f"|{blank:<82}", list[7] , list2[7] , list3[7] ,list4[7] , spritepos[7] ,safe_list[7],f"|Enemy am: {enemyamunition:<6}|")#am = amunition
        print(f"|{blank:<82}", list[8] , list2[8] , list3[8] ,list4[8] , spritepos[8] ,safe_list[8],f"|Shield hp: {enemyshieldhp:<5}|")
        print(f"|{blank:<82}", list[9] , list2[9] , list3[9] ,list4[9] , spritepos[9] ,safe_list[9],"|----------------|")
        print(f"|{blank:<82}", list[10], list2[10], list3[10], list4[10], spritepos[10] ,safe_list[10],lastaction)
        print(f"|{blank:<82}", list[11], list2[11], list3[11], list4[11], spritepos[11] ,safe_list[11],lastaction2)
        print(f"|{blank:<82}", list[12], list2[12], list3[12], list4[12], spritepos[12] ,safe_list[12],"|________________|")
        print(f"|{blank:<82}", list[13], list2[13], list3[13], list4[13], spritepos[13] ,safe_list[13])
        print(f"|{blank:<82}", list[14], list2[14], list3[14], list4[14], spritepos[14] ,safe_list[14])
        print(f"|{blank:<82}", list[15], list2[15], list3[15], list4[15], spritepos[15] ,safe_list[15])
        print(f"|{blank:<82}", list[16], list2[16], list3[16], list4[16], spritepos[16] ,safe_list[16])
        print(f"|{blank:<82}", list[17], list2[17], list3[17], list4[17], spritepos[17] ,safe_list[17])
        print(f"|{blank:<82}", list[18], list2[18], list3[18], list4[18], spritepos[18] ,safe_list[18])
        print("|                          )___(                                                   ", list[19], list2[19], list3[19], list4[19], spritepos[19] ,safe_list[19])
        print("|                    _______\__\_                                                  ", list[20], list2[20], list3[20], list4[20], spritepos[20] ,safe_list[20])
        print("|              ___   |===========\     ___                                         ", list[21], list2[21], list3[21], list4[21], spritepos[21] ,safe_list[21])
        print("|        __   [///]__|____________\___[\\\\\]    __       ____                       ", list[22], list2[22], list3[22], list3[22], spritepos[22] ,safe_list[22])
        print("|     __[//]__/                            \__[//]_____/   /                       ", list[23], list2[23], list3[23], list4[23], spritepos[23] ,safe_list[23])
        print("|    |                                                    /                        ", list[24], list2[24], list3[24], list4[24], spritepos[24] ,safe_list[24])
        print("|     \__________________________________________________/                         ", list[25], list2[25], list3[25], list4[25], spritepos[25] ,safe_list[25])
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~","/=================\\")
        # dont make sense
        if move == "Player":
            if idk == False:
                ListNumber = str(input("Select a level: "))
            else:
                ListLetter = str(input("Select a letter: "))

main_menu()