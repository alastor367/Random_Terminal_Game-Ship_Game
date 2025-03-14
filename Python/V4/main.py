#for your information code uses many var becouse i want it to be modular or smt like that 

# 00111011 00101101 00111011  00111010 00101001

#as far ik you dont need to instal aditcional pacpage to use this imports
import os #for clear console determing console/system
import platform #for check system info
import time #for sleep
import random #for random numbers
import traceback #more error info

#change only var where coments says you cna change you cna change where coments dont say that but you do it on your own risk and for own fun not all var alre made for customization
safe_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#enemylist = ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "D", "D", "D", "D", "D", "D","D","D","D","D","D","D"]#aditionad "D" for fail safe
enemylist = []
safe_dec = "S"
unsafe_dec = "D"

for j in range(26):
    enemylist.append(safe_dec)
for y in range(12):
    enemylist.append(unsafe_dec)

#i hate this
list = safe_list.copy()
list2 = safe_list.copy()
list3 = safe_list.copy()
list4 = safe_list.copy()

spritepos = []
#spritepos = ["   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   ", "   -   "] #i need tor enemy position
for i in range(26): #26 alfabeth characters in safe_list there is 26(25)
    spritepos.append("   -   ") #you can customize this pls follow order of 7 character in this

enemysprite = ["  /-\\  ", "<| O |>", "  \-/  ", "  /-\\  ", "<| X |>", "  \-/  ", "  /-\\  ", "<|   |>", "  \-/  "]#first 3 full hp mid 3 half hp last 3 one hp
enemyhpnormalmax = 3 #hp for enemy on normal mode
curentenemyhp = enemyhpnormalmax #hp for enemy (code will change hp on max after dificulty selection) code only suports number taht can be divene by 3
enemypos = 8 #map mid maybe mid smt like that enemy is 3 haracter long
enemycupo = enemypos # curent enemy position
failcheck1 = ["1", "2", "3"] #fun fact this is chacking for level if you dont try to attack lev6 but 4 and 5 dont work in list ;-;
ListNumber = ""
ListLetter = ""
idk = False
move = "Player" #Player or Enemy
aniamtion_is_playing = False #to handling animations
dificulty = 1
oldenemypos = enemypos

amunition = 70 #normal 70
el = 3 #0 lose 1 win it just difine if win or not
er = "" # when win or lose game is genereting right error to throw errors constaint is win or not that how game knows
playermaxhp = 100 #;-;
playerhp = 100 #;-;
playermaxshield = 10 #first why i cannot make // coments in python second this is for the hard and above dificulty (i hate pong symbol idk if this is caled # pong) and i will not make ahk scrypt for changing // to #
playermaxshield5 = 5 #i forgot about this one so its for fun if you want to play witch variables
playershield = 5 # player max shield5 is overiting it
player_crit_dmg_max = 4 # hceck dificulty selection it determits max adictinal dmg that can be make
enemyamunition = 200 # he he i still want to make coments with // :(
enemyshieldhp = 5 #;-;
first_time = True #if player start game it will be true you cna change that to false
enemy_simple_brain_for_hard_end_my_sufering_pls = 0 #i hate this is preventing errors and it make game posible to win
old_input_testers_dont_like_that = False #old input option is on whne true old = first select level after that press enter and press letter what to attack :)

#options
animation_speed_letter_d = 0.35 #animations peed for destroind letters can be changed in game options
animation_speed_letter_r = 0.35 # same but resored wall 
boat_name = "   " #boat name can be changed in game options it will display 3 letters only in game end screen will use boat name

#display conf
Dmode = 1 #1 use =╔║═╚╗╝ 2= /|-\\/ 3= /|=\\/ + #.center(120) .rjust(118//2) i use that 
ur = "╔" #up right
ul = "╗" #up left
li = "║" #line
dr = "╚" #down right
dl = "╝" #down left
ud = "═" #up && down
mr = "╠" # mid right
ml = "╣" #mid left
mu = "╩" #mid up
mr1 = "╟" #mid right for actions
ml1 = "╢"

############"|                |"
lastaction =f"{li}                {li}" #your last action
lastaction2 =f"{li}                {li}" #enemy last action

#debug varaibles can be changed in game options
debugingtime = 0 #1 yes 0 no thi is for turning cls on or off yes = on no = off (cls = clear)
errormsg = 0 #0off 1 on this is for adiotional info after match also its displaying errors
errorsmg_m = 0 #same rule just more info adictional info about game when end

#if you want to change numbers are some way %
enemymovN = {
    "Fire": 20,
    "Heal": 5,
    "Nothing": 80
}
enemymovH = {
    "Fire": 25,
    "Heal": 10,
    "Nothing": 60,
    "res": 8
}
enemymovHplus = { # i like bulling people
    "Fire": 35,
    "Heal": 15,
    "Nothing": 50,
    "res": 10
}


#terminal title
try:
    os.system("title " + "Ship-Game")
except Exception as e:
    pass


#clear terminal
def cls():
    global debugingtime #for debuging this disable cls funcion 1 == debuging info
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

#this is for game display customization
def display(t):
    global Dmode
    Dmode = t
    global ur, ul, li, dr, dl, ud, mr, ml, mu, mr1, ml1
    if Dmode == 1:
        ur = "╔" #up right
        ul = "╗" #up left
        li = "║" #line
        dr = "╚" #down right
        dl = "╝" #down left
        ud = "═" #up && down
        mr = "╠" # mid right
        ml = "╣" #mid left
        mu = "╩" #mid up
        mr1 = "╟" #mid right for actions
        ml1 = "╢"
    elif Dmode == 2:
        ur = "/" #up right
        ul = "\\" #up left
        li = "|" #line
        dr = "\\" #down right
        dl = "/" #down left
        ud = "-" #up && down
        mr = "|" # mid right
        ml = "|" #mid left
        mu = "-" #mid up
        mr1 = "|" #mid right for actions
        ml1 = "|"

#get terminal info
def get_t_s():
    try:
        size = os.get_terminal_size()
        return size.columns, size.lines
    except Exception as e:
        return -10, -10
width, height = get_t_s()
#print(f"{width} {height}")   
#this part of code will try to resize terminal/cmd
cls()
if width == -10 and height == -10:
    print("")
    print("There was an error while trying to get terminal size.")
    print("But still.")
    print("Your terminal size can be difrent that recomended")
    print("Recomended size is width: 120 or 121 height: 30")
    print("This mesange will dispaer after 10 seconds.")
    time.sleep(10)
