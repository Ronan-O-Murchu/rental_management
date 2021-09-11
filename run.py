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
    print("Input 1, 2 or 3 and select enter to make a selection.\n")
    print("1: View all listings")
    print("2: Add a listing")
    print("3: Delete a listing\n")


def validate_selection():

    """
    This code validates the users selection on the main menu
    """

    user_choice = int(input("Make a selection between 1 and 3: "))
    if user_choice == 1:
        display_listings()
    elif user_choice == 2:
        add_listings()
    elif user_choice == 3:
        add_listings()
    else:
        print("That is not a valid selection,")
        print("please enter a selection between 1 and 3.")
        validate_selection()


def display_listings():

    """
    This code will display the listings when the user makes
    the selection "1" from the main menu.
    """

    display_listings = rentals.get_all_values()
    print(display_listings)


def add_listings():

    """
    This code will allow the user to add a listing to the list.
    """

    """
    Plan here is to create code to load the info from the
    top row and have the user input data.
    1. The user will need to input data for each section.
    2. The data will need to be validated.
    3. The data will all need to be stored and displayed together
    before submission.
    4. The user will need to confirm the info to add to the database.
    """

    print("Please make sure info is correct")
    ref = int(input("Please enter the reference number: "))
    if len(ref) != 8:
        print("That is not a valid input, please try again.")
        print("Example: AKL-1234")
    else:
        print("That is a valid entry, thank you")


load_start()
validate_selection()
