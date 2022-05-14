from utilities import*
from menus import*
from games import*

def main():
    while(True):

        #starting main menu and retreving selected input
        menu_option = main_menu(game_list)

        #validating given option
        if option_validator(menu_option,int,game_list.keys()) == False :
            continue
        else:
            menu_option = int(menu_option)

        #selecting course of action from list as per given option
        game_list[menu_option][1]()



if __name__ == "__main__":
    main()
