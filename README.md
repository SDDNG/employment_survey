# Employment (IT Sector Salary) Survey
This application allows a user to enter respondents' details into an IT salary survey and then to compare a respondent's salary to the salary of either, other respondents, or, to salaries nationally based on data held on the IT sector.  

Comparisons can be in terms of either role, experience or simply all to other employees. At least one respondent's details must be entered in a session before any comparison reports can be run and during any session, a user can enter as many respondents' details as they wish. If the user has entered only one respondent and then chooses to run a report, the application automatically selects that one respondent, if however, they have entered more than one respondent, they are prompted to select the respondent they wish to run comparisons against.
## Main menu
After a welcome screen is displayed:

<img width="377" alt="Welcome Screen" src="https://user-images.githubusercontent.com/70945839/161566910-d7f9a598-efd3-434a-a251-4752b2499ee6.png">

the main menu is displayed:

<img width="479" alt="Main Menu" src="https://user-images.githubusercontent.com/70945839/161567468-497657fd-d2cc-4862-880e-44864fff5067.png">

From the main menu, the user has the choice of entering a repondent's details, running a report or Exiting. If they wish to run a report they must have entered at least one repondent's details, as all of the reports are comparison reports and they need something to compare to. If they try to choose the reports menu and at least one respondent has not been entered, they will be presented with a message telling them they must enter at least one respondent:

<img width="648" alt="At least one respondent" src="https://user-images.githubusercontent.com/70945839/161568907-60232bd0-1078-44d7-a054-b593f26fdedd.png">

## Entering a respondent's details
The user is asked to enter the respondent's name (optional), email (optional), role (from 8 pre-defined roles), experience and salary.

<img width="346" alt="Entering Respondent's Details" src="https://user-images.githubusercontent.com/70945839/161569666-80c54f73-c140-4c7b-bc49-cdf2358cb9f3.png">

If an email is entered, it must be in a valid format. The role must be one of the pre-defined ones, experience can be between one and fifty years and salary must be between €10,000 and €500,000. Once valid data has been entered, the details will be added to a Google Spreadsheet and a list of respondents added during the current session - there is more detail about the data model below.
## Report menu
If the user chooses the report menu and they have entered more than one respondent during this session then they will be asked to select from those respondents entered:

<img width="494" alt="Respondents entered this session" src="https://user-images.githubusercontent.com/70945839/161571184-edd1f32b-f61a-424c-9b8d-def596efa851.png">

If they have only entered one respondent in the session, then that respondent will be automatically selected. Once a respondent has been selected the user is presented with the report menu:

<img width="463" alt="Report menu" src="https://user-images.githubusercontent.com/70945839/161571985-8fd2dd03-3100-415b-9ee7-b2bfbc3d9fe4.png">

From here they can choose one of six reports or choose to exit back to the main menu. When they run a report, they are returned to the report menu and they can run as many reports sequentially as they want before they choose to return to the main menu.

## Report 1: Compare the respondent's salary to other respondents in terms of their role
The respondent selected is compared to all other respondents with the same role, the number of respondents with a higher salary, if any is displayed, the number with the same salary, if any, is displayed and the number with a lower salary, if any, is displayed. The program pauses so the user can look at the information and they are requested to press a key when they wish to continue:

<img width="722" alt="respondent to respondents role" src="https://user-images.githubusercontent.com/70945839/161573175-4f733384-7457-40be-a03e-dfe1d7b2ee4e.png">

## Report 2: Compare the respondent's salary to other respondents in terms of their experience
The respondent selected is compared to all other respondents with the similar experience i.e. =/- a year, the number of respondents with a higher salary, if any is displayed, the number with the same salary, if any, is displayed and the number with a lower salary, if any, is displayed. The program pauses so the user can look at the information and they are requested to press a key when they wish to continue:

<img width="707" alt="respondent to respondents experience" src="https://user-images.githubusercontent.com/70945839/161573763-823ef24c-470e-4a67-873a-ea611be22528.png">







