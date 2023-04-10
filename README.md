# Django Restaurant Booking System #

## Purpose of the project ##
The Restaurant Booking System is a Full-Stack web application that allows users to make reservations at a restaurant online. Users can create an account, log in, and then make, modify, or cancel a booking for a particular date and time. The application is built using Python and Django as the MVC framework, along with HTML, CSS, and JavaScript for the Front-End. The application uses a relational database (PostgreSQL) to store and manage data about users and bookings.

### External User's Goal ###
The external user's goal is to book one or more guests for a meal in a restaurant at a particular time and date.

### Site Owner's Goal ###
The site owner's goal is to take and manage online bookings for their restaurant.


## Features ##

__User Authentication and Authorization__
-   Users can create an account and log in to the system using username and password.
-   Users cannot access content belonging to a different user.
-   Users cannot access their own content without logging in to their account.

__Bookings Management__
-   Users can create a new booking for one or more guests at a particular time and date.
-   Users can modify or delete existing bookings.
-   The system prevents double bookings for the same user.

__Site navigation and main structure__
-	The website has a navigation menu clearly directing the user to each feature.
-   The design is simple and has a header, main part where bookings, instructions and forms display, and a footer at the bottom of the page.

__Form Validation__
-	Both forms (for creating a new booking and editing an existing one) raise errors when a user tries to submit form with invalid input.
-   User gets a prompt to enter valid data.

__Admin dashboard for site owners to view and manage all bookings__
-   Admin accepts bookings, turning their status to True in the UI.
-   Admin can create, view, update and delete bookings.
-   Admin can create, view, update and delete users.

## Further Features to implement ##

- The home page can display a menu, information about the restaurant, a picture, opening hours and more advanced styling to make the experience more lively.
- The system can allow for multiple table occupancies.


