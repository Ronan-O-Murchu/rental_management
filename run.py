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

    print("\nWelcome, please make a choice from the options below.\n")
    print("Type 1, 2 or 3 and press enter to make the selection.\n")
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
    # elif user_choice == 2:
    #     add_listings()
    # elif user_choice == 3:
    #     add_listings()
    else:
        print("That is not a valid selection,")
        print("please enter a selection between 1 and 3.")
        # validate_selection()


def display_listings():

    """
    This code will display the listings when the user makes
    the selection "1" from the main menu.
    """

    rows_data = []
    display_listings = rentals.get_all_values()
    for rows_data in range(1, 11):
        row = rentals.row_values(rows_data)
        print(row)
    # load_start()
    # validate_selection()


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

    reference = input("Please enter the reference number: ")
    if len(reference) != 8:
        print("That is not a valid input, please try again.")
        print("Example: AKL-1234")
        add_listings()
    else:
        print("That is a valid entry, thank you")
        add_location()

    def add_location():
            
        input_location = input("Please enter the location: ")
        location = ["Auckland", "Wellington", "Christchurch"]
        if input_location in location:
            print("That is a valid entry, thank you")
            add_bedrooms()
        else:
            print("That is not a valid input, please try again.")
            print("Example: Auckland, Wellington or Christchurch")
            add_location()
            return(input_location)

    def add_bedrooms():
            
        input_bedrooms = input("Please enter the amount of bedrooms: ")
        bedrooms = ["1", "2", "3", "4", "5"]
        if input_bedrooms in bedrooms:
            print("That is a valid entry, thank you")
            add_parking()
        else:
            print("That is not a valid input, please try again.")
            print("Example: 1, 2, 3, 4 or 5")
            add_bedrooms()

    def add_parking():
            
        input_parking = input("Please enter if parking is available: ")
        parking = ["Yes", "No"]
        if input_parking in parking:
            print("That is a valid entry, thank you")
            add_type()
        else:
            print("That is not a valid input, please try again.")
            print("Example: Yes or No")
            add_parking()

    # def add_cost():
            
    #     input_cost = input("Please enter the cost: ")
    #     cost = 
    #     if len(location) != [8, 10, 12]:
    #         print("That is not a valid input, please try again.")
    #         print("Example: AUCKLAND")
    #         add_type()
    #     else:
    #         print("That is a valid entry, thank you")

    def add_type():
            
        input_type = input("Please enter the type of rental: ")
        type = ["House", "Apartment", "Studio"]
        if input_type in type:
            print("That is a valid entry, thank you")
            load_start()
            validate_selection()
        else:
            print("That is not a valid input, please try again.")
            print("Example: House, Apartment or Studio")
            add_type()


def delete_listings():
    
    """
    This code will allow the user to delete a listing from the existing list.
    """

    """
    Plan here is to create code to load the info from the
    top row and allow the user to delete data.
    1. The user will need to see the full row of data for each listing.
    2. The user will need to be able to select the row of data to delete.
    3. The user will need to confirm to delete the selected data.
    """
    
    print("Please make sure the info is correct\n")
    
    ref_num = input("Please enter the reference number: ")
    if len(ref_num) != 8:
        print("That is not a valid input, please try again.")
        print("Example: AKL-1234")
        add_listings()
    else:
        print("That is a valid entry, thank you")
        load_start()
        validate_selection()


"""
This code runs all the functions in the program.
"""

load_start()
validate_selection()
