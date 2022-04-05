# Employment (IT Sector Salary) Survey
This application allows a user to enter respondents' details into an IT salary survey and then to compare a respondent's salary to the salary of either, other respondents, or, to salaries nationally based on data held on the IT sector.  

Comparisons can be in terms of either role, experience or simply to all other employees. At least one respondent's details must be entered in a session before any comparison reports can be run and during any session, a user can enter as many respondents' details as they wish. If the user has entered only one respondent and then chooses to run a report, the application automatically selects that one respondent, if however, they have entered more than one respondent, they are prompted to select the respondent they wish to run comparisons against.
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
The respondent selected is compared to all other respondents with the similar experience i.e. +/- a year, the number of respondents with a higher salary, if any is displayed, the number with the same salary, if any, is displayed and the number with a lower salary, if any, is displayed. The program pauses so the user can look at the information and they are requested to press a key when they wish to continue:

<img width="707" alt="respondent to respondents experience" src="https://user-images.githubusercontent.com/70945839/161573763-823ef24c-470e-4a67-873a-ea611be22528.png">

## Report 3: Compare the respondent's salary to all other respondents, regardless of role or experience
The respondent selected is compared to all other respondents, the number of respondents with a higher salary, if any is displayed, the number with the same salary, if any, is displayed and the number with a lower salary, if any, is displayed. The program pauses so the user can look at the information and they are requested to press a key when they wish to continue:

<img width="719" alt="Respondent to all other respondents" src="https://user-images.githubusercontent.com/70945839/161574526-57d94b50-e0e4-48cf-918e-1ccb7b28309a.png">

## Report 4: Compare the respondent's salary to national data, in terms of role
The respondent selected is compared to data held for salaries for people with a similar role. The information is saved in quartiles, so the user is told which quartile the respondent falls into and the lower salary range for each quartile. 

<img width="739" alt="role nationally" src="https://user-images.githubusercontent.com/70945839/161575287-ee6bcd16-5b92-46f4-8974-f4b89b9a966b.png">

## Report 5: Compare the respondent's salary to national data, in terms of experience
The respondent selected is compared to data held for salaries for people with the same experience. The salary of the respondent is compared in terms of percentage of the national average for that level of experience.

<img width="759" alt="Experience nationally" src="https://user-images.githubusercontent.com/70945839/161576272-9f336af2-4bef-427c-8547-1c2b865fd484.png">

## Report 6: Compare the respondent's salary to national data, regardless of role or experience
The respondent selected is compared to data held for salaries for people in the IT sector nationally. The information is saved in percentiles, so the user is told which percentile the respondent falls into and the lower salary range for every 20th pecentile. 

<img width="833" alt="all IT nationally" src="https://user-images.githubusercontent.com/70945839/161577053-16018219-d18e-4eb0-94a2-86a282d64d3b.png">

## Data Model
### Respondent
A respondent is an object comprised of name, email, role, experience and salary. The first two are optional strings while the last three are numerics.

Within the program, the component items of a respondent are captured and validated then added to a list of respondents entered in that session of the program and appended to a respondent tab in a Google spreadsheet, see below.  

### Google Spreadsheet
A Google Spreadsheet with 8 tabs was created: 

The first tab stores the respondent data i.e. name (if one entered), email (if one entered), role, expereince and salary. Name and email in a real world setting would need to be handled appropriatley from a data protection standpoint.

The second tab stores the bottom salary level for each percentile of people nationally in the IT sector.

The third tab stores the average salary for each year, 1 to 40, of experience.

The fourth tab stores the bottom salary level for each quartile of people with the role of developer.

The fifth tab stores the bottom salary level for each quartile of people with the role of senior developer.

The sixth tab stores the bottom salary level for each quartile of people with the role of Technical Lead.

The seventh tab stores the bottom salary level for each quartile of people with the role of Head of Engineering.

The eight tab stores the eight roles and their respective salary ranges.

The program appends respondents to the first tab and then uses the other tabs when creating the comparison reports.

### Features Left to Implement

It would be good to implement the ability to send an email summarising a rspondent in terms of the six reports.

## Testing 

Testing was performed on each individual field to make sure that proper validation was performed i.e. that menus will only accept selections which are valid and respondent data is, either, in a valid numerice range or emails are correct format. 

Scenarios where reports were attempted to be run with no respondents previously entered were tested and these successfully stopped the reports from being run. 
Scenarios were tested where reports were run after only one respondent was entered and that respondent was automatically selected for comparison.
Scenarios were tested where reports were run after multiple respondents were entered and the user was forced to choose one before the report could proceed. 

The menu navigation i.e. iteration was also tested. 

### Validator Testing 
The run.py code was run through pycodestyle and all significant errors were fixed. The remaining errors were for lines, either text from the program or logic for the program which were over 79 characters. 

### Unfixed Bugs

There are no known functional bugs. 

## Deployment
- The site was deployed to Heroku. 

## Modules installed
gspread and Credential from google.oauth2.service_account were both installed.

The re module was installed to allow validation of email formats.

The OS module was installed to allow the screen to be cleared at various points in the program.

## Program flow

<img width="284" alt="flowchart" src="https://user-images.githubusercontent.com/70945839/161585963-06832de4-9296-47e6-ae0d-e5c4dee63548.png">


## Credits 

The Code institute GitHub templates and the modules from the Diploma in Software Development were referenced repeatedly. W3Schools.com, W3org.com and StackOverflow.com were all also referenced liberally.











