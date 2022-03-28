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
    name = input("Please enter your name: ")
    email = input("Please enter your email: ")
    roles = SHEET.worksheet("roles").col_values(1)
    for i = 1 to len(roles):
        print(f"{i}. {roles[i]})
        
    #print("1. Frontend Developer\n")
    #print("2. Backend Developer\n")
    #print("3. Full Stack Developer\n")
    #print("4. Senior Frontend Developer\n")
    #print("5. Senior Backend Developer\n")
    #print("6. Senior Full Stack Developer\n")
    #print("7. Technical Lead\n")
    #print("8. Head of Engineering\n")
    job = input("Which of these roles best describes your position: ")
    experience = input("How many years have your worked in Information Technology: ")
    return name,email,job,experience


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