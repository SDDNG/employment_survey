import gspread
from google.oauth2.service_account import Credentials

# import "re" module to validate emails if entered
import re

# import "os" module to clear screen 
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) 
SHEET = GSPREAD_CLIENT.open('employment_survey')

"""
This program accepts user input as part of a salary survey. The respondent can optionally provide 
name and email, and must provide role (from a list of defined roles), experience in terms of years
and salary. Once the respondents response has been registerd they are provided the option to compare
their salary to other respondents or to national results. In both categories, respondents can 
compare in terms of role, experience or all others

"""

def print_introduction():
    """
    Print a Welcome message at the start of the survey
    """
    # clear the screen
    clearConsole()
    print("\nWelcome to the Information Technology Salary Survey\n")
    print("Thank you for participating, please enter your details below\n")
    return

def clearConsole():
    """
    Clears the terminal screen
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def get_respondent():
    """
    Get survey respondents name, email, role and years experience
    """
    name = input("\nPlease enter your name (optional): ")

    while True:
        email = input("\nPlease enter your email (optional): ")
        # an email address is not mndatory but if one has been specified then it must be valid
        if email_validate(email) or email == "":
            break 
    
    print("\nWhich of these roles best describes your position: \n") 
    # Presents a list of roles retrieved from a reference sheet in the Google sheet where
    # the respondents results will be stored
    titles = SHEET.worksheet("roles").col_values(1)
    for i in range( 1, len(titles)):
        print(f"       {i}. {titles[i].title()}")

    while True:
        # there are eight valid roles
        role = input("\nEnter number 1 to 8: ")
        if validate_numeric(1,9,role):
            break
    
    while True:
        experience = input("\nHow many years have you worked in Information Technology: ")
        # a respondent must have worked at least one year and not more than 50 years
        if validate_numeric(1,51,experience):
            break

    while True:
        salary = input("\nWhat is your current salary in euros: ")
        # valid salaries are between 10,000 and 500,000 euros
        if validate_numeric(10000,500001,salary):
            break    
    # when all data is valid return the respondent        
    return name,email,role,experience,salary

def email_validate(email_entered):
    """
    function to validate email addresses entered have correct format
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email_entered)):
        # email is a valid format
        return True

    # email is not a valid format
    print("\n        Error: If you specify an email, it must have a valid format!")
    return False


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
    Print the report menu and ask the user to choose an option. The details of the respondent 
    entered are passed to this report menu
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
    # the menu will continue to be presented after a report is chosen until 'Exit is chosen'
    while choice != "7":
        print(menu_text)
        # validate that the option chosen is valid and store it
        choice = get_menu_choice()
        # pass the report option and details of the respondent entered to a function which
        # will validate the report choice in terms of whether there is enough data to run and, if so,
        # to subsequently run the relevant report 
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
    Execute the appropriate function based on the user's choice of report
    """
    if choice == "1":
        # the function called compares the salary of respondent passed to those of other repsondents with the same role 
        compare_respondent_to_other_respondents("role",respondent)
    elif choice == "2":
        # the function called compares the salary of respondent passed to those of other respondents with the same or similar experience
        compare_respondent_to_other_respondents("experience",respondent)
    elif choice == "3":
        # the function called will compare the salary of respondent passed to those of all other repsondents
        compare_respondent_to_other_respondents(None,respondent)
    elif choice == "4":
        # the function called compares the salary of respondent passed to those nationally with the same role
        compare_respondent_nationally("role", respondent)
    elif choice == "5":
        # the function called compares the salary of respondent passed to those nationally with the same or similar experience
        compare_respondent_nationally_experience(respondent)
    elif choice == "6":
        # the function called will compare the salary of respondent passed to others in the IT sector nationally
        compare_respondent_nationally(None, respondent)
    else:
        # exit
        print("\nExiting survey ........\n\n") 
      

def compare_respondent_to_other_respondents(comparitor,respondent):
    """
    Compares the respondent's salary to other respondents based on the comparitor passed i.e. role or experience or if no 
    comparitor is passed then the respondent is compared to all other respondents
    """

    # first a function is called to check there are enough qualifying respondents to compare to the respondent in question
    if(check_enough_respondents(comparitor,respondent)):
        # if there are enough qualifying respondents to compare to the respondent in question, a function to display the comparison
        # is called
        display_respondent_to_other_respondents_report(comparitor,respondent)
    else:
        # if there are not enough qualifying respondents, the user is informed whereupon they are immediately returned to the report menu
        print(f"There are not enough other respondents with the same or similar {comparitor}")     
        
def check_enough_respondents(comparitor, respondent):
    """
    If there are not enough similar respondents (at least 10) to do a comparison to then this function returns False. 
    The comparitor can either be role or experience or None, if it's None then there just have to be 10 other respondents in total 
    """
    number_of_matching_respondents = 0
    name,email,role,experience,salary = respondent
    
    # retrieve all of the respondents
    worksheet = SHEET.worksheet("respondents")

    
    if comparitor == "role":
        # if the comparitor passed is 'role' then the roles of all of the respondents are checked to see if they match the role of the 
        # respondent who was passed and if they do, a counter is incremented
        values_list = worksheet.col_values(3)
        for i in range(1,len(values_list)):
            if values_list[i] == role:
                number_of_matching_respondents += 1
    elif comparitor == "experience":
        # if the comparitor passed is 'experience' then the experience of all of the respondents are checked to see if they 
        # have a similar amount of experience, i.e. plus or minus a year, to the experience of the respondent who was passed and 
        # if they do, a counter is incremented
        values_list = worksheet.col_values(4)
        for i in range(1,len(values_list)):
            if int(values_list[i]) in range(int(experience) - 1, int(experience) + 2):
                number_of_matching_respondents += 1
    else:
        # if the comparitor passed is not 'role' or 'experience' then it must be None which means the user chose to compare the 
        # respondent to all other respondents, so the number of all respondents is stored
         number_of_matching_respondents = len(worksheet.col_values(3)) - 1           

    # There must be 10 other matching respondents, as the respondent passed is also in the speadsheet, the number of matches must be 
    # greater than 10        
    if number_of_matching_respondents > 10:
        return True
    else:
        return False 

def display_respondent_to_other_respondents_report(comparitor,respondent):
    """
    This function is called if the user has chosen to compare the salary of the respondent in question with other respondents, on 
    the basis of role, experience or simply all other respondents. 
    """

    # the details of the respondent passed are stored in relevant variables
    name,email,role,experience,salary = respondent
    
    # the worksheet with all of the respondents' details is retrieved and then the salaries of all respondents placed in a variable
    worksheet = SHEET.worksheet("respondents")
    salaries_list = worksheet.col_values(5)

    # if a comparitor is passed i.e. it is not None, then it will be "role" or "experience", the details of role or experience of the 
    # respondents is then placed in a variable
    if comparitor == "role":
        values_list = worksheet.col_values(3)
    elif comparitor == "experience":
        values_list = worksheet.col_values(4)

    # the salary of the respondent passed is converted to an interger for comparison purposes
    numeric_of_salary = int(salary)

    # the top salary and bottom salary are set to the salary of the respondent passed and a number of salary counters are initialised
    top_salary = numeric_of_salary
    bottom_salary = numeric_of_salary
    salaries_above = 0
    salaries_below = 0
    salaries_same = 0
    number_of_matching_respondents = 0

    # read through all of the respondents' salaries
    for i in range(1,len(salaries_list)):
        # if a comparitor has not been passed, go straight to counting the other respondents and storing details about their salaries,
        # otherwise if a comparitor was passed, it must be 'role' or 'experience', if it was 'role' then only those with the same role
        # will be counted and their details analysed, if the comparitor passed was 'experience' then only other respondents within a 
        # year or experience either way will be counted and their details analysed 
        if ((comparitor == None) or 
            (comparitor == "role" and values_list[i] == role) or 
            (comparitor == "experience" and 
            (int(values_list[i]) in range(int(experience) - 1, int(experience) + 2)))):
            # increment the number of matching respondents
            number_of_matching_respondents += 1
            # store whether the salary of the respondent is greater than, less than or the same as the respondent passed
            if int(salaries_list[i]) > numeric_of_salary:
                salaries_above += 1
            elif int(salaries_list[i]) < numeric_of_salary:
                salaries_below += 1
            else:
                salaries_same += 1

            # store the top and bottom salary from the respondents
            if int(salaries_list[i]) > top_salary:
                top_salary = int(salaries_list[i])
            elif int(salaries_list[i]) < bottom_salary:
                bottom_salary = int(salaries_list[i])

    # retrieve the title corresponding to the role of the respondent in question
    titles = SHEET.worksheet("roles").col_values(1)
    title = titles[int(role)].title()           

    print(f"\nThe respondent in question has a role of {title}, experience of {experience} years and a salary of {'€{:,}'.format(numeric_of_salary)}.")
    
    # give the total of matching respondents, taking 1 away as the respondent passed is also in the list of respondents so they are not
    # a match
    if comparitor == None:
         print(f"\n   There were {number_of_matching_respondents - 1} other respondents in total:\n")
    else:
         print(f"\n   There were {number_of_matching_respondents -1} respondents with the same or similar {comparitor}:\n")

    if salaries_above != 0:
        print(f"      Of those {salaries_above} had a higher salary than the respondent.\n")
    if salaries_above != 0:
        print(f"      Of those {salaries_below} had a lower salary than the respondent.\n")
    if (salaries_same - 1) != 0:
        print(f"      Of those {salaries_same -1} had the same salary as the respondent.\n")
     
    print(f"      The greatest salary was {'€{:,}'.format(top_salary)}.\n")
     
    print(f"      The lowest salary was {'€{:,}'.format(bottom_salary)}.\n\n")                            
                    

def compare_respondent_nationally(comparitor, respondent):
    """
    This function is called if the user has chosen to compare the salary of the respondent with national figures, on the basis 
    of role or to all of the IT sector nationally. 
    """

    # the details of the respondent passed are stored in relevant variables
    name,email,role,experience,salary = respondent

    # depending on whether a comparitor was passed, open the appropriate worksheet. If the comparitor is "role", then based on the role
    # of the respondent in question, open the worksheet that contains the details for the salary quartiles or that role. If no 
    # comparitor was passed then the worksheet with the percentiles for all workers in the IT sector nationally is opened.  
    
    if comparitor == "role":
        # assume respondent is in bottom salary quartile initially, this will change if salary is found to exceed quartiles
        tile_of_respondent = "4" 
        # if the comparitor is role then the salaries are stored by quartiles and number of tiles is 4
        tile_type = "quartile"
        number_of_tiles = 4
        # set a string for insertion into report if role is a comparitor to explain the context of the quartile they land in
        role_qualifier_text = "for their role "
        # open the worksheet with details of national figures for the respondents' roles
        if int(role) in range(1,4):
            # respondent is a developer
            worksheet = SHEET.worksheet("developer")
        elif int(role) in range(4,7):
            # respondent is a senior developer
            worksheet = SHEET.worksheet("senior_developer")
        elif int(role) == 7:
            # respondent is a technical lead
            worksheet = SHEET.worksheet("tech_lead")
        else:
            # respondent is a head of engineering
            worksheet = SHEET.worksheet("head_engineering")
    else:
        # assume respondent is in bottom salary percentile initially, this will change if salary is found to exceed percentiles
        tile_of_respondent = "100" 
        # if no comparitor passed then a national comparison to all IT is required and the salaries are stored by percentiles  
        # and number of tiles is 100
        tile_type = "percentile"
        number_of_tiles = 100
        # if role is not being used as a comparitor set the role qualifier text to an empty string as their is no qualifier
        role_qualifier_text = ""
        # get salary percentiles for entire IT sector nationally
        worksheet = SHEET.worksheet("national")

    # get the salary floors and corresponding quartiles/percetiles
    salaries = worksheet.col_values(1)
    tiles = worksheet.col_values(2)

    # the salary of the respondent passed is converted to an interger for comparison purposes
    numeric_of_salary = int(salary)
    
    # read through all of the salary quartiles/percentiles
    # note 'number_of_tiles' used here for range rather than length of column to avoid possibility of junk in spreadsheet rows  
    for i in range(1,(number_of_tiles + 1)):
        if int(salaries[i]) < numeric_of_salary:
            tile_of_respondent = tiles[i]

    # retrieve the title corresponding to the role of the respondent in question
    titles = SHEET.worksheet("roles").col_values(1)
    title = titles[int(role)].title()           

    # Print details of the respondent being compared
    print(f"\nThe respondent in question has a role of {title}, experience of {experience} years and a salary of {'€{:,}'.format(numeric_of_salary)} euros.")

    # Specify which quartile or percentile (depending on the comparison) they fall into in terms of salary 
    print(f"\n      They are in {tile_type} {tile_of_respondent} {role_qualifier_text}in terms of salary.\n")

    # Give some context, so print out the salary ranges for all quartiles (if role is being compared) or every 10th percentile
    # if role not being compared i.e. comparison required to all IT workers nationally
    print(f"      The national salary {tile_type}s are:\n")
    for i in range(len(salaries),1,-1):
        if (comparitor == "role") or ( (i%20 -1) == 0):
            print(f"             {tile_type} {tiles[i - 1 ]} contains salaries above {'€{:,}'.format(int(salaries[i - 1]))}\n")


def compare_respondent_nationally_experience(respondent):
    """
    This function is called if the user has chosen to compare the salary of the respondent with national figures, on the basis 
    of experience. 
    """
    # the details of the respondent passed are stored in relevant variables
    name,email,role,experience,salary = respondent

    # Open the worksheet which holds national salary figures on the basis of experience  
    worksheet = SHEET.worksheet("experience")

    # get the salaries for years of experience
    salaries = worksheet.col_values(2)
    
    # the salary and expereince of the respondent passed are converted to intergers for comparison  and retrieval purposes
    numeric_of_salary = int(salary)
    numeric_of_experience = int(experience)
    
    # retrieve the average salary nationally for the respondent's experience
    average_salary = int(salaries[numeric_of_experience])
 
    # retrieve the title corresponding to the role of the respondent in question
    titles = SHEET.worksheet("roles").col_values(1)
    title = titles[int(role)].title()           

    # Print details of the respondent being compared
    print(f"\nThe respondent in question has a role of {title}, experience of {experience} years and a salary of {'€{:,}'.format(int(salary))} euros.")

    print(f"\n        The average salary nationally for this level of experience is {'€{:,}'.format(int(salaries[numeric_of_experience]))}." )
    
    # express salary as a percentage of average salary
    if numeric_of_salary < average_salary:
        salary_percent = int(round((1 - (numeric_of_salary / average_salary)) * 100,0 ))
        print(f"\n        The respondent's salary is {salary_percent} percent below the national average for this level of experience." )
    elif numeric_of_salary > average_salary:    
        salary_percent =  int(round( ((numeric_of_salary / average_salary) -1) * 100,0))
        print(f"\n        The respondent's salary is {salary_percent} percent above the national average for this level of experience." )
    else:
        print(f"\n        The respondent's salary is equal to the national average for this level of experience." )    

def main():
    """
    The main function, it displays a welcome message, gets a respondent's details and then presents the report menu
    """
    print_introduction()
    respondent = get_respondent()
    update_respondents(respondent)
    menu(respondent)

main()    