## Technologies Used ##
- [GitPod](https://gitpod.io/) was used to write, edit and commit the code, [GitHub](https://github.com/) for storage and version control.
- [ElephantSQL](https://www.elephantsql.com/) was used as PostgreSQL database for the project.
- [Heroku](https://www.heroku.com/) was used for deployment and testing.


## Database Model ##

![SCREENSHOT OF DATABASE MODEL](media/database-model.png)

There are two tables in this database model: **User** and **Booking**.

The **User** table has a one-to-many relationship to the **Booking** table. Each **Booking** is associated with exactly one **User**, but each **User** can have zero, one, or many **Bookings**. The **Booking** table has a foreign key relationship with the **User** table, meaning that each booking must belong to a user.


The **Booking** table has a field for **id** (the primary key of the table) and one for **user_id** (a foreign key that references the **id** field of the **User** table). It also has fields for **first_name**, **last_name**, **email**, **date_time**, **guests**, **special_request**, and **accepted**, all of which are specific to the **Booking** model. 

All of these fields work together to represent a single booking made by a user. The **user** field allows us to associate the booking with a specific user, while the other fields store information about the booking itself, such as the date and time, number of guests, and any special requests. The **accepted** field is a boolean field that indicates whether the booking has been accepted or not.

The **Booking** table also has a unique constraint on the combination of **date_time** and **email**, ensuring that no two bookings can be made with the same date and time, and email address.



## Testing ##

### Manual testing ###
I have manually tested this project by doing the following:
- Entering invalid inputs into the form (pressing Enter without any input, entering invalid numerals, entering empty space in the special requirements text field).
- Tried each feature step by step, and documented in test cases below.
- Tested the code in my local development environment as well as in the Heroku deployed app.

## Agile development and User stories ##
Using principles of design thinking, the following goals were set for this project:
- Make the signup process as smooth as possible
- Make it easy for users to see and alter their bookings
- Make it easy for manager to see and manage all changes

These led to this problem statement: How do I develop a restaurant booking system that provides the functionality above to a user?

The problem statement was then used to map out the features I would need. I then created user stories corresponding to these features.
GitHub (specifically a custom user story template, issues and digital KanBan board) was used as an agile tool for creating and managing user stories, assigning them labels and tracking their progress throughout development. The board also helped with breaking down the project into sprints, keeping feature development organized (as each feature had to be created, tested and validated before the next one was created). Each sprint had an estimated time it would take to develop it, further helping keep the project systematic and organized in terms of time.

-   As a site admin I can create, view, edit and delete bookings so that I can manage my restaurant
-   As a site admin I can accept bookings so that I can choose which bookings to take
-   As a website visitor I can register an account so that I can log in to the system
-   As a website visitor I can create a new booking so that I have a table at the restaurant
-   As a website visitor I can view, update and delete my bookings so that I can manage my bookings

- Prevent double booking
- prepulate fields with previous information when editing a booking
- Don't allow bookings in past dates

### Test cases ###

#### User registration ####
- User story: As a website visitor I can register an account so that I can log in to the system

- Testing performed: enter the URL of deployed page in browser, click Register in nav menu, enter mock details and click 'Sign Up'.

- Expected outcome: successful user registration, logs in user to platform automatically with registration.

- Result: as expected.

- Test passed.

![SCREENSHOT OF SIGNUP PAGE](media/signup.png)
![SCREENSHOT OF SUCCESFUL SIGN IN](media/signup-successful.png)

#### Book a table ####
- User story: As a website visitor I can create a new booking so that I have a table at the restaurant

- Testing performed: once logged in, click 'Book a table' in nav menu. 

- Expected outcome: redirect user to booking form. 

- Result: as expected.

- Test passed.

![SCREENSHOT OF ](media/.png)

### Code validation ###
- No errors were returned when passing every .py file through the [PEP8 Python Linter](https://pep8ci.herokuapp.com/) (see screenshots for models.py and views.py in linter).
- No errors were returned when passing the CSS file through [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator)
- All pages were run through [W3C HTML Validator](https://validator.w3.org/) with no errors.

![SCREENSHOT OF PYTHON VALIDATION](media/models-python-validation.png)
![SCREENSHOT OF PYTHON VALIDATION](media/views-python-validation.png)

## Fixed bugs ##

I added a feature where a user is prevented from making a double booking for the same date and time as one of their other bookings. Initially I did this by adding if statements in the form_valid function for the create and edit booking views, so that an error was raised if the same user tried to double book for the same date and time. After a system crash, I deleted the if statement and went back to my model, where I added unique_together = ('date_time', 'email') into the meta class for the model. I then added an error handler directly in the template. This way, a booking made with the same e-mail adress and the same date and time raises an error and prompts the user to enter another date. It is not perfect however, as a user could still use different e-mail addresses in the booking form and make more than one booking for the same time and date.

## Features to develop for better UX ##

- The feature for preventing a user from making double bookings could be developed so that the user id is used in identifying the owner of the booking, instead of email.
- Prevent bookings outside of the restaurant's opening hours: At the moment a user can request a booking at any time and date in the future, and it's up to the admin to not accept the booking if the time is not right.
- When a user submits invalid form input for a new booking, the form clears and they get a red error alert prompting them to enter valid information. For smoother UX, the old information could prepopulate the fields, meaning the user would not have to re-enter all information from scratch. This is only the case when creating new bookings, not updating old ones.
- Unfortunately due to time constraints these features could not be implemented in this project.

## Deployment ##

### Via GitPod ###
The GitHub repository was created using the Code Institute Python Essentials template:
https://github.com/Code-Institute-Org/python-essentials-template
- Click the link to get to the template. Click “Use this template”.
- Enter repository name, make the repository public and click “Create repository from template”.
- Click the green GitPod button, wait a moment for the workspace to open. All work was committed in GitPod.

- The repository can be accessed through following link: https://github.com/robinozer/PythonProject.git

### Via ElephantSQL ###
- After loggin in, create new instance, give it a name and select region. Click 'Review' and Confirm new instance. Use URL in config vars in Heroku(see below) and in project env.py file.

### Via Heroku ###
Heroku was used to deploy the website. The following steps were used:
- After creating an account, create a new app and navigate to the Settings tab.
- In Config Vars, click 'Reveal Config Vars' and add config vars for secret key, database url (from ElephantSQL), Heroku PostreSQL and another with key 'PORT' and value '8000'. 
- Config var DISABLE_COLLECTSTATIC set to value of 1 was used during project development and removed in final deployment.
- In Deploy, connect to GitHub repository and deploy branch to main.

## Attaching PostgreSQL database to the project ##
In settings.py:
- Underneath 'from pathlib import Path', add the following:
import os  
import dj_database_url  
if os.path.isfile('env.py'):  
     import env
- Comment out the existing DATABASES and add the following:  
DATABASES = {'default':dj_database_url.parse(os.environ.get('DATABASE_URL'))}
- Migrate the changes.  

- The secret key variable, now secured since placed in env.py, is also added to settings.py like so:  
SECRET_KEY = os.environ.get('SECRET_KEY')

## Credits ##
- The style.css file, as well as parts of the base.html template were borrowed from CI and Matt's walkthrough project https://github.com/Code-Institute-Solutions/Django3blog
