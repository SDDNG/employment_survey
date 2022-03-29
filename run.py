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
    Inside the try, check valid integer raised and if so within valid range. Raises
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
    Update worksheet, add new row with the respondent filled in
    """
    print("\nUpdating respondents worksheet...\n")
    worksheet_to_update = SHEET.worksheet("respondents")
    worksheet_to_update.append_row(respondent) 
    print("Respondents worksheet updated successfully.\n")

def menu(respondent):
    """
    Print the user menu and ask the user to choose an option
    """

    menu_text = """
What would you like to do now:
        1. Compare the respondent's salary to other respondents in terms of role
        2. Compare the respondent's salary to other respondents in terms of experience
        3. Compare the respondent's salary to other respondents 
        4. Compare the respondent's salary in terms of role nationally
        5. Compare the respondent's salary in terms of experience nationally
        6. Compare the respondent's salary nationally
        7. Exit
        
        """
    choice = None
    while choice != "7":
        print(menu_text)
        choice = get_menu_choice()
        process_menu_choice(choice,respondent) 


def get_menu_choice():
    """
    Validate the menu option the user choose and return if valid
    """
    first_menu_option = 1
    last_plus_one_menu_option = 8
    
    while True:
        choice = input("Please select option: ")
        if validate_numeric(first_menu_option,last_plus_one_menu_option,choice):
            break 

    return choice  

def process_menu_choice(choice, respondent):
    """
    Execute the appropriate function based on the user's choice 
    """
    if choice == "1":
        compare_respondents_to_other_respondents("role",respondent)
    elif choice == "2":
        compare_respondents_to_other_respondents("experience",respondent)
    elif choice == "3":
        compare_respondents_to_other_respondents(None,respondent)
    elif choice == "4":
        print("Report " + choice)
    elif choice == "5":
        print("Report " + choice)
    elif choice == "6":
        print("Report " + choice)
    else:
        print("Exit") 
      

def compare_respondents_to_other_respondents(comparitor,respondent):
    """
    Compares the respondent's salary to other respondents based on the comparitor passed
    i.e. role or experience 
    """
    if(check_enough_respondents(comparitor,respondent)):
        print(f"*** back to here *** comparing respondents salary to other respondents salaries based on {comparitor}")
    else:
        print(f"There are not enough other resondents with the same as {comparitor}")     
        

def check_enough_respondents(comparitor, respondent):
    """
    If there are not enough similar respondents (at least 10) to do a comparison 
    to then this function returns False. The comparitor can either be role or experience 
    """
    number_of_matching_respondents = 0
    name,email,role,experience,salary = respondent
    
    worksheet = SHEET.worksheet("respondents")

    if comparitor == "role":
        values_list = worksheet.col_values(3)
        for i in range(2,len(values_list)):
            if values_list[i] == role:
                number_of_matching_respondents += 1
    elif comparitor == "experience":
        values_list = worksheet.col_values(4)
        for i in range(2,len(values_list)):
            if values_list[i] == experience:
                number_of_matching_respondents += 1
    else:
         number_of_matching_respondents = len(worksheet.col_values(3)) - 1           

    if number_of_matching_respondents > 10:
        return True
    else:
        return False                
                    

def main():
    print_introduction()
    respondent = get_respondent()
    update_respondents(respondent)
    menu(respondent)

main()    