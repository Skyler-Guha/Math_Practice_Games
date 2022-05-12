from utilities import * #local library
from menus import petc, option_validator, game_start_menu
import random

#Game list
game_list = {1:("Addition",lambda:addition_game()),
             2:("Exit",lambda:exit())}


#===============Games=============
def addition_game():#maybe rewrite this?
    while(True):

        menu_option = game_start_menu("Addition")

        #validating given option
        if option_validator(menu_option,[1,2]) == False :
            continue
        else:
            menu_option = int(menu_option)

        if(menu_option==2):
            break




        #getting digit range and no of quesions
        degit_range = None
        no_of_ques= None
        while(True):
            clear()

            slow_print(fg(46)+"Enter range of numbers you wish to practice in starting from 0 and ending at x till 100000: ",0.01)
            degit_range = input(fg(46)+"\n>>> ")

            if option_validator(degit_range,range(0,100000)) == False :
                continue
            else:
                degit_range = int(degit_range)



            slow_print(fg(46)+"\nEnter number of question you want to attempt(max 100): ",0.01)
            no_of_ques = input(fg(46)+"\n>>> ")

            if option_validator(no_of_ques,range(1,100)) == False :
                continue
            else:
                no_of_ques = int(no_of_ques)

            break

        clear()
        print(fgbg(232,226)+"if at any time you wish to stop then give answere as \"stop\"\n")

        score = 0
        for i in range (1,no_of_ques+1):

            print(fgbg(232,226)+"Question",i)
            a=random.randrange(-degit_range,degit_range)
            b=random.randrange(-degit_range,degit_range)

            pr = str(a)+" + "+str(b)+" = "
            ans =input(pr)

            while True:
                if (ans==""):
                    print(fgbg(232,3)+"no value entered ,try again !!")
                    pr = str(a)+" + "+str(b)+" = "
                    ans =input(pr)
                elif(ans=="stop"):
                    break
                else:
                    ans = int(ans)
                    break

            if(ans == "stop"):
                    break
            elif(ans == a+b):
                print(fgbg(15,2)+"correct\n")
                score += 1

            else:
                print(fgbg(15,1)+"incorect\nAns is: "+str(a+b)+"\n")


        enter = input(fgbg(123,93)+"your Score was: "+str(score)+" out of "+str(no_of_ques)+"\n"+nc()+"press enter to continue"+nc())
        break
