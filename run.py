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
    print("Auckland, Wellington and Christchurch regions.")


def validate_selection():

    """
    This code validates the users selection on the main menu
    """

    print("\nPlease make a choice from the options below.\n")

    print("1: View most recent listings")
    print("2: Add a property to the database")
    print("3: Remove a property from the database\n")

    user_choice = int(input("Make a selection between 1 and 3:\n"))
    if user_choice == 1:
        display_latest_listings()
    elif user_choice == 2:
        add_reference()
    elif user_choice == 3:
        delete_listings()
    else:
        print("\nThat is not a valid selection,")
        print("please enter a selection between 1 and 3.")


def display_latest_listings():

    """
    This code will display the 10 most recent listings when the user makes
    the selection "1" from the main menu.
    """

    rows_data = []
    global show_listings
    show_listings = rentals.get_all_values()
    for rows_data in range(2, 11):
        row = rentals.row_values(rows_data)
        print(*row)
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

    print("\nPlease enter the 3 character reference code for the property.")
    print("Example: 123, ABC, A01 and then press enter\n")
    user_reference = []
    global input_reference
    input_reference = input("Enter the data here:\n")

    if len(input_reference) != 3:
        print("\nThat is not a valid input, please try again.")
        print("Example: 123, ABC, A01\n")
        add_reference()
    else:
        print("That is a valid entry, thank you\n")
        add_location()


def add_location():

    """
    This function requests the property location from the user.
    """

    print("Please enter the lcoation either")
    print("Auckland, Wellington or Christchurch\n")
    user_location = []
    global input_location
    input_location = input("Enter the data here:\n")
    location = ["Auckland", "Wellington", "Christchurch"]

    if check_value(input_location, location):
        print("That is a valid entry, thank you\n")
        add_bedrooms()
    else:
        print("\nThat is not a valid input, please try again.")
        print("Please enter Auckland, Wellington or Christchurh\n")
        add_location()


def add_bedrooms():

    """
    This function requests how many bedrooms the property has from the user.
    The users input is also converted into an INT.
    """

    print("Please enter the ammount of bedrooms in the property.")
    print("The bedrooms range from 1-5\n")
    user_bedrooms = []
    global input_bedrooms
    input_bedrooms = int(input("Enter the data here:\n"))

    if 1 <= input_bedrooms <= 5:
        print("That is a valid entry, thank you\n")
        add_parking()
    else:
        print("\nThat is not a valid input, please try again.")
        print("Example: 1, 2, 3, 4 or 5\n")
        add_bedrooms()


def add_parking():

    """
    This function requests if the property has parking available from the user.
    """

    print("Please enter if parking is available at the property")
    print("by typing Yes or No and then pressing enter.\n")
    user_parking = []
    global input_parking
    input_parking = input("Enter the data here:\n")
    parking = ["Yes", "No"]

    if check_value(input_parking, parking):
        print("That is a valid entry, thank you\n")
        add_cost()
    else:
        print("\nThat is not a valid input, please try again.")
        print("Example: Yes or No\n")
        add_parking()


def add_cost():

    """
    This function requests the property cost from the user.
    """

    print("Please enter the rental price for the property.\n")
    user_cost = []
    global input_cost
    input_cost = int(input("Enter the data here:\n"))

    if 300 <= input_cost <= 1000:
        print("That is a valid entry, thank you\n")
        add_type()
    else:
        print("\nThat is not a valid input, please try again.")
        print("Prices are in between $300 - $1000\n")
        add_cost()


def add_type():

    """
    This function requests the property type from the user.
    """

    print("Please enter the type of property this is.")
    print("Example: Please type House, Apartment or Studio and press enter\n")
    user_type = []
    global input_type
    input_type = input("Enter the data here:\n")
    type = ["House", "Apartment", "Studio"]

    if check_value(input_type, type):
        print("That is a valid entry, thank you\n")
        add_availability()
    else:
        print("\nThat is not a valid input, please try again.")
        print("Example: House, Apartment or Studio\n")
        add_type()


def add_availability():

    """
    This function requests data from the user to determine
    if this property is occupied or not.
    """

    print("Please enter if this property is currently available.")
    print("Example: Please type Available or Occupied and press enter\n")
    user_type = []
    global input_availability
    input_availability = makeCap(input("Enter the data here:\n"))
    available = ["Available", "Occupied"]

    if check_value(input_availability, available):
        print("That is a valid entry, thank you\n")
        add_listings()
    else:
        print("\nThat is not a valid input, please try again.")
        print("Example: Please type Available or Occupied and press enter\n")
        add_availability()


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

    print("You entered: " + str(input_reference) + ", " + str(input_location) + ", " + str(input_bedrooms) + ", " + str(input_parking) + ", " + str(input_cost) + ", " + str(input_type) + ", " + str(input_availability))
    user_input = [input_reference, input_location, str(input_bedrooms), input_parking, str(input_cost), input_type, input_availability]

    confirm = []
    global user_selections
    user_selections = input("\nDo you want to update the database with this new data:\n")
    user_confirmation = ["Yes", "No"]

    if user_selections == ("Yes"):
        print("\nThe listing is being updated . . .\n")
        rentals.append_row(user_input)
        print("- - - Success! - - -\n")
        print("Returning to main menu . . .")
        validate_selection()
    elif user_selections == ("No"):
        print("\nThe listing is has not been updated\n")
        print("Returning to main menu . . .")
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

    print("Please enter the 3 character reference code for the property to delete.")
    print("Example: 123, ABC, A01 and then press enter\n")
    print("Please make sure the info is correct\n")

    ref_num = input("Enter the data here: ")

    if len(ref_num) != 3:
        rentals.pop_row(ref_num)
        print("\nThat is not a valid input, please try again.")
        print("Example: 123, ABC, A01")
        delete_listings()
    else:
        print(*{ref_num})
        confirm_delete = input("Are you sure you want to delete this data:\n")
        confirm = ["Yes"]

        if check_value(confirm_delete, confirm):
            print("That entry has now been deleted\n")
        else:
            print("\nThat is not a valid input, please try again.")
            print("Example: Yes or No\n")
            delete_listings()


def main():

    """
    This code runs all the functions in the program.
    """

    load_start()
    validate_selection()

main()

# add_type()