if width != 120 and height != 30 or height != 30 and width != 121:
    print("")
    print("Your terminal size is difrent that recomended")
    print("Recomended size is width: 120 or 121 height: 30")
    print("This mesange will dispaer after 5 seconds.")
    time.sleep(5)


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
    elif dificulty == 4:
        randomef = {
            "hel": 9,
            "not": 60,
            "amo": 11,
            "shi": 6
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
        lastaction2 =f"{li}                {li}"
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
        lastaction2 ="║You res amo     ║"
        amunition += random.randint(1,4)
    elif endchoice == "shi":
        playershield += 1


def main_menu():
    while True:
        cls()
        #1 use =╔║═╚╗╝ 2= /|-\\/ 3= /|=\\/ + #.center(120) .rjust(118//2) i use that 
        a = "" #old one i dont want to delete this
        print(f"{ur}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ul}".center(120))
        print(f"{li} Terminal Ship Game {li}".center(120)) #print centered text
        print(f"{dr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl}".center(120))
        print("\n") #\n is just enter if you want another blank line add \n if you dont want blank line delete this print()
        print(f"{ur}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ul}".center(120))
        print(f"{li}   1.Play   {li}".center(120))
        print(f"{li} 2.Options  {li}".center(120))
        print(f"{li} 3.Tutorial {li}".center(120))
        print(f"{li}   0.Exit   {li}".center(120))
        print(f"{dr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl}".center(120))
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
            print("comming soon".center(120))
            time.sleep(0.75)
        elif option.upper() in exitl:
            exit()
        else:
            print("Wrong input Try again".center(120))
            time.sleep(0.75)

def options():
    global animation_speed_letter_d, boat_name, animation_speed_letter_r
    global old_input_testers_dont_like_that
    global debugingtime, errormsg, errorsmg_m
    while True:
        while True:
            try:
                cls()
                #╔║═╚╗╝.center(120) .rjust(118//2) i use that 
                print(f"{ur}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ul}".center(120))
                print(f"{li} Options {li}".center(120)) #print centered text
                print(f"{dr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl}".center(120))
                print("")
                print(f"{ur}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ul}".center(120))
                print(f"{li}   1.Change animations speed   {li}".center(120))
                print(f"{li}   2.Ship Name                 {li}".center(120))
                print(f"{li}   3.Input method              {li}".center(120))
                print(f"{li}   4.Aperance                  {li}".center(120))
                print(f"{li}   5.Debug                     {li}".center(120))
                print(f"{li}   0.Back                      {li}".center(120))
                print(f"{dr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl}".center(120))
                option = str(input("> ".rjust(118//2)))
                back = ["0","0.","BACK"]
                if option.upper() in back:
                    main_menu()
                    break
                elif option.upper() == "1":
                    while True:
                        cls()
                        print(f"{ur}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ul}".center(120))
                        print(f"{li} Animations Speed {li}".center(120)) #print centered text
                        print(f"{dr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl}".center(120))
                        print("")
                        print(f"{ur}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ul}".center(120))
                        print(f"{li}   1.Letters destroy speed     {li}".center(120))
                        print(f"{li}      2.Letter res speed       {li}".center(120))
                        print(f"{li}   0.Back                      {li}".center(120))
                        print(f"{dr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl}".center(120))
                        try:
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
                                    try:
                                        cls()
                                        print("")
                                        print("Type new letter animation speed normal = 1 you can type 0.X or X.X X is your number".center(120))
                                        print("")
                                        animspe = float(input("> ".rjust(118//2)))
                                        if animspe == 1 or animspe == 1.0:
                                            animation_speed_letter_r = 0.35
                                        else:
                                            animation_speed_letter_r = 0.35*animspe
                                        options()
                                        break
                                    except ValueError:
                                        print("This need to be float number ;-;".center(120))
                                        time.sleep(0.75)
                                        options()
                                        break
                        except Exception as e:
                            pass
                elif option.upper() == "2":
                    while True:
                        cls()
                        print("")
                        print("You can type any name for your Ship on the ship will be only dispaly 3 first characters".center(120))
                        print("")
                        boat_name = input("> ".rjust(118//2))
                        options()
                        break
                elif option.upper() == "3":
                    while True:
                        cls()
                        print("")
                        print("With one input method you prefer? (dificult is 2)".center(120))
                        print("")
                        print("1.Old [Two imputs]".center(120))
                        print("2.Type in one input (1a)".center(120))
                        print("0.Back".center(120))
                        print("")
                        selec = str(input("> ".rjust(118//2)))
                        sele1 = ["1.","1","OLD"]
                        sele2 = ["2.","2"]
                        sele3 = ["0","0.","Back"]
                        if selec.upper() in sele1:
                            old_input_testers_dont_like_that = True
                        elif selec.upper() in sele2:
                            old_input_testers_dont_like_that = False
                        elif selec.upper() in sele3:
                            break
                        else:
                            print("Wrong input.".center(120))
                            time.sleep(0.75)
                        break
                elif option.upper() == "4":
                    while True:
                        #╔║═╚╗╝╩.center(120) .rjust(118//2) i use that nah
                        cls()
                        print("")
                        print("What you want to change:".center(120))
                        print("")
                        print("1.Enemy look.".center(120))
                        print("2.Game visual apirance".center(120))
                        print("0.Back".center(120))
                        sele1 = ["1.","ENEMY","1"]
                        sele2 = ["2.","GAME","2"]
                        sele3 = ["0","0.","BACK"]
                        selec = str(input("> ".rjust(118//2)))
                        if selec.upper() in sele1:
                            pass
                        elif selec.upper() in sele2:
                            cls()
                            while True:
                                print("")
                                print("Select you farvorite theme".center(120))
                                print("")
                                #1 use =╔║═╚╗╝ 2= /|-\\/ 3= /|=\\/ + #.center(120) .rjust(118//2) i use that 
                                print("1.Standard theme.".center(120))
                                print("2.Symboll theme.".center(120))
                                print("0.Back.".center(120))
                                print("")
                                print("If you want to make custom one go to tutorials.".center(120))
                                sele1 = ["1.","1","STANDARD"]
                                sele2 = ["2.","2","SYMBOLL","SYMBOL"]
                                seleb = ["0","0.","BACK"]
                                selec = str(input("> ".rjust(118//2)))
                                if selec.upper() in sele1:
                                    display(1)
                                    break
                                elif selec.upper() in sele2:
                                    display(2)
                                    break
                                elif selec.upper() in seleb:
                                    break
                                else:
                                    print("wrong number input".center(120))
                                    time.sleep(0.75)
                                    cls()
                                cls()
                        elif selec.upper() in sele3:
                            break
                        else:
                            print("Wrong input.".center(120))
                            time.sleep(0.75)
                        break
                elif option.upper() == "5":
                    cls()
                    while True:
                        cls()
                        print("")
                        print("Change debug options:".center(120))
                        print("")
                        if debugingtime == 0:
                            print("1.Disable cls()".center(120))
                        else:
                            print("1.Enable cls()".center(120))
                        if errormsg == 0:
                            print("2.Enable error msg".center(120))
                        else:
                            print("2.Disable error msg".center(120))
                        if errorsmg_m == 0:
                            print("3.Enable more msg info".center(120))
                        else:
                            print("3.DIsable more msg info".center(120))
                        print("0.Back".center(120))
                        seleb = ["0","0.","BACK"]
                        selec = str(input("> ".rjust(118//2)))
                        if selec.upper() == "1" or selec.upper() == "1.":
                            if debugingtime == 1:
                                debugingtime = 0
                            else:
                                debugingtime = 1
                        elif selec.upper() == "2" or selec.upper() == "2.":
                            if errormsg == 0:
                                errormsg = 1
                            else:
                                errormsg = 0
                        elif selec.upper() == "3" or selec.upper() == "3.":
                            if errorsmg_m == 0:
                                errorsmg_m = 1
                            else:
                                errorsmg_m = 0
                        elif selec.upper() in seleb:
                            break
                        else:
                            cls()
                else:
                    print("Option not avalible or wrong number".center(120))
                    time.sleep(0.65)
            except Exception as e:
                pass
        break


def Play():
    global enemyhpnormalmax
    global curentenemyhp
    global dificulty
    global amunition
    global playershield, player_crit_dmg_max
    global enemy75p
    global enemy50p
    global playerhp
    global enemyamunition
    global enemyshieldhp
    global lastaction, lastaction2
    while True:
        cls()
        #╔║═╚╗╝.center(120) .rjust(118//2) i use that 
        print(f"{ur}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ul}".center(120))
        print(f"{li}Select your difuculty{li}".center(120))
        print(f"{dr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl}".center(120))
        print("\n")#\n is just enter if you want another blank line add \n if you dont want blank line delete this print()
        print(f"{ur}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ul}".center(120))
        print(f"{li}   1.Easy   {li}".center(120))
        print(f"{li}  2.Normal  {li}".center(120))
        print(f"{li}   3.Hard   {li}".center(120))
        print(f"{li}   4.Hard+  {li}".center(120))
        print(f"{li}   0.Back   {li}".center(120))
        print(f"{dr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl}".center(120))
        dif1 = ["1","1.","EASY","1.EASY"]
        dif2 = ["2","2.","NORMAL","NORMAI","2.NORMAL","2.NORMAI"]
        dif3 = ["3","3.","HARD","3.HARD"]
        dif4 = ["4","4.","HARD+","4.HARD+"]
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
                player_crit_dmg_max = 0
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
                player_crit_dmg_max = 4
                break
            elif dificultyt.upper() in dif3:
                dificulty = 3 #def 3
                amunition = 60 #def 60
                enemyhpnormalmax = 18 #def 18
                curentenemyhp = enemyhpnormalmax
                playershield = 2 #def 2
                playerhp = int(playermaxhp*0.9) #def *0.9
                enemyamunition = 250 #def 250
                enemyshieldhp = 5 #def 5
                player_crit_dmg_max = 3 #def 3
                break
            elif dificultyt.upper() in dif4:
                dificulty = 4
                amunition = 55 #def 55
                enemyhpnormalmax = 24
                curentenemyhp = enemyhpnormalmax
                playershield = 4
                playerhp = int(playermaxhp*0.8) #def *0.8
                enemyamunition = 260
                enemyshieldhp = 4
                player_crit_dmg_max = 2
                break
            else:
                #╔║═╚╗╝.center(120) .rjust(118//2) i use that 
                print("This need to be a existing dificulty number".center(120))
                time.sleep(0.75) #i like this number i also like 3 dont ask why i like 3 or why im teling in coment i like 3 i just like that number :)
        except ValueError as ve: #old code don't use this i will remake this and yes i used ' ;-;
            print("This need to be an number")
    enemy75p = int((enemyhpnormalmax/3)*2)-1
    enemy50p = int(enemyhpnormalmax/2)-1
    lastaction =f"{li}                {li}"
    lastaction2 =f"{li}                {li}"
    maingamelogic()


enemy75p = int((enemyhpnormalmax/3)*2)-1
enemy50p = int(enemyhpnormalmax/2)-1

def enemyhardsi(a, b):
    Elist = []
    b = 25
    print(Elist)
    # Check for index depends on enemy movement
    for i in range(enemycupo - a, enemycupo + b):
        if i < 0:
            Elist.append(unsafe_dec)  # Forced "D" if list is below 0
        if i > 25:
            Elist.append(unsafe_dec)
        if 0 <= i < len(enemylist):  # Check for potential error
            if enemylist[i] == str(safe_dec) or enemylist[i] == str(unsafe_dec):
                Elist.append(enemylist[i])  # Only append "S" or "D"
    return Elist

def enmyimposible():
    Elist = []
    # Check for index depends on enemy movement
    for i in range(0, 25):
        if i < 0:
            Elist.append(unsafe_dec)  # Forced "D" if list is below 0
        if i > 25:
            Elist.append(unsafe_dec)
        elif 0 <= i < len(enemylist):  # Check for potential error
            if enemylist[i] == str(safe_dec) or enemylist[i] == str(unsafe_dec):
                Elist.append(enemylist[i])  # Only append "S" or "D"
    return Elist

#for coments this is just the same what is in enemyhardsi with extra things in it
def restore():
    Rlist = []
    choice = 0
    if " " in list4: #check for " " in list if yes get there index numbers
        for i in range(0, len(list4)):
            if 0 <= i < len(list4):
                if list4[i] == " ":
                    Rlist.append(i)
        if Rlist: #duble check becouse why not 
            choice = random.choice(Rlist)
        else:
            choice = 420
    else: # if no return 420
        choice = 420
    return choice


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
    global enemy_simple_brain_for_hard_end_my_sufering_pls
    #reset evrything to def value
    enemylist = ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "D", "D", "D", "D", "D", "D","D","D","D","D","D","D"]
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
    lastaction =f"{li}                {li}"
    playerhp = playermaxhp
    first_time = True
    enemy_simple_brain_for_hard_end_my_sufering_pls = 0
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
                            print(f"{ur}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ul}".center(120))
                            print(f"{li}Wrong input.{li}".center(120))
                            print(f"{dr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl}".center(120))
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
                                            if curentenemyhp <= 0:
                                                er = "Enemy ded"
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
                                            enemylist[index] = str(unsafe_dec)
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
                                                if number == (enemycupo+1) and curentenemyhp >= enemy75p:
                                                    tyu = int(random.randint(0, player_crit_dmg_max))
                                                    curentenemyhp -= 1+tyu
                                                    lastaction ="║Atacked Enemy + ║"
                                                else:
                                                    curentenemyhp -=1
                                                lastaction ="║Atacked Enemy   ║"
                                            move = "Enemy"
                                            
                                            if curentenemyhp <= 0:
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
                                while True:
                                    try:
                                        if curentenemyhp > enemy75p:
                                            if enemycupo == 0:#bro 0 is the up enemy shuldn't go up
                                                randomdirection = 2 #set direction to down
                                            elif (enemycupo-2) < 0: #when enemy curent position - how many steps if < 0 then force to go down
                                                randomdirection = 2
                                            elif (enemycupo+4) >= 24: #when enemy curent position + 2 height + how many steps is mor ethat 25 force to go up
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
                                        elif curentenemyhp > enemy50p or curentenemyhp == enemy50p:
                                            if enemycupo == 0:#bro 0 is the up enemy shuldn't go up
                                                randomdirection = 2 #set direction to down
                                            elif (enemycupo-3) < 0: #when enemy curent position - how many steps if < 0 then force to go down
                                                randomdirection = 2
                                            elif (enemycupo+5) >= 24: #when enemy curent position + 2 height + how many steps is mor ethat 25 force to go up
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
                                        elif curentenemyhp > 1 or curentenemyhp == 1:
                                            if enemycupo == 0:#bro 0 is the up enemy shuldn't go up
                                                randomdirection = 2 #set direction to down
                                            elif (enemycupo-4) < 0: #when enemy curent position - how many steps if < 0 then force to go down
                                                randomdirection = 2
                                            elif (enemycupo+6) >= 24: #when enemy curent position + 2 height + how many steps is mor ethat 25 force to go up
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
                                        break
                                    except Exception as e:
                                        print(e)
                                        print("loop error")
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
                                        if enemyamunition > 0:
                                            enemyamunition -=1
                                            #lastaction ="║Atacked Enemy   ║" i need that to make lastaction
                                            lastaction ="║Enemy Atacked   ║"
                                            if playershield >= 1:
                                                playershield -= random.randint(1,2)#randomzie shield dmg
                                                if playershield <= 0:
                                                    playershield = 0
                                            else:
                                                playerhp -= random.randint(1,8) #randomize dmg
                                                playershield = 0
                                                if playerhp < 1:
                                                    er = "hp down"
                                                    raise Exception("hp down")
                                            #here will be animation handler i will do that in the futere
                                    elif endchoice == "Heal":
                                        if curentenemyhp >= enemyhpnormalmax:
                                            lastaction ="║Enemy res shield║"
                                            enemyshieldhp += 1
                                        else:
                                            lastaction ="║Enemy healed    ║" #idk how to say that
                                            howmuch = random.randint(1,3) #randomize how much heal fell free to modify
                                            curentenemyhp += howmuch
                                    elif endchoice == "Nothing":
                                        lastaction =f"{li}                {li}"
                                        pass #what did you encepted ;-; pass = skip this thing im trying not to swear in coments ok?
                            move = "Player"
                            break
                        elif dificulty == 3 or dificulty == 4:
                            #----------------------------------------------------
                            #
                            #ENEMY HANLDER FOR DIFCULTY ABOVE 2
                            #
                            #----------------------------------------------------
                            if move == "Enemy": #when enemy turn ENEMY CANT SHOT ON NORMAL MODE
                                if curentenemyhp > enemy75p: #enemy75p p stands for % 75 this number stand of hp 75% of hp
                                    #math to check if can move
                                    while True:
                                        try:
                                            if enemycupo == 0 or enemycupo == 1:#bro 0 is the up enemy shuldn't go up
                                                randomdirection = 2 #set direction to down
                                            elif (enemycupo-2) < 0: #when enemy curent position - how many steps if < 0 then force to go down
                                                randomdirection = 2
                                            elif (enemycupo+4) >= 25: #when enemy curent position + 2 height + how many steps is mor ethat 25 force to go up
                                                randomdirection = 1 #to do: swtch this to 2 steps 
                                            else:
                                                safepointup = 0
                                                safepointDo = 0
                                                if enemy_simple_brain_for_hard_end_my_sufering_pls >4:
                                                    enemy_simple_brain_for_hard_end_my_sufering_pls = 0
                                                Elist = enemyhardsi(2,5)
                                                if Elist[0] == str(safe_dec):
                                                    safepointup += 1
                                                if Elist[1] == str(safe_dec):
                                                    safepointup += 1
                                                if Elist[2] == str(safe_dec):
                                                    safepointup += 1
                                                if Elist[3] == str(safe_dec):
                                                    safepointup += 1
                                                    safepointDo += 1
                                                if Elist[6] == str(safe_dec):
                                                    safepointDo += 1
                                                if Elist[5] == str(safe_dec):
                                                    safepointDo += 1
                                                if Elist[4] == str(safe_dec):
                                                    safepointDo += 1
                                                if safepointup > safepointDo and enemy_simple_brain_for_hard_end_my_sufering_pls <5:
                                                    randomdirection = 1
                                                elif safepointDo > safepointup and enemy_simple_brain_for_hard_end_my_sufering_pls <5:
                                                    randomdirection = 2
                                                else:
                                                    #randomdirection = random.randint(1,2)
                                                    if enemycupo == 0 or enemycupo == 1:#bro 0 is the up enemy shuldn't go up
                                                        randomdirection = 2 #set direction to down
                                                    elif (enemycupo-2) < 0: #when enemy curent position - how many steps if < 0 then force to go down
                                                        randomdirection = 2
                                                    elif (enemycupo+4) >= 25: #when enemy curent position + 2 height + how many steps is mor ethat 25 force to go up
                                                        randomdirection = 1 #to do: swtch this to 2 steps 
                                                    else:
                                                        randomdirection = random.randint(1,2)
                                            #move logic
                                            if randomdirection == 1: #to understand hy look at def ship(): and on spritepos[]
                                                #i use index var becouse i like it
                                                Elist = enemyhardsi(2,5)# call the enemy si funcion to get list for enemy what to see hard+ will see in range to max 6up 8 down on hard: 2 up 4 down 4 becouse 2 on body 2 on down one part of body is implemented in funcion
                                                #for Elist enemy body is 3,4,5 in index
                                                if Elist[0] == str(safe_dec) and Elist[1] == str(safe_dec) and Elist[2] == str(safe_dec):
                                                    posenemy = enemycupo-2 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                elif Elist[0] == str(unsafe_dec) and Elist[1] == str(safe_dec) and Elist[2] == str(safe_dec) and Elist[3] == str(safe_dec):
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
                                                Elist = enemyhardsi(2,5)
                                                if Elist[6] == str(safe_dec) and Elist[5] == str(safe_dec) and Elist[4] == str(safe_dec):
                                                    posenemy = enemycupo+2 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                elif Elist[6] == str(unsafe_dec) and Elist[5] == str(safe_dec) and Elist[4] == str(safe_dec) and Elist[3] == str(safe_dec):
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
                                            break
                                        except Exception as e:
                                            print(e)
                                            print("loop error")
                                elif curentenemyhp > enemy50p or curentenemyhp > (enemy50p-4):
                                    while True:
                                        try:
                                            if enemycupo == 0:#bro 0 is the up enemy shuldn't go up
                                                randomdirection = 2 #set direction to down
                                            elif (enemycupo-3) < 0: #when enemy curent position - how many steps if < 0 then force to go down
                                                randomdirection = 2
                                            elif (enemycupo+5) >= 25: #when enemy curent position + 2 height + how many steps is mor ethat 25 force to go up
                                                randomdirection = 1 #to do: swtch this to 2 steps 
                                            else:
                                                safepointup = 0
                                                safepointDo = 0
                                                if enemy_simple_brain_for_hard_end_my_sufering_pls >4:
                                                    enemy_simple_brain_for_hard_end_my_sufering_pls = 0
                                                Elist = enemyhardsi(3,6)
                                                if Elist[0] == str(safe_dec):
                                                    safepointup += 1
                                                if Elist[1] == str(safe_dec):
                                                    safepointup += 1
                                                if Elist[2] == str(safe_dec):
                                                    safepointup += 1
                                                if Elist[3] == str(safe_dec):
                                                    safepointup += 1
                                                if Elist[6] == str(safe_dec):
                                                    safepointDo += 1
                                                if Elist[5] == str(safe_dec):
                                                    safepointDo += 1
                                                if Elist[4] == str(safe_dec):
                                                    safepointDo += 1
                                                    safepointup += 1
                                                if Elist[7] == str(safe_dec):
                                                    safepointDo += 1
                                                if safepointup > safepointDo and enemy_simple_brain_for_hard_end_my_sufering_pls <5:
                                                    randomdirection = 1
                                                elif safepointDo > safepointup and enemy_simple_brain_for_hard_end_my_sufering_pls <5:
                                                    randomdirection = 2
                                                else:
                                                    #randomdirection = random.randint(1,2)
                                                    if enemycupo == 0:#bro 0 is the up enemy shuldn't go up
                                                        randomdirection = 2 #set direction to down
                                                    elif (enemycupo-3) < 0: #when enemy curent position - how many steps if < 0 then force to go down
                                                        randomdirection = 2
                                                    elif (enemycupo+5) >= 25: #when enemy curent position + 2 height + how many steps is mor ethat 25 force to go up
                                                        randomdirection = 1 #to do: swtch this to 2 steps 
                                                    else:
                                                        randomdirection = random.randint(1,2)
                                            if randomdirection == 1: #to understand hy look at def ship(): and on spritepos[]
                                                #i use index var becouse i like it
                                                Elist = enemyhardsi(3,6)# call the enemy si funcion to get list for enemy what to see hard+ will see in range to max 6up 8 down on hard: 2 up 4 down 4 becouse 2 on body 2 on down one part of body is implemented in funcion
                                                #for Elist enemy body is 3,4,5 in index
                                                if Elist[0] == str(safe_dec) and Elist[1] == str(safe_dec) and Elist[2] == str(safe_dec):
                                                    posenemy = enemycupo-3 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                elif Elist[0] == str(unsafe_dec) and Elist[1] == str(safe_dec) and Elist[2] == str(safe_dec) and Elist[3] == str(safe_dec):
                                                    posenemy = enemycupo-2 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                elif Elist[0] == str(unsafe_dec) and Elist[1] == str(unsafe_dec) and Elist[2] == str(safe_dec) and Elist[3] == str(safe_dec):
                                                    posenemy = enemycupo-1 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                else:
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
                                                Elist = enemyhardsi(3,6)# call the enemy si funcion to get list for enemy what to see hard+ will see in range to max 6up 8 down on hard: 2 up 4 down 4 becouse 2 on body 2 on down one part of body is implemented in funcion
                                                #for Elist enemy body is 3,4,5 in index
                                                if Elist[7] == str(safe_dec) and Elist[6] == str(safe_dec) and Elist[5] == str(safe_dec):
                                                    posenemy = enemycupo+3 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                elif Elist[7] == str(unsafe_dec) and Elist[6] == str(safe_dec) and Elist[5] == str(safe_dec) and Elist[4] == str(safe_dec):
                                                    posenemy = enemycupo+2 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                elif Elist[7] == str(unsafe_dec) and Elist[6] == str(unsafe_dec) and Elist[5] == str(safe_dec) and Elist[4] == str(safe_dec):
                                                    posenemy = enemycupo+1 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                else:
                                                    posenemy = enemycupo+3 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want 
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
                                            break
                                        except Exception as e:
                                            print(e)
                                            print("loop error")
                                elif curentenemyhp > 1 or curentenemyhp == 1:
                                    while True:
                                        try:
                                            if enemycupo == 0:#bro 0 is the up enemy shuldn't go up
                                                randomdirection = 2 #set direction to down
                                            elif (enemycupo-4) < 0: #when enemy curent position - how many steps if < 0 then force to go down
                                                randomdirection = 2
                                            elif (enemycupo+6) >= 25: #when enemy curent position + 2 height + how many steps is mor ethat 25 force to go up
                                                randomdirection = 1 #to do: swtch this to 2 steps 
                                            else:
                                                safepointup = 0
                                                safepointDo = 0
                                                if enemy_simple_brain_for_hard_end_my_sufering_pls >4:
                                                    enemy_simple_brain_for_hard_end_my_sufering_pls = 0
                                                Elist = enemyhardsi(4,8)
                                                #here index 5 is enemy center
                                                if Elist[0] == str(safe_dec):
                                                    safepointup += 1
                                                if Elist[1] == str(safe_dec):
                                                    safepointup += 1
                                                if Elist[2] == str(safe_dec):
                                                    safepointup += 1
                                                if Elist[3] == str(safe_dec):
                                                    safepointup += 1
                                                if Elist[6] == str(safe_dec):
                                                    safepointDo += 1
                                                if Elist[5] == str(safe_dec):
                                                    safepointDo += 1
                                                    safepointup += 1
                                                if Elist[4] == str(safe_dec):
                                                    safepointDo += 1
                                                if Elist[7] == str(safe_dec):
                                                    safepointDo += 1
                                                if Elist[8] == str(safe_dec):
                                                    safepointDo += 1
                                                if safepointup > safepointDo and enemy_simple_brain_for_hard_end_my_sufering_pls <5:
                                                    randomdirection = 1
                                                elif safepointDo > safepointup and enemy_simple_brain_for_hard_end_my_sufering_pls <5:
                                                    randomdirection = 2
                                                else:
                                                    #randomdirection = random.randint(1,2)
                                                    if enemycupo == 0:#bro 0 is the up enemy shuldn't go up
                                                        randomdirection = 2 #set direction to down
                                                    elif (enemycupo-4) < 0: #when enemy curent position - how many steps if < 0 then force to go down
                                                        randomdirection = 2
                                                    elif (enemycupo+6) >= 25: #when enemy curent position + 2 height + how many steps is mor ethat 25 force to go up
                                                        randomdirection = 1 #to do: swtch this to 2 steps 
                                                    else:
                                                        randomdirection = random.randint(1,2)
                                            if randomdirection == 1: #to understand hy look at def ship(): and on spritepos[]
                                                #i use index var becouse i like it
                                                Elist = enemyhardsi(4,8)# call the enemy si funcion to get list for enemy what to see hard+ will see in range to max 6up 8 down on hard: 2 up 4 down 4 becouse 2 on body 2 on down one part of body is implemented in funcion
                                                #for Elist enemy body is 3,4,5 in index
                                                if Elist[0] == str(safe_dec) and Elist[1] == str(safe_dec) and Elist[2] == str(safe_dec) and Elist[3] == str(safe_dec):
                                                    posenemy = enemycupo-4 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                elif Elist[0] == str(unsafe_dec) and Elist[1] == str(safe_dec) and Elist[2] == str(safe_dec) and Elist[3] == str(safe_dec) and Elist[4] == str(safe_dec):
                                                    posenemy = enemycupo-3 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                elif Elist[0] == str(unsafe_dec) and Elist[1] == str(unsafe_dec) and Elist[2] == str(safe_dec) and Elist[3] == str(safe_dec) and Elist[4] == str(safe_dec) and Elist[5] == str(safe_dec):
                                                    posenemy = enemycupo-2 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                elif Elist[0] == str(unsafe_dec) and Elist[1] == str(unsafe_dec) and Elist[2] == str(unsafe_dec) and Elist[3] == str(safe_dec) and Elist[4] == str(safe_dec) and Elist[5] == str(safe_dec):
                                                    posenemy = enemycupo-1 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                else:
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
                                                Elist = enemyhardsi(4,8)# call the enemy si funcion to get list for enemy what to see hard+ will see in range to max 6up 8 down on hard: 2 up 4 down 4 becouse 2 on body 2 on down one part of body is implemented in funcion
                                                #for Elist enemy body is 3,4,5 in index
                                                if Elist[8] == str(safe_dec) and Elist[7] == str(safe_dec) and Elist[6] == str(safe_dec) and Elist[5] == str(safe_dec):
                                                    posenemy = enemycupo+4 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                elif Elist[8] == str(unsafe_dec) and Elist[7] == str(safe_dec) and Elist[6] == str(safe_dec) and Elist[5] == str(safe_dec) and Elist[4] == str(safe_dec):
                                                    posenemy = enemycupo+3 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                elif Elist[8] == str(unsafe_dec) and Elist[7] == str(unsafe_dec) and Elist[6] == str(safe_dec) and Elist[5] == str(safe_dec) and Elist[4] == str(safe_dec) and Elist[5] == str(safe_dec):
                                                    posenemy = enemycupo+2 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                elif Elist[8] == str(unsafe_dec) and Elist[7] == str(unsafe_dec) and Elist[6] == str(unsafe_dec) and Elist[5] == str(safe_dec) and Elist[4] == str(safe_dec) and Elist[5] == str(safe_dec):
                                                    posenemy = enemycupo+1 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want
                                                else:
                                                    posenemy = enemycupo+4 #this is hanlding how many steps in state he can take
                                                    enemycupo = posenemy #this hanlde enemy also delete = enemy moves when he want 
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
                                            break
                                        except Exception as e:
                                            print(e)
                                            print("loop error")
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
                                    if dificulty == 3:
                                        for text, percent in enemymovH.items(): #magic :) this shuld makes a long list nah
                                            nah.extend([text]*percent)
                                    elif dificulty == 4:
                                        for text, percent in enemymovHplus.items(): #magic :) this shuld makes a long list nah
                                            nah.extend([text]*percent)
                                    endchoice = random.choice(nah) #randomize what enemy will do from long list (for any dificulty above normal this will be dont in other way)
                                    #"Fire": x,"Heal": x,"Nothing": x  x=precents + names all this are write in enemymovN
                                    if endchoice == "Fire":
                                        if enemyamunition > 0:
                                            enemyamunition -=1
                                            #lastaction ="║Atacked Enemy   ║" i need that to make lastaction
                                            lastaction ="║Enemy Atacked   ║"
                                            if playershield >= 1:
                                                playershield -= random.randint(1,2)#randomzie shield dmg
                                                if playershield <= 0:
                                                    playershield = 0
                                            else:
                                                playerhp -= random.randint(1,10) #randomize dmg
                                                playershield = 0
                                                if playerhp < 1:
                                                    er = "hp down"
                                                    raise Exception("hp down")
                                            #here will be animation handler i will do that in the futere
                                        else:
                                            pass
                                    elif endchoice == "Heal":
                                        if curentenemyhp >= enemyhpnormalmax:
                                            lastaction ="║Enemy res shield║"
                                            enemyshieldhp += 1
                                        else:
                                            lastaction ="║Enemy healed    ║" #idk how to say that
                                            howmuch = random.randint(1,3) #randomize how much heal fell free to modify
                                            curentenemyhp += howmuch
                                    elif endchoice == "Nothing":
                                        lastaction =f"{li}                {li}"
                                        pass #what did you encepted ;-; pass = skip this thing im trying not to swear in coments ok?
                                    elif endchoice == "res":
                                        res = restore()
                                        if res == 420:
                                            lastaction =f"{li}                {li}"
                                        else:
                                            #add animations here you idiot
                                            list4[res] = safe_list[res]
                                            aniamtion_is_playing = True
                                            ship()
                                            time.sleep(animation_speed_letter_r)
                                            cls()
                                            list4[res] = " "
                                            ship()
                                            time.sleep(animation_speed_letter_r)
                                            cls()
                                            list4[res] = safe_list[res]
                                            aniamtion_is_playing = False
                                            lastaction ="║Enemy res wall  ║"
                            move = "Player"
                            break
                        elif dificulty == 5:
                            pass
                elif aniamtion_is_playing == True:
                    pass
                if amunition <= 0:
                    er = "Ammo out"
                    raise Exception("Ammo out")
        except Exception as e:
            er = e
            if errormsg == 1:
                print(er)
            errormesd = ""
            erormesu = ""
            if str(er) == "Ammo out":
                el = 0 #0 lose 1 win
                erormesu = "╔═════════════════════════════╗"
                errormes = "║Because you have no more ammo║" #mesage after W or L
                errormesd= "╚═════════════════════════════╝"
            elif str(er) == "Enemy ded":
                el = 1
                erormesu = "╔═════════════════════════════╗"
                errormes = "║ You defeated the \"enemy\". ║" #enemy will be replaced witch var to name enemy
                errormesd= "╚═════════════════════════════╝"
            elif str(er) == "hp down":
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
                if errormsg == 1:
                    print(e)
                if errorsmg_m == 1:
                    print(e.args)
                    traceback.print_exc()
                    print(f"enemycupo: {enemycupo}, posenemy: {posenemy}, index: {index}, spritepos len: {len(spritepos)}")
                    print(f"Enemy hp: {curentenemyhp}, Enemy ammo: {enemyamunition}, Enemy shield: {enemyshieldhp}")
                    print(f"player hp: {playerhp}, player ammo: {amunition}, player shield: {playershield}")
                    print(f"t3684tiyf78t238gfuidtf873tuirhsdtf78wufuisdf87w4gfuisduigv78wyf")
                if el == 1:
                    print(f"{ur}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ul}".center(120))
                    print(f"{li}You Win {li}".center(120))
                    print(f"{dr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl}".center(120))
                elif el == 0:
                    print(f"{ur}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ul}".center(120))
                    print(f"{li}You Lost{li}".center(120))
                    print(f"{dr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl}".center(120))
                    print(erormesu.center(120))
                    print(errormes.center(120))
                    print(errormesd.center(120))
                print(f"{ur}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ul}".center(120))
                print(f"{li}Wanna go to the menu?{li}".center(120))
                print(f"{dr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl}".center(120))
                print("")
                print(f"{ur}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ul}".center(120))
                print(f"{li}   1.Yes   {li}".center(120))
                print(f"{li}   2.No    {li}".center(120))
                print(f"{dr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl}".center(120))
                print("")
                if errormsg == 1:
                    print(e)
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

inputs = ""
ia = ""
ib = ""
def ship(): #game board dont make sens ik
    global ListNumber
    global ListLetter
    global inputs
    global ia, ib
    if dificulty == 1:
        cls()
        print(f"{li}                                                                          {li} levels: {li}1|2|3{li}Enemy[4]{li} {li}  Information   {li}")
        print(f"{mr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{mu}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{mu}{ud}{ud}{ud}{ud}{ud}{mu}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl} {mr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ml}")
        print(f"{li}                                                                                    ", list[0] , list2[0] , list3[0] , f"{spritepos[0]:<7}" ,safe_list[0],f"{li}Gamemode: Easy  {li}")
        print(f"{li}                                                                                    ", list[1] , list2[1] , list3[1] , f"{spritepos[1]:<7}" ,safe_list[1],f"{mr1}----------------{ml1}")
        print(f"{li}                                                                                    ", list[2] , list2[2] , list3[2] , f"{spritepos[2]:<7}" ,safe_list[2],f"{li}Your hp:  inf   {li}") 
        print(f"{li}                                                                                    ", list[3] , list2[3] , list3[3] , f"{spritepos[3]:<7}" ,safe_list[3],f"{li}Your amo: inf   {li}")#am = amunition
        print(f"{li}                                                                                    ", list[4] , list2[4] , list3[4] , f"{spritepos[4]:<7}" ,safe_list[4],f"{li}Shield hp: 0    {li}")
        print(f"{li}                                                                                    ", list[5] , list2[5] , list3[5] , f"{spritepos[5]:<7}" ,safe_list[5],f"{mr1}----------------{ml1}")
        print(f"{li}                                                                                    ", list[6] , list2[6] , list3[6] , f"{spritepos[6]:<7}" ,safe_list[6],f"{li}Enemy hp: {curentenemyhp:<6}{li}")#f  string allow for less spaces in code + more control over formating
        print(f"{li}                                                                                    ", list[7] , list2[7] , list3[7] , f"{spritepos[7]:<7}" ,safe_list[7],f"{li}Enemy amo: 0    {li}")#am = amunition
        print(f"{li}                                                                                    ", list[8] , list2[8] , list3[8] , f"{spritepos[8]:<7}" ,safe_list[8],f"{li}Shield hp: 0    {li}")
        print(f"{li}                                                                                    ", list[9] , list2[9] , list3[9] , f"{spritepos[9]:<7}" ,safe_list[9],f"{mr1}----------------{ml1}")
        print(f"{li}                                                                                    ", list[10], list2[10], list3[10], f"{spritepos[10]:<7}" ,safe_list[10],lastaction)
        print(f"{li}                                                                                    ", list[11], list2[11], list3[11], f"{spritepos[11]:<7}" ,safe_list[11],f"{dr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl}")
        print(f"{li}                                                                                    ", list[12], list2[12], list3[12], f"{spritepos[12]:<7}" ,safe_list[12])
        print(f"{li}                                                                                    ", list[13], list2[13], list3[13], f"{spritepos[13]:<7}" ,safe_list[13])
        print(f"{li}                                                                                    ", list[14], list2[14], list3[14], f"{spritepos[14]:<7}" ,safe_list[14])
        print(f"{li}                                                                                    ", list[15], list2[15], list3[15], f"{spritepos[15]:<7}" ,safe_list[15])
        print(f"{li}                                                                                    ", list[16], list2[16], list3[16], f"{spritepos[16]:<7}" ,safe_list[16])
        print(f"{li}                                                                                    ", list[17], list2[17], list3[17], f"{spritepos[17]:<7}" ,safe_list[17])
        print(f"{li}                                                                                    ", list[18], list2[18], list3[18], f"{spritepos[18]:<7}" ,safe_list[18])
        print(f"{li}                          )___(                                                     ", list[19], list2[19], list3[19], f"{spritepos[19]:<7}" ,safe_list[19])
        print(f"{li}                    _______\__\_                                                    ", list[20], list2[20], list3[20], f"{spritepos[20]:<7}" ,safe_list[20])
        print(f"{li}              ___   |===========\     ___                                           ", list[21], list2[21], list3[21], f"{spritepos[21]:<7}" ,safe_list[21])
        print(f"{li}        __   [///]__|____________\___[\\\\\]    __       ____                         ", list[22], list2[22], list3[22], f"{spritepos[22]:<7}" ,safe_list[22])
        print(f"{li}     __[//]__/                            \__[//]_____/   /                         ", list[23], list2[23], list3[23], f"{spritepos[23]:<7}" ,safe_list[23])
        print(f"{li}    |{boat_name[:3]:<3}                                                 /                          ", list[24], list2[24], list3[24], f"{spritepos[24]:<7}" ,safe_list[24])
        print(f"{li}     \__________________________________________________/                           ", list[25], list2[25], list3[25], f"{spritepos[25]:7}" ,safe_list[25])
        print(f"{dr}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",f"/{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}\\")
        # dont make sense
        if aniamtion_is_playing == False:
            if move == "Player":
                if old_input_testers_dont_like_that == True:
                    if idk == False:
                        ListNumber = str(input("Select a level: "))
                    else:
                        ListLetter = str(input("Select a letter: "))
                else: #this allow you to type 1a level and letter in one input ia and ib are becouse i treid to make this another way
                    #didnt work that why there is ia and ib
                    if idk == False:
                        inputs = input("What to attack (1a): ")
                    else:
                        ListLetter = str(ib)
                    if len(inputs) >= 2 and inputs[0].isdigit(): #check min input character 
                        ia = int(inputs[0])
                        ib = str(inputs[1])
                        ListNumber = str(ia)
                        ListLetter = str(ib)
                    
    elif dificulty >= 2 and dificulty <= 5:
        if amunition > 999:
            amutext = 999
        else:
            amutext = amunition
        cls()
        dificultytex = ""
        if dificulty == 2:
            dificultytex = "Normal"
        elif dificulty == 3:
            dificultytex = "Hard"
        elif dificulty == 4:
            dificultytex = "Hard+"
        print(f"{li}                                                                        {li} levels: {li}1{li}2{li}3{li}4{li}Enemy[5]{li} {li}  Information   {li}")
        print(f"{mr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{mu}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{mu}{ud}{mu}{ud}{mu}{ud}{mu}{ud}{mu}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl} {mr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ml}")
        print(f"{li}                                                                                  ", list[0] , list2[0] , list3[0] ,list4[0] , f"{spritepos[0]:<7}" ,safe_list[0],f"{li}Gamemode: {dificultytex:<6}{li}")#16 characters
        print(f"{li}                                                                                  ", list[1] , list2[1] , list3[1] ,list4[1] , f"{spritepos[1]:<7}" ,safe_list[1],f"{mr1}----------------{ml1}")
        print(f"{li}                                                                                  ", list[2] , list2[2] , list3[2] ,list4[2] , f"{spritepos[2]:<7}" ,safe_list[2],f"{li}Your hp: {playerhp:<7}{li}") 
        print(f"{li}                                                                                  ", list[3] , list2[3] , list3[3] ,list4[3] , f"{spritepos[3]:<7}" ,safe_list[3],f"{li}Your amo: {amutext:<6}{li}")#am = amunition + f string allow for less spaces in code + more control over formating
        print(f"{li}                                                                                  ", list[4] , list2[4] , list3[4] ,list4[4] , f"{spritepos[4]:<7}" ,safe_list[4],f"{li}Shield hp: {playershield:<5}{li}")
        print(f"{li}                                                                                  ", list[5] , list2[5] , list3[5] ,list4[5] , f"{spritepos[5]:<7}" ,safe_list[5],f"{mr1}----------------{ml1}")
        print(f"{li}                                                                                  ", list[6] , list2[6] , list3[6] ,list4[6] , f"{spritepos[6]:<7}" ,safe_list[6],f"{li}Enemy hp: {curentenemyhp:<6}{li}")
        print(f"{li}                                                                                  ", list[7] , list2[7] , list3[7] ,list4[7] , f"{spritepos[7]:<7}" ,safe_list[7],f"{li}Enemy amo: {enemyamunition:<5}{li}")#am = amunition
        print(f"{li}                                                                                  ", list[8] , list2[8] , list3[8] ,list4[8] , f"{spritepos[8]:<7}" ,safe_list[8],f"{li}Shield hp: {enemyshieldhp:<5}{li}")
        print(f"{li}                                                                                  ", list[9] , list2[9] , list3[9] ,list4[9] , f"{spritepos[9]:<7}" ,safe_list[9],f"{mr1}----------------{ml1}")
        print(f"{li}                                                                                  ", list[10], list2[10], list3[10], list4[10], f"{spritepos[10]:<7}" ,safe_list[10],lastaction)
        print(f"{li}                                                                                  ", list[11], list2[11], list3[11], list4[11], f"{spritepos[11]:<7}" ,safe_list[11],lastaction2)
        print(f"{li}                                                                                  ", list[12], list2[12], list3[12], list4[12], f"{spritepos[12]:<7}" ,safe_list[12],f"{dr}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{dl}")
        print(f"{li}                                                                                  ", list[13], list2[13], list3[13], list4[13], f"{spritepos[13]:<7}" ,safe_list[13])
        print(f"{li}                                                                                  ", list[14], list2[14], list3[14], list4[14], f"{spritepos[14]:<7}" ,safe_list[14])
        print(f"{li}                                                                                  ", list[15], list2[15], list3[15], list4[15], f"{spritepos[15]:<7}" ,safe_list[15])
        print(f"{li}                                                                                  ", list[16], list2[16], list3[16], list4[16], f"{spritepos[16]:<7}" ,safe_list[16])
        print(f"{li}                                                                                  ", list[17], list2[17], list3[17], list4[17], f"{spritepos[17]:<7}" ,safe_list[17])
        print(f"{li}                                                                                  ", list[18], list2[18], list3[18], list4[18], f"{spritepos[18]:<7}" ,safe_list[18])
        print(f"{li}                          )___(                                                   ", list[19], list2[19], list3[19], list4[19], f"{spritepos[19]:<7}" ,safe_list[19])
        print(f"{li}                    _______\__\_                                                  ", list[20], list2[20], list3[20], list4[20], f"{spritepos[20]:<7}" ,safe_list[20])
        print(f"{li}              ___   |===========\     ___                                         ", list[21], list2[21], list3[21], list4[21], f"{spritepos[21]:<7}" ,safe_list[21])
        print(f"{li}        __   [///]__|____________\___[\\\\\]    __       ____                       ", list[22], list2[22], list3[22], list3[22], spritepos[22] ,safe_list[22])
        print(f"{li}     __[//]__/                            \__[//]_____/   /                       ", list[23], list2[23], list3[23], list4[23], f"{spritepos[23]:<7}" ,safe_list[23])
        print(f"{li}    |{boat_name[:3]:<3}                                                 /                        ", list[24], list2[24], list3[24], list4[24], f"{spritepos[24]:<7}" ,safe_list[24])
        print(f"{li}     \__________________________________________________/                         ", list[25], list2[25], list3[25], list4[25], f"{spritepos[25]:<7}" ,safe_list[25])
        print(f"{dr}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",f"/{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}{ud}\\")
        # dont make sense
        if aniamtion_is_playing == False:
            if move == "Player":
                if old_input_testers_dont_like_that == True:
                    if idk == False:
                        ListNumber = str(input("Select a level: "))
                    else:
                        ListLetter = str(input("Select a letter: "))
                else:
                    if idk == False:
                        inputs = input("What to attack (1a): ")
                    else:
                        ListLetter = str(ib)
                    if len(inputs) >= 2 and inputs[0].isdigit():
                        ia = int(inputs[0])
                        ib = str(inputs[1])
                        ListNumber = str(ia)
                        ListLetter = str(ib)

main_menu()