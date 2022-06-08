from ntpath import join
from posixpath import split
from turtle import clear
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
#defining variable players_sheet to fetch data from players sheet
admins_sheet = SHEET.worksheet('admins')
#defining variable players_sheet to fetch data from admins sheet

players = players_sheet.get_all_values() #gets all values from players sheet
admins = admins_sheet.get_all_values() #gets all values from admin sheet
#print(players)
#print(admins)


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
        
        print(f"\\\ *** Main menu *** ///\n")

        print(f"1: Create new Player")
        print(f"2: Delete player")
        print(f"3: Update Player Score")
        print(f"4: Show Player list")
        print(f"5: Show Admin List")
        print(f"6: Exit program")
        print("\n")
        menu_num = int(input("Enter a number below: \n"))
        if menu_num == 1:
            new_player()
        elif menu_num == 4: 
            show_players('players')
        elif menu_num == 5:
            show_players('admins')
        elif menu_num == 6: 
            return False
        else: 
            return True




def show_players(type):
    """
    Gets players or admins from sheet
    """
    print(f"\n*** Getting {type} from worksheet... ***\n")
    data = SHEET.worksheet(type).get_all_values()[1:]
    i = 1
    for x in data:
        name = f"Player {i}: \t{x[0]} {x[1]}"
        print(name)
        if type == "players": 
            points = f"Score: {x[4]} pts"
            print(f"\t\tPoints: {points}")
            print(f"\t\t---------------------")
        i+=1
    print(f"\n *** End of player list *** \n")
    return True

    #names = []
    #for x in range(0,2):
    #    names.append(data[x])
    #name_string = ' '.join(names)
    #print(name_string)

"""
    list_col = SHEET.worksheet(type).col_values(1)
    for i in range(1,len(list_col)):
        print(f"{i}: {list_col[i]}")
"""        

def update_score(player, score):
    """
    Updates score for a certain player
    """

    data = SHEET.worksheet(type).get_all_values()[1:]
    i = 1
    for x in data:
        points = {x[4]}
        name = f"Player {i}: {x[0]} {x[1]} \nPoints: {points}\n"
        print(name)
        i+=1
        print("*** Updating points for " + name + "***\n")
        if SHEET.worksheet(type).update(f'E{i}', 3):
            print("*** Points updated successfully! ***\n")


def validate_data(type, data):
    """
    Validates a certain type of data based on what type it is
    Numbers ar checked for int type
    Strings are checked for str type
    """

def new_player():
    """
    Creates a new instance of regular player
    """
    print(f"\n***** Create a player *****")
    print(f"You must enter information about the player you wish to create.\n")
    print(f"These are the required credentials: ")
    print(f"Admin or Regular player, First name, Last name, Age and Email.\n")

    type = input("Admin or regular player?\n")
    f_name = input("First name: \n")
        # check function comes here to check if age is only str and not int
    l_name = input("Last name: \n")
        # check function comes here to check if age is only str and not int
    age = input("Age: ")
        # check function comes here to check if age is only int and not str
    email = input("Email: ")

    print("\n***** The following information was entered: *****")
    print("\n")
    print(f"Type: {type}")
    print(f"First name: {f_name}")
    print(f"Last name: {l_name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"\n")
    player_data = [f_name, l_name, age, email]
    print("Adding player to list...\n")
    if type == "players" or type == "Players" or type == "player" or type == "Player": 
        player_data = [f_name, l_name, age, email, 0]
        players_sheet.append_row(player_data)
    elif type == "Admin" or type == "admin" or type == "Admins" or type == "admins":
        admins_sheet.append_row(player_data)
    print(f"Player added to {type} list!\n\n")

def main():
    print(f"\n\n*** Welcome to player database control center ***\n\n")
    main_menu()


main()