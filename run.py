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
SHEET = GSPREAD_CLIENT.open('rental_listings')

rentals = SHEET.worksheet('rentals')


def load_start():

    """
    This code displays the main menu and requires the
    user to make a selection in order to continue.
    """

    print("Welcome, please make a choice from the options below.")
    print("Input 1, 2 or 3 and select enter to make a selection.""\n")
    print("1: View all listings")
    print("2: Add a listing")
    print("3: Delete a listing""\n")


def validate_selection():

    """
    This code validates the users selection on the main menu
    """

    user_choice = int(input("Make a selection between 1 and 3: "))
    while user_choice in [1, 2, 3]:
        print("Thank you, that was a valid selection")
        break
    else:
        print("That is not a valid selection,")
        print("please enter a selection between 1 and 3.")
        validate_selection()

    # def view_all_listings():
    #     view_all = rentals.get_all_values()

load_start()
validate_selection()
