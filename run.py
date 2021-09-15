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

    print("\nWelcome to the online property management app for the")
    print("Auckland, Wellington and Christchurch regions.\n")

    print("Please make a choice from the options below.\n")

    print("Type 1, 2 or 3 and press enter to make the selection.\n")
    print("1: View most recent listings")
    print("2: Add a property to the database")
    print("3: Remove a property from the database\n")


def validate_selection():

    """
    This code validates the users selection on the main menu
    """

    user_choice = int(input("Make a selection between 1 and 3: "))
    if user_choice == 1:
        display_latest_listings()
    elif user_choice == 2:
        add_reference()
    elif user_choice == 3:
        delete_listings()
    else:
        print("That is not a valid selection,")
        print("please enter a selection between 1 and 3.")


def display_latest_listings():

    """
    This code will display the 20 most recent listings when the user makes
    the selection "1" from the main menu.
    """

    rows_data = []
    global show_listings
    show_listings = rentals.get_all_values()
    for rows_data in range(1, 21):
        row = rentals.row_values(rows_data)
        print(*row)
    load_start()
    validate_selection()


def add_reference():

    """
    This code will allow the user to add a property to the database
    when the user selects "2" from the main menu.

    The user is will be prompted with entry requests for each value
    input and the function will validate each users input. Each function
    will display a request of the type of input it requries and will
    print a message to indicate if it was valid or not. Once the user
    provides valid data the functions will keep moving down the list
    until the data is uploaded to the database.
    """

    user_reference = []
    global input_reference
    input_reference = input("\nPlease enter the reference number: ")

    if len(input_reference) != 3:
        print("That is not a valid input, please try again.")
        print("Example: 1234\n")
        add_reference()
    else:
        print("That is a valid entry, thank you\n")
        add_location()


def add_location():

    """
    This function requests the property location from the user.
    """

    user_location = []
    global input_location
    input_location = input("Please enter the location: ")
    location = ["Auckland", "Wellington", "Christchurch"]

    if check_value(input_location, location):
        print("That is a valid entry, thank you\n")
        add_bedrooms()
    else:
        print("That is not a valid entry, try again")
        print("Please enter Auckland, Wellington or Christchurh\n")
        add_location()


def add_bedrooms():

    """
    This function requests how many bedrooms the property has from the user.
    The users input is also converted into an INT.
    """

    user_bedrooms = []
    global input_bedrooms
    input_bedrooms = input("Please enter the amount of bedrooms: ")
    bedrooms = ["1", "2", "3", "4", "5"]

    if check_value(input_bedrooms, bedrooms):
        print("That is a valid entry, thank you\n")
        add_parking()
    else:
        print("That is not a valid input, please try again.")
        print("Example: 1, 2, 3, 4 or 5\n")
        add_bedrooms()


def add_parking():

    """
    This function requests if the property has parking available from the user.
    """

    user_parking = []
    global input_parking
    input_parking = input("Please enter if parking is available: ")
    parking = ["Yes", "No"]

    if check_value(input_parking, parking):
        print("That is a valid entry, thank you\n")
        add_cost()
    else:
        print("That is not a valid input, please try again.")
        print("Example: Yes or No\n")
        add_parking()


def add_cost():

    """
    This function requests the property cost from the user.
    """

    user_cost = []
    global input_cost
    input_cost = input("Please enter the cost: ")
    cost = ["300", "350", "400", "450", "500", "550", "600"]

    if check_value(input_cost, cost):
        print("That is a valid entry, thank you\n")
        add_type()
    else:
        print("That is not a valid input, please try again.")
        print("Prices are in between $300 - $600\n")
        add_cost()


def add_type():

    """
    This function requests the property type from the user.
    """

    user_type = []
    global input_type
    input_type = makeCap(input("Please enter the type of rental: "))
    type = ["House", "Apartment", "Studio"]

    if check_value(input_type, type):
        print("That is a valid entry, thank you\n")
        add_listings()
    else:
        print("That is not a valid input, please try again.")
        print("Example: House, Apartment or Studio\n")
        add_type()


def makeCap(the_word):

    """
    This function used in conjuction with the add_data functions
    above makes the users inputs the correct format to update the database.
    It will capitalise the first letter of each string input regardless which
    way the user types the selections.
    """

    return the_word


def check_value(the_value, the_array):

    """
    This function used in conjuction with the add_data functions
    above checks if the values entered are valid.
    """

    if the_value in the_array:
        return True
    else:
        return False


def add_listings():

    """
    This function used in conjuction with the add_data functions
    above checks if the values entered are valid.
    """

    print("You entered: " + (input_reference) + ", " + (input_location) + ", " + str(input_bedrooms) + ", " + (input_parking) + ", " + str(input_cost) + ", " + (input_type))
    user_input = [input_reference, input_location, input_bedrooms, input_parking, input_cost, input_type]

    confirm = []
    global user_selections
    user_selections = input("\nDo you want to update the database with this new data: ")
    user_confirmation = ["Yes", "No"]

    if user_selections == ("Yes"):
        print("\nThe listing is being updated . . .\n")
        rentals.append_row(user_input)
        print("- - - Success! - - -\n")
        print("Returning to main menu . . .")
        load_start()
        validate_selection()
    elif user_selections == ("No"):
        print("\nThe listing is has not been updated\n")
        print("Returning to main menu . . .")
        load_start()
        validate_selection()
    else:
        print("\nThat is not a valid input, please try again.")
        print("Example: Yes or No\n")
        add_listings()


def delete_listings():

    """
    This code will allow the user to delete a listing from the existing list
    when the user selects "3" from the main menu.
    """

    print("Please make sure the info is correct\n")

    ref_num = input("Please enter the reference number: ")

    if len(ref_num) != 3:
        print("That is not a valid input, please try again.")
        print("Example: 123")
        delete_listings()
    else:
        print(*{ref_num})
        confirm_delete = input("Are you sure you want to delete this data: ")
        confirm = ["Yes"]

        if confirm_delete in confirm:
            print("That entry has now been deleted\n")
        else:
            print("That is not a valid input, please try again.")
            print("Example: Yes or No\n")
            delete_listings()


def main():

    """
    This code runs all the functions in the program.
    """

    load_start()
    validate_selection()

main()
