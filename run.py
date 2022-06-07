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
admin_sheet = SHEET.worksheet('admin')

players = players_sheet.get_all_values()
admins = admin_sheet.get_all_values()
print(players)
print(admins)

def show_players(type):
    """
    Gets players or admins from sheet
    """


def new_player():
    """
    Creates a new instance of regular player
    """
    print("\n***** Enter a player name: *****")
    f_name = input("\nFirst name: ")
        # check function comes here to check if age is only str and not int
    l_name = input("Last name: ")
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


def main():
    print("hello terminal")
    new_player()


#main()