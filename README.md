# Django Restaurant Booking System #

## Purpose of the project ##
The Restaurant Booking System is a Full-Stack web application that allows users to make reservations at a restaurant online. Users can create an account, log in, and then make, modify, or cancel a booking for a particular date and time. The application is built using Python and Django as the MVC framework, along with HTML, CSS, and JavaScript for the Front-End. The application uses a relational database (PostgreSQL) to store and manage data about users and bookings.

### External User's Goal ###
The external user's goal is to book one or more guests for a meal in a restaurant at a particular time and date.

### Site Owner's Goal ###
The site owner's goal is to take and manage online bookings for their restaurant.


## Features ##

![SCREENSHOT OF FLOWCHART]()

__User Authentication and Authorization__
-   Users can create an account and log in to the system using username and password.

__Bookings Management__
-   Users can create a new booking for one or more guests at a particular time and date.
-   Users can modify or delete existing bookings.
-   The system prevents double bookings for the same user.

__Form Validation__
-	Prompts user to input valid form data.

__Admin dashboard for site owners to view and manage all bookings__
-   Admin accepts bookings, turning their status to True in the UI.
-   Admin can view, change and delete bookings and users.

## Future features ##
- Prevent bookings outside of the restaurant's opening hours. At the moment a user can request a booking at any time and date in the future, and it's up to the admin to not accept the booking if the time is not right.
- When a user submits invalid form input for a new booking, the form clears and they get a red error alert prompting them to enter valid information. For smoother UX, the old information could prepopulate the fields, meaning the user would not have to re-enter all information from scratch. This is not an issue when updating bookings, only in creating new ones.
- The home page can display a menu, information about the restaurant, a picture, opening hours and more advanced styling to make the experience more lively.
- The system can allow for multiple table occupancies.
- The feature for preventing a user from making double bookings could be developed so that the user id is used in identifying the owner of the booking. At the moment email is used for this.


## Technologies Used ##
- [GitPod](https://gitpod.io/) was used to write, edit and commit the code, [GitHub](https://github.com/) was used for storage and version control.
- [ElephantSQL](https://www.elephantsql.com/) was used as PostgreSQL database for the project.
- [Heroku](https://www.heroku.com/) was used for deployment and testing.
- [Lucidchart](https://www.lucidchart.com/pages/) was used to create a flowchart of the project.
- [Am I Responsive](https://ui.dev/amiresponsive) was used to create screenshot of website on different screen sizes.


## Testing ##

### Code validation ###
- No errors were returned when passing the Python code through the [PEP8 Python Linter](https://pep8ci.herokuapp.com/)
- No errors were returned when passing the CSS file through [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator)

![SCREENSHOT OF PYTHON VALIDATION](media/screenshot-python-linter.png)

### Manual testing ###
I have manually tested this project by doing the following:
- Run the code through pylint using the terminal and received a rating of 10/10.
- Entering invalid inputs into the form (pressing Enter without any input, entering invalid numerals, entering empty space in the special requirements text field).
- Used PEP8 Python validator and returned the code with no errors. Some comments regarding indentation were ignored as the validator did not recognize multi-line print statements.
- Tested the code in my local development environment as well as in the Heroku deployed app.

### Test cases ###

#### Quiz Introduction ####

- 

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

- I wanted to add a feature where a user is prevented from making a double booking for the same date and time as one of their other bookings. Initially I did this by adding if statements in the form_valid function for the create and edit booking views, so that an error was raised if the same user tried to double book for the same date and time. After a system crash, I deleted the if statement and went back to my model, where I added unique_together = ('date_time', 'email') into the meta class for the model. I then added an error handler directly in the template. This way, a booking made with the same e-mail adress and the same date and time raises an error and prompts the user to enter another date. It is not perfect however, as a user could still use different e-mail addresses in the booking form and make more than one booking for the same time and date.

## Deployment ##

### Via GitPod ###
The GitHub repository was created using the Code Institute Python Essentials template:
https://github.com/Code-Institute-Org/python-essentials-template
- Click the link to get to the template. Click “Use this template”.
- Enter repository name, make the repository public and click “Create repository from template”.
- Click the green GitPod button, wait a moment for the workspace to open. All work was committed in GitPod.

- The repository can be accessed through following link: https://github.com/robinozer/PythonProject.git

### Via Heroku ###
Heroku was used to deploy the website. The following steps were used:
- After creating an account, create a new app and navigate to the Settings tab.
- In Config Vars, click 'Reveal Config Vars' and add one with key 'PORT' and value '8000'.
- In Buildpacks, click 'Add buildpack' and select python, and then node.js, saving changes after each.

- Go to the Deploy tab, select GitHub as the Deployment Method, and confirm.
- Search for the repository name and connect.
- Deploy the branch.

## Credits ##
- The style.css file, as well as parts of the base.html template were borrowed from CI and Matt walkthrough project https://github.com/Code-Institute-Solutions/Django3blog


