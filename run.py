# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


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


main()