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

### Google Spreadsheet
A Google Spreadsheet with 8 tabs was created: 
The first tab stores the respondent data i.e. name (if one entered), email (if one entered), role, expereince and salary. Name and email in a real world setting would need to be handled appropriatley from a data protection standpoint.
The second tab stores the bottom salary level for each percentile of people nationally in the IT sector.
The third tab stores the average salary for each year, 1 to 40, of experience.

### Features Left to Implement

It would be good to implement the ability to send an email summarising a rspondent in terms of the six reports.

## Testing 

Testing was performed on each individual field, functional area and the interaction of the functional areas. Before the user can calculate a maintenance calorie amount, it was ensured that all fields need to be specified correctly and before a target calorie amount can be specified, it is required that a maintenance amount be calculated. If a user specified a macro percentage breakdown that is not 100%  warning is issued.

During the testing, it was decided that Event Listeners should be used in such a way that alerts were not called incessantly if a user were to mistype but called when a significant operation was about to occur. This was judged to be the right balance between ensuring accurate inputs without making the user exprience cumbersome.

When the screen width goes below 950px, the Target Goals section moves from the right of the screen to below the Current Maintenance Calories section. When the screen width goes below 460px, the width of columns in the Macro Composition area is reduced.

The application works on an iPhone but it does not look as well as it might, some additional time would ideally be spent in addressing this.

The application has some issues on Firefox in that the area where macronutrient percentages are displayed are automatically displayed with up and down arrows beside them obscuring the fields, some additional time would ideally be spent addressing this. 

One area that was not addressed is to optimise the display based on the display scale of the device. The programming occured on a laptop where the display was set to 150% and it fits best there. When it is changed to 100%, the application still looks reasonable and functions but it would be optimal if the font size automatically adjusted to make better use of the relatively larger screen. Some prelimiary investigation of this indicated that it is possible with some dynamic media queries in the javascript code interacting with the CSS.  

### Validator Testing 
The run.py code was run through pycodestyle and all significant errors were fixed. The remaining errors were for lines, either text from the program or logic for the program which were over 79 characters. 

### Unfixed Bugs

There are no obvious functional bugs but a decision was made not to check each field as it is entered with dedicated Event Listeners but rather to check at significant stages e.g. when the Calculate Maintenance Calories button is clicked, when the Target (in terms of weight) is changed or when the Composition in terms of Macronutrients is changed. This makes for a better experience most of the time but there are some situations where it might be frustrating to have to change an input. It also means if a Current Maintenance Amount is calculated and then a field is changed but the Calculate Maintenance Calories button is not pressed again that the user might be misled (although this is unlikely). It was felt that continually recalculating fields everytime one value changed would be unpleasant for the user.

Another area that would be nice to have a more elegant solution to is in the Macronutrient Composition is set to a number other than 100%, the user is warned but in some instances resetting the numbers might be preferable, however, in other cases it was felt that this could be misleading if the user was unknowingly left with a composition they did not intend and on balance this was a worse situation.

One area that was not addressed is to optimise the display based on the display scale of the device. The programming occured on a laptop where the display was set to 150% and it fits best there. When it is changed to 100%, the application still looks reasonable and functions but it would be optimal if the font size automatically adjusted to make better use of the relatively larger screen. Some prelimiary investigation of this indicated that it is possible with some dynamic media queries in the javascript code interacting with the CSS. 

## Deployment
- The site was deployed to GitHub pages. 

## Credits 

The Code institute GitHub templates and the modules from the Diploma in Software Development (E-commerce Applications) were referenced repeatedly. W3Schools.com, W3org.com and StackOverflow.com were all also referenced liberally.

For the actual Calorie Maintenance formulas https://tdeecalculator.net/ and https://www.calculator.net/tdee-calculator.html were used along with Wikipedia and the book The Lean Muscle Diet by Alan Aragon and Lou Schuler.

Google Fonts and Favicon.io were also utilised.










