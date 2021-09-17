"""
This code was referenced from the CI "Love Sandwiches" project
for the import and scope syntax.
"""

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


def make_selection():

    """
    This code validates the users selection on the main menu
    """

    print("\nPlease make a choice from the options below.\n")

    print("1: View most recent listings")
    print("2: Add a property to the database")
    print("3: Remove a property from the database\n")

    user_choice = int(input("Make a selection between 1 and 3:\n"))
    if user_choice == 1:
        display_listings()
    elif user_choice == 2:
        add_reference()
    elif user_choice == 3:
        display_delete_list()
        delete_listings()
    else:
        print("\nThat is not a valid selection,")
        print("now exiting the app.\n")


def display_listings():

    """
    This code will display the listings when the user makes
    the selection "1" from the main menu.
    """
    i = 0
    rows_data = []
    global show_listings
    show_listings = rentals.get_all_values()
    for rows_data in reversed(range(len(show_listings), 0, -1)):
        i += 1
        row = rentals.row_values(rows_data)
        row.insert(0, i)
        print(*row)
    make_selection()


def display_delete_list():

    """
    This code will display the listings when the user makes
    the selection "1" from the main menu.
    """
    i = 0
    rows_data = []
    global show_listings
    show_listings = rentals.get_all_values()
    for rows_data in reversed(range(len(show_listings), 0, -1)):
        i += 1
        row = rentals.row_values(rows_data)
        row.insert(0, i)
        print(*row)


def check_value(the_value, the_array):

    """
    This function used in conjuction with the add_data functions
    above checks if the values entered are valid.
    """

    if the_value in the_array:
        return True
    else:
        return False


def makeCap(the_word):

    """
    This function used in conjuction with the add_data functions
    above makes the users inputs the correct format to update the database.
    It will capitalise the first letter of each string input regardless which
    way the user types the selections.
    """

    cap_the_word = the_word.capitalize()
    return cap_the_word


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
    print("Example: 123, ABC, A01 and then press enter.\n")
    user_reference = []
    global input_reference
    input_reference = input("Enter the data here:\n")

    if len(input_reference) != 3:
        print("\nThat is not a valid input, please try again.")
        add_reference()
    else:
        print("That is a valid entry, thank you\n")
        add_location()


def add_location():

    """
    This function requests the property location from the user.
    """

    print("Please enter the lcoation of the property.")
    print("Listings are only located in")
    print("Auckland, Wellington or Christchurch.\n"")
    user_location = []
    global input_location
    input_location = makeCap(input("Enter the data here:\n"))
    location = ["Auckland", "Wellington", "Christchurch"]

    if check_value(input_location, location):
        print("That is a valid entry, thank you\n")
        add_bedrooms()
    else:
        print("\nThat is not a valid input, please try again.\n")
        add_location()


def add_bedrooms():

    """
    This function requests how many bedrooms the property has from the user.
    The users input is also converted into an INT.
    """

    print("Please enter the ammount of bedrooms in the property.")
    print("The bedrooms range from 1-5 bedrooms.\n")
    user_bedrooms = []
    global input_bedrooms
    input_bedrooms = int(input("Enter the data here:\n"))

    if 1 <= input_bedrooms <= 5:
        print("That is a valid entry, thank you\n")
        add_parking()
    else:
        print("\nThat is not a valid input, please try again.\n")
        add_bedrooms()


def add_parking():

    """
    This function requests if the property has parking available from the user.
    """

    print("Please enter if parking is available at the property")
    print("by typing Yes or No and then pressing enter.\n")
    user_parking = []
    global input_parking
    input_parking = makeCap(input("Enter the data here:\n"))
    parking = ["Yes", "No"]

    if check_value(input_parking, parking):
        print("That is a valid entry, thank you\n")
        add_cost()
    else:
        print("\nThat is not a valid input, please try again.\n")
        add_parking()


def add_cost():

    """
    This function requests the property cost from the user.
    """

    print("Please enter the rental price for the property.")
    print("Prices are in between $300 - $1000\n")
    user_cost = []
    global input_cost
    input_cost = int(input("Enter the data here:\n"))

    if 300 <= input_cost <= 1000:
        print("That is a valid entry, thank you\n")
        add_type()
    else:
        print("\nThat is not a valid input, please try again.\n")
        add_cost()


def add_type():

    """
    This function requests the property type from the user.
    """

    print("Please enter the type of property this is.")
    print("Example: House, Apartment or Studio.\n")
    user_type = []
    global input_type
    input_type = makeCap(input("Enter the data here:\n"))
    type = ["House", "Apartment", "Studio"]

    if check_value(input_type, type):
        print("That is a valid entry, thank you\n")
        add_availability()
    else:
        print("\nThat is not a valid input, please try again.\n")
        add_type()


def add_availability():

    """
    This function requests data from the user to determine
    if this property is occupied or not.
    """

    print("Please enter if this property is currently available.")
    print("Example: Available or Occupied.\n")
    user_type = []
    global input_availability
    input_availability = makeCap(input("Enter the data here:\n"))
    available = ["Available", "Occupied"]

    if check_value(input_availability, available):
        print("That is a valid entry, thank you\n")
        add_listings()
    else:
        print("\nThat is not a valid input, please try again.\n")
        add_availability()


def add_listings():

    """
    This function used in conjuction with the add_data functions
    above checks if the values entered are valid.
    """

    print("You entered: " + str(input_reference) + ", " +
          str(input_location) + ", " + str(input_bedrooms) + ", " +
          str(input_parking) + ", " + str(input_cost) + ", " +
          str(input_type) + ", " + str(input_availability))
    user_input = [input_reference, input_location,
                  str(input_bedrooms), input_parking,
                  str(input_cost), input_type, input_availability]

    confirm = []
    global user_selections
    user_selections = makeCap(input("\nDo you want to update the"
                              "database with this new data:\n"))
    user_confirmation = ["Yes", "No"]

    if user_selections == ("Yes"):
        print("\nThe listing is being updated . . .\n")
        rentals.append_row(user_input)
        print("- - - Success! - - -\n")
        print("Returning to main menu . . .")
        make_selection()
    elif user_selections == ("No"):
        print("\nThe listing is has not been updated\n")
        print("Returning to main menu . . .")
        make_selection()
    else:
        print("\nThat is not a valid input, please try again.")
        print("Example: Yes or No\n")
        add_listings()


def delete_listings():

    """
    This code will allow the user to delete a listing from the existing list
    when the user selects "3" from the main menu.
    """

    print("\nPlease enter the row number you wish to delete.\n")
    print("Please make sure the info is correct\n")

    ref_num = input("Enter the data here:\n")
    cell_data_list = rentals.findall(ref_num)
    print("You have selected: " + str(rentals.row_values(ref_num)) + "\n")
    confirm_delete = makeCap(input("Are you sure you want"
                             "to delete this listing?:\n"))
    user_confirmation = ["Yes", "No"]

    if confirm_delete == ("Yes"):
        print("That entry has now been deleted\n")
        rentals.delete_rows(int(ref_num))
        make_selection()
    elif confirm_delete == ("No"):
        print("\nThat entry has not been deleted\n")
        print("Returning to main menu . . . \n")
        make_selection()
    else:
        print("\nThat is not a valid input, please try again.")
        delete_listings()


def main():

    """
    This code runs all the functions in the program.
    """

    load_start()
    make_selection()

main()
