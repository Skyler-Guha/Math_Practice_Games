from utilities import* #local library

def main_menu(gl):
    clear()
    slow_print(fgbg(123,93)+"Welcome to Arithmetic Skill Building Game!!"+NC+ES,0)
    slow_print(fg(46)+"\nEnter the option number for the choice you wish to select:\n",0.03)
    slow_print(fgbg(15,9)+"\nPlease Select an operation:"+NC+ES+"\n",0.03)

    for item in gl.items():
        print("\033[0;30;47m "+str(item[0])+" \033[1;37;40m "+item[1][0])
        time.sleep(0.4)

    choice = input(fg(46)+">>> "+NC)
    return(choice)

def petc(color=NC,clr=True):
    input(color+"Press Enter to Continue..."+NC+ES)
    if(clr):clear()

def option_validator(given_option,type,true_range=None,stop=True):
    try:
        given_option = type(given_option)

    except Exception:
        #if type conversion fails
        if(stop):
            print("Invalid input. Try again!!")
            petc()
        return(False)

    if(true_range==None):
        return(True)
    elif(given_option in true_range):
        return(True)
    else:
        if(stop):
            print("Selected option number not part of given options\nTry again")
            petc()
        return(False)


def game_start_menu(game_name):
    clear()
    slow_print(fgbg(15,2)+game_name+"\n",0.04)

    slow_print(fgbg(15,9)+"\nPlease Select an operation:"+NC+ES+"\n",0.03)
    print("\033[0;30;47m 1 \033[1;37;40m Start Game")
    time.sleep(0.4)
    print("\033[0;30;47m 2 \033[1;37;40m Back")
    time.sleep(0.4)

    return input(fg(46)+">>> "+NC)
