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
    name = input("Please enter your name (optional): ")
    email = input("Please enter your email (optional): ") 
    
    titles = SHEET.worksheet("roles").col_values(1)
    for i in range( 1, len(titles)):
        print(f"{i}. {titles[i].title()}")

    while True:
        role = input("Which of these roles best describes your position, enter number 1 to 8: ")
        if validate_numeric(1,9,role):
            break
    
    while True:
        experience = input("How many years have your worked in Information Technology: ")
        if validate_numeric(1,51,experience):
            break

    while True:
        salary = input("What is your current salary: ")
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
    print(f"Updating respondents worksheet...\n")
    worksheet_to_update = SHEET.worksheet("respondents")
    worksheet_to_update.append_row(respondent) 
    print("Respondents worksheet updated successfully.\n")

def main():
    print_introduction()
    respondent = get_respondent()
    update_respondents(respondent)

main()    