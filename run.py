import gspread
from google.oauth2.service_account import Credentials
# Python program to validate an Email
 
# import re module
 
# re module provides support
# for regular expressions
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) 
SHEET = GSPREAD_CLIENT.open('employment_survey')

def print_introduction():
    """
    Print a Welcome message at the start of the survey
    """
    print("Welcome to the Information Technology Salary Survey\n")
    print("Thank you for participating, please enter your details below\n")
    return

def get_respondent():
    """
    Get survey respondents name, email, role and years experience
    """
    name = input("\nPlease enter your name (optional): ")
    email = input("\nPlease enter your email (optional): ") 
    
    print("\nWhich of these roles best describes your position\n") 
    titles = SHEET.worksheet("roles").col_values(1)
    for i in range( 1, len(titles)):
        print(f"       {i}. {titles[i].title()}")

    while True:
        role = input("\nEnter number 1 to 8: ")
        if validate_numeric(1,9,role):
            break
    
    while True:
        experience = input("\nHow many years have your worked in Information Technology: ")
        if validate_numeric(1,51,experience):
            break

    while True:
        salary = input("\nWhat is your current salary: ")
        if validate_numeric(10000,500001,salary):
            break    

    return name,email,role,experience,salary


def validate_numeric(start,end,value):
    """
    Inside the try, check valid integer raised and if valid range. Raises
    ValueError.
    """
    try:
        number = int(value)    
        if start and number not in range(start,end):
            raise ValueError(
                f"You must choose a number between {start} and {end - 1}"
            ) 
    except ValueError as e:
        print(f"{e}! Please try again ...\n")
        return False  

    return True    

def update_respondents(respondent):
    """
    Update worksheet, add new row with the list provided
    """
    print("\nUpdating respondents worksheet...\n")
    worksheet_to_update = SHEET.worksheet("respondents")
    worksheet_to_update.append_row(respondent) 
    print("Respondents worksheet updated successfully.\n")

def menu(respondent):
    print(get_menu_text())
    choice = get_menu_choice()
    process_menu_choice(choice,respondent) 

def get_menu_choice():
    first_menu_option = 1
    last_plus_one_menu_option = 8
    
    while True:
        choice = input("Please select option: ")
        if validate_numeric(first_menu_option,last_plus_one_menu_option,choice):
            break 

    return choice  

def process_menu_choice(choice, respondent):
    if choice == "1":
        print("Report " + choice)
    elif choice == "2":
        print("Report " + choice)
    elif choice == "3":
        print("Report " + choice)
    elif choice == "4":
        print("Report " + choice)
    elif choice == "5":
        print("Report " + choice)
    elif choice == "6":
        print("Report " + choice)
    else:
        print("Exit") 
      

          

def get_menu_text():
    
    menu_text = """
What would you like to do now:
        1. Compare your salary to other respondents in terms of role
        2. Compare your salary to other respondents in terms of experience
        3. Compare your salary to other respondents in terms of role AND experience
        4. Compare your salary in terms of role
        5. Compare your salary in terms of experience
        6. Compare your salary in terms of role AND experience
        7. Exit
        
        """
    
    return menu_text 


def main():
    print_introduction()
    respondent = get_respondent()
    update_respondents(respondent)
    menu(respondent)

main()    