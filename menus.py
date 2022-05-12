from utilities import* #local library

def main_menu(gl):
    clear()
    slow_print(fgbg(123,93)+"Welcome to Arithmetic Skill Building Game!!"+nc(),0)
    slow_print(fg(46)+"\nEnter the option number for the choice you wish to select:\n",0.04)
    slow_print(fgbg(15,9)+"\nPlease Select an operation:\n",0.04)

    for item in gl.items():
        print("\033[0;30;47m "+str(item[0])+" \033[1;37;40m "+item[1][0])
        time.sleep(0.4)

    choice = input(fg(46)+"\n>>> "+nc())
    return(choice)

def petc():
    input("Press Enter to Continue...")
    clear()

def option_validator(given_option,true_range):
    if(given_option.isdigit()==True):
        given_option = int(given_option)
        if(given_option in true_range):
            return(True)
        else:
            print("Selected option number not part of given options\nTry again")
            petc()
            return(False)
    else:
        print("Invalid input. Try again!!")
        petc()
        return(False)

def game_start_menu(game_name):
    clear()
    slow_print(fgbg(15,2)+game_name+"\n",0.04)

    slow_print(fgbg(15,9)+"\nPlease Select an operation:\n",0.04)
    print("\033[0;30;47m 1 \033[1;37;40m Start Game")
    time.sleep(0.4)
    print("\033[0;30;47m 2 \033[1;37;40m Back")
    time.sleep(0.4)

    return input(fg(46)+">>> "+nc())
