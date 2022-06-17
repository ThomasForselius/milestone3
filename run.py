from colorama import Fore, Back, Style, init
init(autoreset=True)
from tabulate import tabulate
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('players')

players_sheet = SHEET.worksheet('players')
admins_sheet = SHEET.worksheet('admins')

players = players_sheet.get_all_values()  # gets all values from players sheet
admins = admins_sheet.get_all_values()  # gets all values from admin sheet


def main_menu():
    """
    Shows the main menu in the program:
        1. Create player
        2. Delete Player
        3. Update Player
        4. Show Player List
        5. Show Admin List
        6. Exit program
    """
    while True:
        print(Fore.GREEN + f"\t --- Main menu --- \n")
        print(Fore.GREEN + f"\t1: Create new Player")
        print(Fore.GREEN + f"\t2: Delete player")
        print(Fore.GREEN + f"\t3: Update Player Score")
        print(Fore.GREEN + f"\t4: Show Player list")
        print(Fore.GREEN + f"\t5: Show Admin List")
        print(Fore.GREEN + f"\t6: Exit program")
        print("\n")
        menu_num = 0
        try:
            menu_num = int(input("Enter a number below: \n\n"))
            print("\n")
        except ValueError:
            print(Fore.RED + f"* Error * \nincorrect value.")
            print("Please enter a number from 1 - 6\n\n")

        if menu_num == 1:
            new_player()
        elif menu_num == 2:
            delete_player('players')
        elif menu_num == 3:
            update_score("players")
        elif menu_num == 4:
            show_players('players')
        elif menu_num == 5:
            show_players('admins')
        elif menu_num == 6:
            exit()
        elif menu_num > 6:
            print(Fore.RED + "Not a number between 1 and 6, try again.\n")


def count_players(type):
    """
    Counts the number of players in a certain sheet and returns the value -1
    """
    num = SHEET.worksheet(type).row_count - 1
    return num


def show_players(type):
    """
    Gets players or admins from sheet
    """
    print(Fore.GREEN + f"\n*** Getting {type} from worksheet... ***\n")
    data = SHEET.worksheet(type).get_all_values()[1:]
    i = 1
    players_num = count_players('players')
    if players_num < 1:
        print(Fore.RED + "No players to display, add one first.\n\n")
        main_menu()
    player_list = []
    print(Fore.CYAN)
    for x in data:
        name = [i,x[0],x[1]]
        player_list.append(name)
        if type == "players":
            name.append(x[4])
        i += 1
    if type == "players":
        print(tabulate(player_list, headers=["Num:","First Name","Last Name","Score"],  tablefmt="github"))
        print(f"\n")
    else:
        print(tabulate(player_list, headers=["Num:","First Name","Last Name"], tablefmt="github"))
        print(f"\n")
    print(Fore.GREEN + f"*** End of player list *** \n")


def update_score(type):
    """
    Updates score for a certain player
    """
    show_players(type)
    player_check = True
    while player_check is True:
        try:
            player_choice = int(input(f"Choose a player number:"))
            print("Enter number for corresponding player:\n")
            player_count = count_players('players')
            print(player_count)
            if player_choice == 0:
                player_check = False
            elif player_choice > player_count > player_choice:
                print("You must choose a player from list, try again")
                print(f"Choice: {player_choice}")
                print(player_count)
                player_check = True
            elif 1 <= player_choice <= player_count:
                choice = player_choice+1
                score = players_sheet.row_values(choice)[4]
                print(f"Current score: {score}")
                first_name = players_sheet.row_values(choice)[0]
                last_name = players_sheet.row_values(choice)[1]
                print(f"You chose player: {first_name} {last_name}\n")
                score_check = False
                while score_check is False:
                    try:
                        menu_input_score = int(input("Enter new score:\n"))
                        print(f"*** Updating points for: ***")
                        print(f"{first_name} {last_name}\n")
                        players_sheet.update(f'E{choice}', menu_input_score)
                        print("*** Points updated successfully! ***\n")
                        score_check = True
                    except ValueError:
                        print(Fore.RED + "Mut be a number, try again ")
                break
        except ValueError:
            print(Fore.RED + f"Only numbers are allowed, try again.\n")


