#im not nativ speaker i dont used translator this is why english is bad in this code :)
#this version of codes was make for be as easy to red as poisble && and to be easy to make
#not to be as fast as posible (they will be more version of this code in python and other progrtaming launge ) (maybe i hate my self becouse of this code)
#i know you can make big code comends but i dont like using that 

#this code is programing war crime

# 00111011 00101101 00111011  00111010 00101001
#more levels - done
#enemy better si - only for hard and above
#amunition system - let say done
#hp system - yes sir
#player shield system - yes sir 


#as far ik you dont need to instal aditcional pacpage to use this imports
import os #for clear console
import platform #for check system info
import time #for sleep
import random #for random numbers
#if smt from imports isnt being used in code that means i will use this in the furtere i will nto delet that import from code that import will be in code to moment when i will use this

#change only var where coments says you cna change you cna change where coments dont say that but you do it on your own risk and for own fun not all var alre made for customization
safe_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
enemylist = ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "D", "D", "D", "D", "D", "D"]#aditionad "D" for fail safe
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
lastaction ="║                ║"
lastaction2 ="║                ║"
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
first_time = True #if player start game it will be true you cna change that to false
enemy_simple_brain_for_hard_end_my_sufering_pls = 0

#options
animation_speed_letter_d = 0.35
boat_name = "   "

