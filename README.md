# Django Restaurant Booking System #

## Purpose of the project ##
This is a web-based application that allows users to book a table at a restaurant. Users can create an account, log in, and then make, modify, or cancel a booking for a particular date and time.


## Features ##

![SCREENSHOT OF FLOWCHART]()

__User account creation and login system for external users__

__Once logged in, a user can create new bookings, modify existing bookings, and cancel bookings__
-   Prompts user to input valid form data.

__Input validation__
-	Prompts user to input valid form data.

__Admin dashboard for site owners to view and manage all bookings__
- Admin accepts bookings, and can change and delete bookings and users.

## Future features ##

- At the moment a user can request a booking at any time and date. A future feature would be to prevent bookings outside of the restaurant's opening hours.
- When a user enters an invalid number of guests for a new booking, they get an error alert prompting them to enter a valid number of guests. This happens after form submission and clears the form, making the user have to re-enter all information. 
- The home page can display a menu, information about the restaurant, a picture, opening hours and more to make the experience more lively.
- The system can allow for multiple table occupancies.
- The system can automatically prevent a user from making a booking at the same date and time as one of their other bookings.



## Technology ##
- [GitPod](https://gitpod.io/) was used to write, edit and commit the code, [GitHub](https://github.com/) was used for storage and version control.
- [ElephantSQL](https://www.elephantsql.com/) was used as the PostreSQL database.
- [Heroku](https://www.heroku.com/) was used for deployment and testing.
- [Lucidchart](https://www.lucidchart.com/pages/) was used to create a flowchart of the project.
- [Am I Responsive](https://ui.dev/amiresponsive) was used to create screenshot of website on different screen sizes.


## Testing ##

### Code validation ###
- No errors were returned when passing the Python code through the [PEP8 Python Linter](https://pep8ci.herokuapp.com/)

![SCREENSHOT OF PYTHON VALIDATION](media/screenshot-python-linter.png)

### Manual testing ###
I have manually tested this project by doing the following:
- Run the code through pylint using the terminal and received a rating of 10/10.
- Entered invalid inputs as question answers (pressing Enter without any input, entering invalid numerals, entering letters and entering empty space) several times over.
- Used PEP8 Python validator and returned the code with no errors. Some comments regarding indentation were ignored as the validator did not recognize multi-line print statements.
- Tested the code in my local terminal as well as the Heroku terminal.

### Test cases ###

#### Quiz Introduction ####

- Testing performed: enter the URL of deployed page and click Run Program.

- Expected outcome: displays welcome message with instructions on how to play the quiz, and a prompt to press Enter to start.

- Result: as expected.

- Test passed.

![SCREENSHOT OF QUIZ INTRODUCTION](media/screenshot-introduction.png)

#### Quiz Start ####

- Testing performed: press Enter after the introduction to start the quiz.

- Expected outcome: display first question along with 4 answer options. Display instruction on how to answer the question.

- Result: as expected.

- Test passed.


![SCREENSHOT OF QUIZ START](media/screenshot-start-quiz.png)

#### Enter valid answer option ####

- Testing performed: entering a valid number when answering a question (1-4).

- Expected outcome: See if my answer is correct, display the correct option, and my score.

- Result: as expected.

- Test passed.

![SCREENSHOT OF VALID ANSWERS, THIS ONE INCORRECT](media/screenshot-valid-incorrect-answer.png)

![SCREENSHOT OF VALID ANSWERS, THIS ONE CORRECT](media/screenshot-valid-correct-answer.png)

#### Enter invalid answer option ####

- Testing performed: entering an invalid character (e.g. letter S) when answering a question.

- Expected outcome: alert message prompting me to re-enter a valid answer option.

- Result: as expected.

- Test passed.

![SCREENSHOT OF INVALID ANSWER](media/screenshot-invalid-answer.png)

#### End of quiz ####

- Testing performed: answer all questions.

- Expected outcome: display message showing final score.

- Result: as expected.

- Test passed.

![SCREENSHOT OF QUIZ END](media/screenshot-end-quiz.png)

### Fixed bugs ###

- 

## Deployment ##

### Via GitPod ###
The GitHub repository was created using the Code Institute Python Essentials template:
https://github.com/Code-Institute-Org/python-essentials-template
- Click the link to get to the template. Click “Use this template”.
- Enter repository name, make the repository public and click “Create repository from template”.
- Click the green GitPod button, wait a moment for the workspace to open.

- The repository can be accessed through following link: https://github.com/robinozer/portfolio4.git

### Via Heroku ###
Heroku was used to deploy the website. The following steps were used:
- After creating an account, create a new app and navigate to the Settings tab.
- In Config Vars, click 'Reveal Config Vars' and add one with key 'PORT' and value '8000'.
- In Buildpacks, click 'Add buildpack' and select python, and then node.js, saving changes after each.

- Go to the Deploy tab, select GitHub as the Deployment Method, and confirm.
- Search for the repository name and connect.
- Deploy the branch.

## Credits ##
- CI for the deployment terminal.