def new_player():
    """
    Creates a new instance of regular player
    """
    print(Back.CYAN + "\n***** Create a player *****")
    print(Style.RESET_ALL)
    print("\n")
    print(f"You must enter information about the player you wish to create.\n")
    print(f"These are the required credentials: \n")
    print(f"- Admin or Regular player")
    print(f"- First name")
    print(f"- Last name")
    print(f"- Age")
    print(f"- Email\n")
    type = ""
    type_alt = ["admin", "player"]
    type_check = False
    while type_check is False:
        print(Fore.CYAN + "* Admin or Player? *")
        type = input()
        type_lower = str(type).lower()
        has = type_lower in type_alt
        if has:
            type_check = True
    f_name = ""
    f_name_check = False
    while f_name_check is False:
        try:
            print(Fore.CYAN + "First name:")
            f_name = input()
            if len(f_name) > 2:
                f_name_check = True
            else:
                print(Fore.RED + "Name too short, try again.")
                f_name_check = False
        except ValueError as e:
                print(f"Something went wrong: {e}\n")
    l_name = ""
    l_name_check = False
    while l_name_check is False:
        try:
            print(Fore.CYAN + "* Last Name:")
            l_name = input()
            if len(l_name) > 2:
                l_name_check = True
            else:
                print(Fore.RED + "Last name too short, try again.")
                l_name_check = False
        except ValueError as e:
                print(f"Something went wrong: {e}\n")
    age_check = False
    while age_check is False:
        try:
            print(Fore.CYAN + "* Age:")
            age = int(input())
            age_check = True
        except ValueError:
            print(Fore.RED + "Wrong value, try again.")
    email_check = False
    while email_check is False:
        try:
            print(Fore.CYAN + "* Email:")
            email = input()
            if "@" in email:
                email_check = True
            else:
                print(Fore.RED + "Email must contain @")
                email_check = False
        except ValueError:
            print(Fore.RED + f"Incorrect email, try again.")
            print(Fore.RED + "Email must contain @")
    first_name = f_name.capitalize()
    last_name = l_name.capitalize()
    print("\n***** The following information was entered: *****")
    print("\n")
    print(f"Type: {type_lower}")
    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"\n")
    player_data = [first_name, last_name, age, email]
    print(Fore.GREEN + "Adding player to list...\n")
    if type_lower == "player":
        score_int = 0
        player_data.append(score_int)
        players_sheet.append_row(player_data)
        print(f"{first_name} {last_name} added to {type_lower} list!\n\n")
    elif type_lower == "admin":
        admins_sheet.append_row(player_data)
        print(f"{first_name} {last_name} added to {type_lower} list!\n\n")
    else:
        print("Something went wrong, please try again.\n")
        new_player()


def delete_player(type):
    """
    Deletes player based on choice from player list
    If there are no players, user is reverted back to main menu
    """
    show_players('players')
    player_count = count_players('players')
    del_player = False
    print("* Note: To go back to main menu, enter 0 and press enter *\n")
    while del_player is False:
        try:
            choice = int(input("Enter number for the player you wish to delete:\n"))
            if choice == 0:
                main()
            elif choice < 1:
                print(Fore.RED + "Negative numbers are not allowed. Try again")
            elif choice > player_count:
                print(Fore.RED + "Input is larger than number of players.\nTry again. ")
                del_player = False
            else:
                del_player = True
        except ValueError:
            print(Fore.RED + "Not a valid choice, try again")

    print(f"*** Deleting selected player... ***\n")
    choice += 1
    SHEET.worksheet('players').delete_rows(choice)
    print(f"Successfully deleted player from game!\n")


def main():
    print(Back.BLUE + f"\n\n*** Welcome to player database control center ***\n" + Style.RESET_ALL + "\n")
    main_menu()

if __name__ == "__main__":
    main()