#if you want to change numbers are some way %
enemymovN = { #N = normal dificulty numbers for procentes
    "Fire": 20,
    "Heal": 5,
    "Nothing": 80
}
enemymovH = { #N = normal dificulty numbers for procentes
    "Fire": 25,
    "Heal": 10,
    "Nothing": 60
}
enemymovHplus = {
    "Fire": 35,
    "Heal": 10,
    "Nothing": 50
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
            try: #if cls funciotn fails there will be error
                os.system("cls")
            except Exception as e:
                print("Error while cls function 'cls")
        else: #if linux use clear
            try:
                os.system("clear")
            except Exception as e:
                print("Error while cls function 'clearn'")

def idsk(): #for random loot form destroing letters
    global playerhp
    global playershield
    global lastaction2
    global amunition
    if dificulty == 2:
        randomef = {
            "hel": 15,
            "not": 60,
            "amo": 15,
            "shi": 10
        }
    elif dificulty == 3:
        randomef = {
            "hel": 8,
            "not": 55,
            "amo": 13,
            "shi": 8
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
        lastaction2 ="║                ║"
        pass
    elif endchoice == "hel":
        if playerhp >= playermaxhp:
            lastaction2 ="║You res shield  ║"
            playershield += 1
        else:
            #lastaction ="║Atacked Enemy   ║"
            lastaction2 ="║You res hp      ║"
            playerhp += random.randint(1,5)
    elif endchoice == "amo":
        amunition += random.randint(1,2)
    elif endchoice == "shi":
        playershield += 1


def main_menu():
    while True:
        cls()
        #╔║═╚╗╝.center(120) .rjust(118//2) i use that 
        a = "" #old one i dont want to delete this
        print("╔════════════════════╗".center(120))
        print("║ Terminal Ship Game ║".center(120)) #print centered text
        print("╚════════════════════╝".center(120))
        print("\n") #\n is just enter if you want another blank line add \n if you dont want blank line delete this print()
        print("╔════════════╗".center(120))
        print("║   1.Play   ║".center(120))
        print("║ 2.Options  ║".center(120))
        print("║ 3.Tutorial ║".center(120))
        print("║   0.Exit   ║".center(120))
        print("╚════════════╝".center(120))
        playl = ["1","1.","PLAY","PILAY"]
        optl = ["2","2.","OPTIONS","OPTLONS","OPTION","OPTLON"]
        tuto = ["3","3.", "TUTORIALS", "TUTORIAIS", "TUTORLAI","TUTORIAL"]
        exitl = ["0","0.","EXIT", "EXLT"]
        print("")
        option = str(input("> ".rjust(118//2)))
        if option.upper() in playl:
            Play()
            break
        elif option.upper() in optl:
            options()
            break
        elif option.upper() in tuto:
            print("comming soon")
            time.sleep(0.75)
        elif option.upper() in exitl:
            exit()
        else:
            print("Wrong input Try again")
            time.sleep(0.75)

def options():
    global animation_speed_letter_d, boat_name
    while True:
        cls()
        #╔║═╚╗╝.center(120) .rjust(118//2) i use that 
        print("╔═════════╗".center(120))
        print("║ Options ║".center(120)) #print centered text
        print("╚═════════╝".center(120))
        print("")
        print("╔═══════════════════════════════╗".center(120))
        print("║   1.Change animations speed   ║".center(120))
        print("║   2.Ship Name                 ║".center(120))
        print("║   0.Back                      ║".center(120))
        print("╚═══════════════════════════════╝".center(120))
        option = str(input("> ".rjust(118//2)))
        back = ["0","0.","BACK"]
        if option.upper() in back:
            main_menu()
            break
        elif option.upper() == "1":
            cls()
            print("╔══════════════════╗".center(120))
            print("║ Animations Speed ║".center(120)) #print centered text
            print("╚══════════════════╝".center(120))
            print("")
            print("╔═══════════════════════════════╗".center(120))
            print("║   1.Letters destroy speed     ║".center(120))
            print("║   0.Back                      ║".center(120))
            print("╚═══════════════════════════════╝".center(120))
            option = str(input("> ".rjust(118//2)))
            back = ["0","0.","BACK"]
            if option.upper() in back:
                options()
                break
            elif option.upper() == "1":
                while True:
                    try:
                        cls()
                        print("")
                        print("Type new letter animation speed normal = 1 you can type 0.X or X.X X is your number".center(120))
                        print("")
                        animspe = float(input("> ".rjust(118//2)))
                        if animspe == 1 or animspe == 1.0:
                            animation_speed_letter_d = 0.35
                        else:
                            animation_speed_letter_d = 0.35*animspe
                        options()
                        break
                    except ValueError:
                        print("This need to be float number ;-;".center(120))
                        time.sleep(0.75)
                        options()
                        break
        elif option.upper() == "2":
            while True:
                cls()
                print("")
                print("You can type any name for your Ship on the ship will be only dispaly 3 first characters".center(120))
                print("")
                boat_name = input("> ".rjust(118//2))
                options()
                break
        break


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
        #╔║═╚╗╝.center(120) .rjust(118//2) i use that 
        print("╔═════════════════════╗".center(120))
        print("║Select your difuculty║".center(120))
        print("╚═════════════════════╝".center(120))
        print("\n")#\n is just enter if you want another blank line add \n if you dont want blank line delete this print()
        print("╔════════════╗".center(120))
        print("║   1.Easy   ║".center(120))
        print("║  2.Normal  ║".center(120))
        print("║   3.Hard   ║".center(120))
        print("║   0.Back   ║".center(120))
        print("╚════════════╝".center(120))
        dif1 = ["1","1.","EASY","1.EASY"]
        dif2 = ["2","2.","NORMAL","NORMAI","2.NORMAL","2.NORMAI"]
        dif3 = ["3","3.","HARD","3.HARD"]
        back = ["0","0.","BACK"]
        try:
            print("")
            dificultyt = str(input("> ".rjust(118//2)))
            if dificultyt.upper() in dif1:
                dificulty = 1
                amunition = 100000 #in easy mode amunition is inf code dont count amunition at all
                enemyhpnormalmax = 3 #max enymy hp
                curentenemyhp = enemyhpnormalmax #set enemi hp to max at game start
                playershield = playermaxshield5
                playerhp = 100
                break
            elif dificultyt.upper() in back:
                main_menu()
                break
            elif dificultyt.upper() in dif2:
                dificulty = 2
                amunition = 70
                enemyhpnormalmax = 12
                curentenemyhp = enemyhpnormalmax
                playershield = playermaxshield5
                playerhp = playermaxhp
                enemyamunition = 200
                enemyshieldhp = 1
                break
            elif dificultyt.upper() in dif3:
                dificulty = 3
                amunition = 60
                enemyhpnormalmax = 18
                curentenemyhp = enemyhpnormalmax
                playershield = 2
                playerhp = int(playermaxhp*0.9)
                enemyamunition = 250
                enemyshieldhp = 5
                break
            else:
                cls() #nah
                #╔║═╚╗╝.center(120) .rjust(118//2) i use that 
                print("This need to be a existing dificulty number")
                time.sleep(0.75) #i like this number i also like 3 dont ask why i like 3 or why im teling in coment i like 3 i just like that number :)
        except ValueError as ve: #old code don't use this i will remake this and yes i used ' ;-;
            print("This need to be an number")
    enemy75p = int((enemyhpnormalmax/3)*2)-1
    enemy50p = int(enemyhpnormalmax/2)-1
    maingamelogic()
#print("3.Hard")
#print("4.Hard+")
#print("5.Imposible")


enemy75p = int((enemyhpnormalmax/3)*2)-1
enemy50p = int(enemyhpnormalmax/2)-1

def enemyhardsi(a, b):
    Elist = []
    # Check for index depends on enemy movement
    for i in range(enemycupo - 2, enemycupo + 5):
        if i < 0:
            Elist.append("D")  # Forced "D" if list is below 0
        elif 0 <= i < len(enemylist):  # Check for potential error
            if enemylist[i] == "S" or enemylist[i] == "D":
                Elist.append(enemylist[i])  # Only append "S" or "D"
    return Elist

def enmyhardplussi():
    Elist = []
    # Check for index depends on enemy movement
    for i in range(0, 25):
        if i < 0:
            Elist.append("D")  # Forced "D" if list is below 0
        elif 0 <= i < len(enemylist):  # Check for potential error
            if enemylist[i] == "S" or enemylist[i] == "D":
                Elist.append(enemylist[i])  # Only append "S" or "D"
    return Elist

def restore():
    Rlist = []
    for i in range(0, len(list4)):
        if 0 <= i < len(list4):
            #make fucnion to remember where is " "
            Rlist = []
    return Rlist


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
    global first_time
    global enemylist
    #reset evrything to def value
    enemylist = ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "D", "D", "D", "D", "D", "D"]
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
    lastaction ="║                ║"
    playerhp = playermaxhp
    first_time = True
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
    global enemyamunition
    global enemylist
    global enemy_simple_brain_for_hard_end_my_sufering_pls
    if dificulty > 0 and dificulty < 6:
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
                        elif ListNumber == "5" and dificulty >= 2:
                            idk = True
                            ListN = 5
                            break
                        else:
                            cls()
                            print("\n\n")
                            #╔║═╚╗╝.center(120) .rjust(118//2) i use that 
                            print("╔════════════════════════════════╗".center(120))
                            print("║This needs to be a level number.║".center(120))
                            print("╚════════════════════════════════╝".center(120))
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
                                    old = list[index]
                                    #animaino handler
                                    aniamtion_is_playing = True
                                    list[index] = " "
                                    ship()
                                    time.sleep(animation_speed_letter_d)
                                    cls()
                                    list[index] = old
                                    ship()
                                    time.sleep(animation_speed_letter_d)
                                    cls()
                                    list[index] = " "
                                    aniamtion_is_playing = False
                                    #end of animation handler
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
                                    old = list2[index]
                                    #animaino handler
                                    aniamtion_is_playing = True
                                    list2[index] = " "
                                    ship()
                                    time.sleep(animation_speed_letter_d)
                                    cls()
                                    list2[index] = old
                                    ship()
                                    time.sleep(animation_speed_letter_d)
                                    cls()
                                    list2[index] = " "
                                    aniamtion_is_playing = False
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
                                    old = list3[index]
                                    #animaino handler
                                    aniamtion_is_playing = True
                                    list3[index] = " "
                                    ship()
                                    time.sleep(animation_speed_letter_d)
                                    cls()
                                    list3[index] = old
                                    ship()
                                    time.sleep(animation_speed_letter_d)
                                    cls()
                                    list3[index] = " "
                                    aniamtion_is_playing = False
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
                                            lastaction ="║Atacked Enemy   ║"
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
                                elif dificulty >= 2 and dificulty < 6:
                                    if ListLetter.upper() in list4 and ListLetter.upper() not in list3: #check if leter is in list and if is isnt in the list before 
                                        index = list4.index(str(ListLetter.upper()))
                                        old = list4[index]
                                        #animaino handler
                                        aniamtion_is_playing = True
                                        list4[index] = " "
                                        ship()
                                        time.sleep(animation_speed_letter_d)
                                        cls()
                                        list4[index] = old
                                        ship()
                                        time.sleep(animation_speed_letter_d)
                                        cls()
                                        list4[index] = " "
                                        aniamtion_is_playing = False
                                        move = "Enemy"
                                        if dificulty >= 2:
                                            amunition -= 1
                                            enemylist[index] = "D"
                                            idsk()
                                        break
                                    else: #if smt is in wrong input let player type againt we talk about if player typed a in lev 1 when a in level 1 is destroyed already
                                        idk = False
                                        move = "Player"
                                        break
                            elif ListN == 5:
                                if ListLetter.upper() in safe_list and ListLetter.upper() not in list4: #logic for enemy demage ;-;
                                        number = safe_list.index(ListLetter.upper())
                                        if dificulty >= 2:
                                            amunition -= 1
                                        if number == enemycupo or number == (enemycupo+1) or number == (enemycupo+2):
                                            if enemyshieldhp > 0:
                                                enemyshieldhp -= 1
                                            else:
                                                curentenemyhp -=1
                                            lastaction ="║Atacked Enemy   ║"
                                            move = "Enemy"
                                            
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

                    #--------------------------------------------------
                    #
                    #ENEMY MOVES HANDLER ITS BAD BUT WORKS
                    #
                    #--------------------------------------------------

                    while True:
                        if dificulty <= 2:
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
                                        #lastaction ="║Atacked Enemy   ║" i need that to make lastaction
                                        lastaction ="║Enemy Atacked   ║"
                                        if playershield >= 1:
                                            playershield -= random.randint(1,2)#randomzie shield dmg
                                        else:
                                            playerhp -= random.randint(1,8) #randomize dmg
                                            playershield = 0
                                            if playerhp < 1:
                                                er = "hp down"
                                                raise Exception("hp down")
                                        #here will be animation handler i will do that in the futere
                                    elif endchoice == "Heal":
                                        if curentenemyhp == enemyhpnormalmax:
                                            lastaction ="║Enemy res shield║"
                                            enemyshieldhp += 1
                                        else:
                                            lastaction ="║Enemy healed    ║" #idk how to say that
                                            howmuch = random.randint(1,3) #randomize how much heal fell free to modify
                                            curentenemyhp += howmuch
                                    elif endchoice == "Nothing":
                                        lastaction ="║                ║"
                                        pass #what did you encepted ;-; pass = skip this thing im trying not to swear in coments ok?
                            move = "Player"
                            break
                        else:
                            #----------------------------------------------------
                            #
                            #ENEMY HANLDER FOR DIFCULTY ABOVE 2
                            #
                            #----------------------------------------------------
                            if move == "Enemy": #when enemy turn ENEMY CANT SHOT ON NORMAL MODE
                                if curentenemyhp > enemy75p: #enemy75p p stands for % 75 this number stand of hp 75% of hp
                                    #math to check if can move
                                    if enemycupo == 0 or enemycupo == 1:#bro 0 is the up enemy shuldn't go up
                                        randomdirection = 2 #set direction to down
                                    elif (enemycupo-2) < 0: #when enemy curent position - how many steps if < 0 then force to go down
                                        randomdirection = 2
                                    elif (enemycupo+4) > 25: #when enemy curent position + 2 height + how many steps is mor ethat 25 force to go up
                                        randomdirection = 1 #to do: swtch this to 2 steps 
                                    else:
                                        safepointup = 0
                                        safepointDo = 0
                                        if enemy_simple_brain_for_hard_end_my_sufering_pls >4:
                                            enemy_simple_brain_for_hard_end_my_sufering_pls = 0
                                        Elist = enemyhardsi(2,4)
                                        if Elist[0] == "S":
                                            safepointup += 1
                                        if Elist[1] == "S":
                                            safepointup += 1
                                        if Elist[2] == "S":
                                            safepointup += 1
                                        if Elist[3] == "S":
                                            safepointup += 1
                                            safepointDo += 1
                                        if Elist[6] == "S":
                                            safepointDo += 1
                                        if Elist[5] == "S":
                                            safepointDo += 1
                                        if Elist[4] == "S":
                                            safepointDo += 1
                                        if safepointup > safepointDo and enemy_simple_brain_for_hard_end_my_sufering_pls <5:
                                            randomdirection = 1
                                        elif safepointDo > safepointup and enemy_simple_brain_for_hard_end_my_sufering_pls <5:
                                            randomdirection = 2
                                        else:
                                            randomdirection = random.randint(1,2)
                                    #move logic
                                    if randomdirection == 1: #to understand hy look at def ship(): and on spritepos[]
                                        #i use index var becouse i like it
                                        Elist = enemyhardsi(2,4)# call the enemy si funcion to get list for enemy what to see hard+ will see in range to max 6up 8 down on hard: 2 up 4 down 4 becouse 2 on body 2 on down one part of body is implemented in funcion
                                        #for Elist enemy body is 3,4,5 in index
                                        if Elist[0] == "S" and Elist[1] == "S" and Elist[2] == "S":
                                            posenemy = enemycupo-2 #this is hanlding how many steps in state he can take
                                            enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                        elif Elist[0] == "D" and Elist[1] == "S" and Elist[2] == "S" and Elist[3] == "S":
                                            posenemy = enemycupo-1 #this is hanlding how many steps in state he can take
                                            enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                        else:
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
                                        Elist = enemyhardsi(2,4)
                                        if Elist[6] == "S" and Elist[5] == "S" and Elist[4] == "S":
                                            posenemy = enemycupo+2 #this is hanlding how many steps in state he can take
                                            enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                        elif Elist[6] == "D" and Elist[5] == "S" and Elist[4] == "S" and Elist[3] == "S":
                                            posenemy = enemycupo+1 #this is hanlding how many steps in state he can take
                                            enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                        else:
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
                            #
                            #
                            #
                            #--------------------------------------------------
                            #-------------------enemy things to do-------------
                            #--------------------------------------------------
                            #
                            #
                            #
                            if move == "Enemy":
                                if amunition > 0 and dificulty >= 2:
                                    nah = [] #var for moves
                                    for text, percent in enemymovH.items(): #magic :) this shuld makes a long list
                                        nah.extend([text]*percent)
                                    endchoice = random.choice(nah) #randomize what enemy will do from long list (for any dificulty above normal this will be dont in other way)
                                    #"Fire": x,"Heal": x,"Nothing": x  x=precents + names all this are write in enemymovN
                                    if endchoice == "Fire":
                                        if enemyamunition > 0:
                                            #lastaction ="║Atacked Enemy   ║" i need that to make lastaction
                                            lastaction ="║Enemy Atacked   ║"
                                            if playershield >= 1:
                                                playershield -= random.randint(1,2)#randomzie shield dmg
                                            else:
                                                playerhp -= random.randint(1,8) #randomize dmg
                                                playershield = 0 #force shield to be always 0
                                                if playerhp < 1:
                                                    er = "hp down"
                                                    raise Exception("hp down")
                                            #here will be animation handler i will do that in the futere
                                        else:
                                            pass
                                    elif endchoice == "Heal":
                                        if curentenemyhp == enemyhpnormalmax:
                                            lastaction ="║Enemy res shield║"
                                            enemyshieldhp += 1
                                        else:
                                            lastaction ="║Enemy healed    ║" #idk how to say that
                                            howmuch = random.randint(1,3) #randomize how much heal fell free to modify
                                            curentenemyhp += howmuch
                                    elif endchoice == "Nothing":
                                        lastaction ="║                ║"
                                        pass #what did you encepted ;-; pass = skip this thing im trying not to swear in coments ok?
                            move = "Player"
                            break
                elif aniamtion_is_playing == True:
                    pass
                if amunition <= 0:
                    er = "Ammo out"
                    raise Exception("Ammo out")
        except Exception as e:
            errormesd = ""
            erormesu = ""
            print(e)
            if er == "Ammo out":
                el = 0 #0 lose 1 win
                erormesu = "╔═════════════════════════════╗"
                errormes = "║Because you have no more ammo║" #mesage after W or L
                errormesd= "╚═════════════════════════════╝"
            elif er == "Enemy ded":
                el = 1
                erormesu = "╔═════════════════════════════╗"
                errormes = "║ You defeated the \"enemy\". ║" #enemy will be replaced witch var to name enemy
                errormesd= "╚═════════════════════════════╝"
            elif er == "hp down":
                el = 0
                erormesu = "╔═════════════════════════════╗"
                errormes = "║      Because you died.      ║" #no more to explain ecplain idk i just idk
                errormesd= "╚═════════════════════════════╝"
            
            #/-----\ /=====================================\ /-----\
            #|     | |                                     | |     |
            #| ;-; | |ask player if exit or go back to menu| | ;-; |
            #|     | |                                     | |     |
            #\-----/ \=====================================/ \-----/
            while True:
                cls()
                #╔║═╚╗╝.center(120) .rjust(118//2) i use that 
                if el == 1:
                    print("╔════════╗".center(120))
                    print("║You Win ║".center(120))
                    print("╚════════╝".center(120))
                elif el == 0:
                    print("╔════════╗".center(120))
                    print("║You Lost║".center(120))
                    print("╚════════╝".center(120))
                    print(erormesu.center(120))
                    print(errormes.center(120))
                    print(errormesd.center(120))
                    print("")
                print("╔═════════════════════╗".center(120))
                print("║Wanna go to the menu?║".center(120))
                print("╚═════════════════════╝".center(120))
                print("")
                print("╔═══════════╗".center(120))
                print("║   1.Yes   ║".center(120))
                print("║   2.No    ║".center(120))
                print("╚═══════════╝".center(120))
                print("")
                print(e) # for debuging info delete after previev
                gameoverevit = str(input("> ".rjust(118//2)))
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
        #{boat_name[:3]:<3} in f formating makes only 3 first letters visible and :<3 min character need to be 3 else fill witch blank you cna delte the :<3 and see waht hapends
        #╔║═╚╗╝╩.center(120) .rjust(118//2) i use that 
        cls()#levels 120 in cmd windows basic 10 line
        #####("----------------------------------------------------------------------------------------")-just leve this 
        print(f"║                                                                          ║ levels: ║1|2|3║Enemy[4]║ ║  Information   ║")
        print(f"╠══════════════════════════════════════════════════════════════════════════╩═════════╩═════╩════════╝ ╠════════════════╣")
        print(f"║                                                                                    ", list[0] , list2[0] , list3[0] , spritepos[0] ,safe_list[0],"║Gamemode: Easy  ║")
        print(f"║                                                                                    ", list[1] , list2[1] , list3[1] , spritepos[1] ,safe_list[1],"╟----------------╢")
        print(f"║                                                                                    ", list[2] , list2[2] , list3[2] , spritepos[2] ,safe_list[2],"║Your hp:  inf   ║") 
        print(f"║                                                                                    ", list[3] , list2[3] , list3[3] , spritepos[3] ,safe_list[3],"║Your amo: inf   ║")#am = amunition
        print(f"║                                                                                    ", list[4] , list2[4] , list3[4] , spritepos[4] ,safe_list[4],"║Shield hp: 0    ║")
        print(f"║                                                                                    ", list[5] , list2[5] , list3[5] , spritepos[5] ,safe_list[5],"╟----------------╢")
        print(f"║                                                                                    ", list[6] , list2[6] , list3[6] , spritepos[6] ,safe_list[6],f"║Enemy hp: {curentenemyhp:<6}║")#f  string allow for less spaces in code + more control over formating
        print(f"║                                                                                    ", list[7] , list2[7] , list3[7] , spritepos[7] ,safe_list[7],"║Enemy amo: 0    ║")#am = amunition
        print(f"║                                                                                    ", list[8] , list2[8] , list3[8] , spritepos[8] ,safe_list[8],"║Shield hp: 0    ║")
        print(f"║                                                                                    ", list[9] , list2[9] , list3[9] , spritepos[9] ,safe_list[9],"╟----------------╢")
        print(f"║                                                                                    ", list[10], list2[10], list3[10], spritepos[10] ,safe_list[10],lastaction)
        print(f"║                                                                                    ", list[11], list2[11], list3[11], spritepos[11] ,safe_list[11],"╚════════════════╝")
        print(f"║                                                                                    ", list[12], list2[12], list3[12], spritepos[12] ,safe_list[12])
        print(f"║                                                                                    ", list[13], list2[13], list3[13], spritepos[13] ,safe_list[13])
        print(f"║                                                                                    ", list[14], list2[14], list3[14], spritepos[14] ,safe_list[14])
        print(f"║                                                                                    ", list[15], list2[15], list3[15], spritepos[15] ,safe_list[15])
        print(f"║                                                                                    ", list[16], list2[16], list3[16], spritepos[16] ,safe_list[16])
        print(f"║                                                                                    ", list[17], list2[17], list3[17], spritepos[17] ,safe_list[17])
        print(f"║                                                                                    ", list[18], list2[18], list3[18], spritepos[18] ,safe_list[18])
        print(f"║                          )___(                                                     ", list[19], list2[19], list3[19], spritepos[19] ,safe_list[19])
        print(f"║                    _______\__\_                                                    ", list[20], list2[20], list3[20], spritepos[20] ,safe_list[20])
        print(f"║              ___   |===========\     ___                                           ", list[21], list2[21], list3[21], spritepos[21] ,safe_list[21])
        print(f"║        __   [///]__|____________\___[\\\\\]    __       ____                         ", list[22], list2[22], list3[22], spritepos[22] ,safe_list[22])
        print(f"║     __[//]__/                            \__[//]_____/   /                         ", list[23], list2[23], list3[23], spritepos[23] ,safe_list[23])
        print(f"║    |{boat_name[:3]:<3}                                                 /                          ", list[24], list2[24], list3[24], spritepos[24] ,safe_list[24])
        print(f"║     \__________________________________________________/                           ", list[25], list2[25], list3[25], spritepos[25] ,safe_list[25])
        print(f"╚~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~","/═══════════════\\")
        # dont make sense
        if aniamtion_is_playing == False:
            if move == "Player":
                if idk == False:
                    ListNumber = str(input("Select a level: "))
                else:
                    ListLetter = str(input("Select a letter: "))
    elif dificulty >= 2 and dificulty <= 4: # 2 normal 3 hard 4 hard+ 5imposible 6custom
        if amunition > 999:
            amutext = 999
        else:
            amutext = amunition
        cls()
        #ps i used in this one f formating becouse i just get bored witch using scrol bar to see smt ;-;
        #f"|{blank:<82}" evry f foramting have {} where you put var and you can put some thinkgs i put :<82 that means var needs to be min 82 characters long i didnt specifay with what character
        #i deleted the f formating iwtch 82 ;-;
        #that means formating will fill print var with blank spaces
        #####("----------------------------------------------------------------------------------------")-just leve this 
        #╔║═╚╗╝╩.center(120) .rjust(118//2) i use that 
        dificultytex = ""
        if dificulty == 2:
            dificultytex = "Normal"
        elif dificulty == 3:
            dificultytex = "Hard"
        print(f"║                                                                        ║ levels: ║1║2║3║4║Enemy[5]║ ║  Information   ║")
        print(f"╠════════════════════════════════════════════════════════════════════════╩═════════╩═╩═╩═╩═╩════════╝ ╠════════════════╣")
        print(f"║                                                                                  ", list[0] , list2[0] , list3[0] ,list4[0] , spritepos[0] ,safe_list[0],f"║Gamemode: {dificultytex:<6}║")#16 characters
        print(f"║                                                                                  ", list[1] , list2[1] , list3[1] ,list4[1] , spritepos[1] ,safe_list[1],f"╟----------------╢")
        print(f"║                                                                                  ", list[2] , list2[2] , list3[2] ,list4[2] , spritepos[2] ,safe_list[2],f"║Your hp: {playerhp:<7}║") 
        print(f"║                                                                                  ", list[3] , list2[3] , list3[3] ,list4[3] , spritepos[3] ,safe_list[3],f"║Your amo: {amutext:<6}║")#am = amunition + f string allow for less spaces in code + more control over formating
        print(f"║                                                                                  ", list[4] , list2[4] , list3[4] ,list4[4] , spritepos[4] ,safe_list[4],f"║Shield hp: {playershield:<5}║")
        print(f"║                                                                                  ", list[5] , list2[5] , list3[5] ,list4[5] , spritepos[5] ,safe_list[5],f"╟----------------╢")
        print(f"║                                                                                  ", list[6] , list2[6] , list3[6] ,list4[6] , spritepos[6] ,safe_list[6],f"║Enemy hp: {curentenemyhp:<6}║")
        print(f"║                                                                                  ", list[7] , list2[7] , list3[7] ,list4[7] , spritepos[7] ,safe_list[7],f"║Enemy amo: {enemyamunition:<5}║")#am = amunition
        print(f"║                                                                                  ", list[8] , list2[8] , list3[8] ,list4[8] , spritepos[8] ,safe_list[8],f"║Shield hp: {enemyshieldhp:<5}║")
        print(f"║                                                                                  ", list[9] , list2[9] , list3[9] ,list4[9] , spritepos[9] ,safe_list[9],"╟----------------╢")
        print(f"║                                                                                  ", list[10], list2[10], list3[10], list4[10], spritepos[10] ,safe_list[10],lastaction)
        print(f"║                                                                                  ", list[11], list2[11], list3[11], list4[11], spritepos[11] ,safe_list[11],lastaction2)
        print(f"║                                                                                  ", list[12], list2[12], list3[12], list4[12], spritepos[12] ,safe_list[12],"╚════════════════╝")
        print(f"║                                                                                  ", list[13], list2[13], list3[13], list4[13], spritepos[13] ,safe_list[13])
        print(f"║                                                                                  ", list[14], list2[14], list3[14], list4[14], spritepos[14] ,safe_list[14])
        print(f"║                                                                                  ", list[15], list2[15], list3[15], list4[15], spritepos[15] ,safe_list[15])
        print(f"║                                                                                  ", list[16], list2[16], list3[16], list4[16], spritepos[16] ,safe_list[16])
        print(f"║                                                                                  ", list[17], list2[17], list3[17], list4[17], spritepos[17] ,safe_list[17])
        print(f"║                                                                                  ", list[18], list2[18], list3[18], list4[18], spritepos[18] ,safe_list[18])
        print(f"║                          )___(                                                   ", list[19], list2[19], list3[19], list4[19], spritepos[19] ,safe_list[19])
        print(f"║                    _______\__\_                                                  ", list[20], list2[20], list3[20], list4[20], spritepos[20] ,safe_list[20])
        print(f"║              ___   |===========\     ___                                         ", list[21], list2[21], list3[21], list4[21], spritepos[21] ,safe_list[21])
        print(f"║        __   [///]__|____________\___[\\\\\]    __       ____                       ", list[22], list2[22], list3[22], list3[22], spritepos[22] ,safe_list[22])
        print(f"║     __[//]__/                            \__[//]_____/   /                       ", list[23], list2[23], list3[23], list4[23], spritepos[23] ,safe_list[23])
        print(f"║    |{boat_name[:3]:<3}                                                 /                        ", list[24], list2[24], list3[24], list4[24], spritepos[24] ,safe_list[24])
        print(f"║     \__________________________________________________/                         ", list[25], list2[25], list3[25], list4[25], spritepos[25] ,safe_list[25])
        print(f"╚~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~","/═════════════════\\")
        # dont make sense
        if aniamtion_is_playing == False:
            if move == "Player":
                if idk == False:
                    ListNumber = str(input("Select a level: "))
                else:
                    ListLetter = str(input("Select a letter: "))

main_menu()