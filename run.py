from ntpath import join
from posixpath import split
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
admin_sheet = SHEET.worksheet('admins')
#defining variable players_sheet to fetch data from admins sheet

players = players_sheet.get_all_values() #gets all values from players sheet
admins = admin_sheet.get_all_values() #gets all values from admin sheet
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
    """

def show_players(type):
    """
    Gets players or admins from sheet
    """
    
    data = SHEET.worksheet(type).get_all_values()[1:]
    i = 1
    for x in data:
        name = f"Player {i}: {x[0]} {x[1]}"
        print(name)
        i+=1


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


def validate_data(type, data):
    """
    Validates a certain type of data based on what type it is
    Numbers ar checked for int type
    Strings are checked for str type
    """
    #if type == "text"
    #print("Enter")


def new_player():
    """
    Creates a new instance of regular player
    """
    print("***** Create a player *****")
    print("You must enter information about the player you wish to create.\n")
    print("These are the required credentials: ")
    print("Admin or Regular player, First name, Last name, Age and Email.\n")

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
    print(f"First name: {f_name}")
    print(f"Last name: {l_name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"\n")
    player_data = [f_name, l_name, age, email]
    print("Adding player to list...\n")
    players_sheet.append_row(player_data)
    print("Player added to list!")



def main():
    print("*** Welcome to player database control center ***\n\n")
    new_player()


#main()
show_players("players")