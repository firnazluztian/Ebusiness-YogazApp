PROJECT SETUP INSTRUCTION
Step Descriptions
1)
Create a 
GitHub account
GitHub repository
Trello boards

2)
Install project environments for each OS (Windows/Mac)
Ensure Python is installed
Ensure Python flask is installed
Ensure docker is installed

3)
Clone the project from GitHub: 
https://github.com/firnazluztian/Ebusiness-YogazApp.git
4)
Check git status, pull changes, create a branch for each member
5)
Front-end and Back-end team work independently, conduct unit testing to each completed task
6)
In the end of the sprint, branches are merged and system testing is conducted

Project is hosted on  http://mianmian.duckdns.org:8888/


------------------------------------------------------------


Assessment Task 2: Application Development Group Web Project

CP 5310: E-Business Technologies

Team member:
Firnaz Luztian Adiansyah - 13686589 
Jimena Yu Qing Muchsel - 13686884
Mianmian Zhang - 13652608
Tianliang Yi  - 13659225


James Cook University
Project objectives
Today, almost everything can be found online, the main purpose of the migration of local to online businesses is so that client can reach more customers. Moreover, Yoga websites are becoming more and more common by providing basic yoga features and classes. However, Most of the Yoga Websites have terrible UI/UX designs and unresponsive. We would like to develop a Yoga web application that is responsive, interactive, has good UI/UX designs, and is usable. Our main goal is to build a user friendly site to help yoga lovers, beginners or yoga enthusiasts to have easy access to yoga classes, trainers, events, etc.

Keyword: Responsive, Interactive, User friendly, User experience, User Interface, Usability

Web2.0 features
Requirements 
Description
Priority
ETC
ClassType.html
Display a list of class types from JSON using AJAX
High
3
ClassSchedule.html
Display a list of class schedules from DB SQLite
High
3
Trainer.html
Display a list of Trainer information from DB
Name
Image
Description

Medium
4
AboutUs.html
Display a paragraph of project goals 
Low
3
ContactUs.html
Display some contact information
Low
3
Index.html
Display a slider with news or recent information
Button onclick pop-up JS login box

High
3
Signup.html
Display registration form that will be connected to python signup script and DB
High
4
Profile.html
Display registration form that will be connected to python login script and DB
High
4
Yogaz.json
Creation of JSON file in order to dynamically display data retrieved from the JSON file into the front end


Medium
3
Sign up and Login function
Sign up function to allow user to register their information to the database. Login function will be used for existing registered users
High
3
DB creation + storing data to database 
Data from sign up form will be stored in Database
High
3
User authentication & authorization
Check user login and sign up to ensure user is authorized to access his own data only
Medium
3
User Session
Handle user session such as log out and profile button instead of login and signup
High
3
User Log out
Handle if user session is true then log out can be done
High
2
Book class
Class id will be stored in the user table
Medium
2
Search bar
Search JSON lists and return any match input
Low
2
Hosting 
Host the webpage online from a hosting service
Low
2

Features implemented
Features
Description
ClassType.html
JSON and AJAX is used to display class types
ClassSchedule.html
Class schedule data is retrieved from the SQlite class type table and displayed them in a card 
Trainer.html
Trainer data is displayed from DB from Trainer table
Beginner.html
Accordion with JQuery and different yoga poses pictures
AboutUs.html
HTML and CSS
ContactUs.html
HTML and CSS plus iframe google maps
Index.html
HTML and CSS, slider, login and signup button, and session handling
Signup.html
User can sign up and will be storing all the information

Profile.html
Display basic user information in a div 

Yogaz.json






Sign up and Login function
Python flask script to handle sign up and login 
DB creation and storing data to database 
We are using SQLite since it is lightweight
Four Tables creation:

User authentication & authorization
Check if user is already in the db, check username and password if they match with the one in DB
User Session
Check user session if on then display the logout and remove the signup and login button
Hosting 
Website is hosted in a server that can be accessed remotely

Features planned but not implemented
Features
Reason
Search bar
Search bar could not be implemented because there was not enough time as its priority is low so it was not implemented.
Responsiveness
Some objects in the pages are not responsive as we could not implement bootstrap properly to achieve our desired style.
Class Types (JSON)
Json file suddenly was not displaying the data in the last minute, therefore we decided to get the class types information from DB

Potential improvements
In the near future, the Yogaz project can be further improved by implementing more features in order to improve user experience. The use of more complex python flask integration to build a more robust and secure product can be our next potential goals. Yogaz can be brought to cross-platform by integrating the system with Ionic. 

Framework and technologies 
Programming language
JavaScript (front-end), Python (back-end)
Framework
JQuery, JQueryUI, AJAX, Python Flask
Web Tech
HTML, CSS, Bootstrap, JSON
Database
SQLite
Version Control
Git, Github
Images/Container Platform
Docker
SDLC 
Agile with Scrum

Individual contributions of each member
Firnaz Luztian Adiansyah
Roles: Fullstack
Contribution:
Created and managed repository in the version control, GitHub, and write the project report in google docs so other team members could collaborate real time.
Implemented a responsive skeleton page for all the pages with bootstrap.
Created dummy JSON file with classes, and trainers, and dummy user data.
Retrieved JSON data using AJAX get request.
Restructured files as template and static to fit python flask project format.
Create and display data from DB SQlite in trainer, class-type, class-schedule, profile.

Jimena Yu Qing Muchsel
Roles: UI/UX, Graphic designer, Front-End developer
Contribution: 
Styling the pages with CSS
Contributed on index.html, contactus.html, beginner.html
Photoshopped images and designed a logo to fit the theme of the website
Implemented iframe with google maps in contactus.html
Worked on the page aboutme.html
Added information about the trainers and yoga classes in the JSON file.
Worked on python flask

Mianmian Zhang
Roles: Front-end developer, UI/UX designer
Contribution:
Provided hosting services
Designed the styling of the pages
Beginner.html, profile.html, indexlogin.html
Pop-up confirmation about booking
Worked on python flask together 
Picture editing 
Content design 

Tianliang Yi
Roles: Front-end developer
Contribution:
Created animation in JS/JQuery
Designed the styling of the pages
Contactus.html, index.html, indexlogin.html
Work on Python flask

Project roles



Actual implementation schedule

Configuration management



Project plan: https://trello.com/b/WURGU0ZZ/yogaz
Week 5
Plan project content and idea
Define project scope
Identify end-user
Gather requirements 
Identify software, hosting, tools or development environments

Week 6
Design wireframes or web skeletons
Set up development environment (Installing necessary tools/plugins)
Create all required HTML, CSS, JS, PHP files

Week 7, 8, 9
Design, Develop, Test, Review 
Improve the design or add more interactions/functionalities

Week 10
Final release & bug fixing


