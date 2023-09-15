# QA Cinema

The project goal is to create a cinema website that allows users to buy tickets for movies they wish to see.

## Table of Contents
1. [Introduction](#1-introduction)
2. [Installation Steps](#2-installation-steps)
2. [Project Structure](#2-project-structure)
3. [Tech Stack](#3-tech-stack)
4. [Requirements Gathering](#4-requirements-gathering)
5. [Design Choices](#5-design-choices)
6. [Wireframe](#6-wireframe)
7. [ERD Diagram](#7-erd-diagram)
8. [CRUD Features](#8-crud-features)
9. [Component Diagram](#9-component-diagram)
10. [Pipeline Diagram](#10-pipeline-diagram)
11. [Testing](#11-testing)
12. [Risk Assessment](#12-risk-assessment)
13. [Code Refactoring](#13-code-refactoring)
14. [Conclusion](#14-conclusion)
15. [Acknowledgements](#15-acknowledgements)
16. [References](#16-references)




## 1. Introduction

Introduce the project's purpose, goals, and high-level overview.

The project goal is to create a cinema website that allows users to buy tickets for movies they wish to see.

---
## 2. Installation steps
1. Clone the repo
	`git clone https://github.com/pamswi/QA_Cinema`
2. Create a virtual Environment
	`python -m venv venv`
	`venv\Scripts\activate`
3. Install the dependencies
	`pip install -r requirements.txt`
4. Run create.py to feed the database
	`python3 create.py`
5. Finally run the app
	`python3 app.py`
It should then be accessible on port 5000 of localhost

## 2. Project Structure

- **Directory Structure**: Describe the organizational structure of your directories and files.

        QA-Cinema/
        │
        ├── application/ 
        │ ├── static/ 
        │ │ ├── script.js 
        │ │ ├── styles.css
        │ │ └── images/ 
        │ ├── templates/
        │ ├── routes.py 
        │ └── init.py 
        ├── scripts/ 
        │ ├── containers.sh
        │ ├── testing.sh 
        ├── tests/ 
        │ ├── test_app.py 
        ├── additional-resources/ 
        ├── README.md 
        ├── app.py
        ├── create.py 
        ├── models.py 
        ├── nginx.conf
        ├── Jenkinsfile
        ├── docker-compose.yaml 
        ├── Dockerfile 
        └── requirements.txt 

- **Main Components**: Explain the primary components/modules of your application and their roles.  

**Key modules**:
 - `app.py`: This is the main entry point of the application. It sets up the web server, handles routing, and manages user requests.
  - `models.py`: Defines data models and the database schema for storing information related to cinema, movies, users, and bookings.
  - `routes.py`: Manages URL routing and handles HTTP requests, including rendering HTML templates and processing user interactions.
  - `containers.sh`: A script used in Jenkins Pipeline for managing Docker containers, such as building, starting, stopping, or removing containers.
  - `testing.sh`: A script used in Jenkins Pipeline for automating testing procedures, which may include running unit tests, integration tests, or other testing tasks.
   - `test_app.py`: This test script focuses on testing specific features of the application, ensuring that they function as intended and identifying any issues or regressions.
  - `docker-compose.yaml`: Configuration file for Docker Compose, defining the multi-container application setup.
  - `Dockerfile`: Used to build the Docker image for the Flask application.
  - `nginx.conf`: Nginx configuration file, if the application is deployed behind an Nginx web server.
  - `requirements.txt`: A list of Python dependencies required for the application to run successfully.
  - `Jenkinsfile` is a Jenkins pipeline file used for setting up continuous integration and continuous delivery (CI/CD) processes for the "QA-Cinema" application.

---

## 3. Tech Stack

Detail all the technologies you used in this project:

- **Languages**: (Python 3.11.4, JavaScript, HTML 5, CSS)
- **Frameworks**: (Flask)
- **Databases**: (SQlite, MySQL Ver 8.0.33)
- **Deployment**: (Docker)
- **Other Tools**: (Github, Jenkins)

---

## 4. Requirements Gathering

Discuss the process by which you gathered requirements for your project:


- **Research**: Did you use existing literature or projects to inform your design?
- **Iterations**: Describe how the requirements might have evolved over time.

---

## 5. Design Choices

Discuss the major design decisions you made for this project:

### Design Decision 1: Forking Central Repository and Using Pull/Merge Requests with Pam as Request Validator

Title: Forking Central Repository and Pull/Merge Requests

Date: [Insert Date]

Background: In the QA Cinemas project, we need to establish a workflow for collaborative development and version control. To ensure a systematic and controlled approach to code changes, we have decided to fork the central repository on GitHub and utilize the pull/merge request system, with Pam as the central repository request validator.

Alternatives:

Direct Commit to Central Repository: Allowing team members to directly commit changes to the central repository without a forking and pull/merge request process. Different Request Validator: Choosing a different team member or an automated system as the request validator. Pros and Cons:

Alternative Pros Cons Direct Commit to Central Repo Simple and quick, less overhead. Lack of control and validation of code changes. Different Request Validator Distributed responsibility, multiple validators. Potential inconsistency in validation process. Chosen Solution: We have chosen to fork the central repository on GitHub and utilize the pull/merge request system with Pam as the central repository request validator for the following reasons:

It provides a structured and controlled approach to code changes, ensuring code quality and consistency. Forking allows team members to work on changes independently and submit them for review. Pam's experience and expertise make her an ideal candidate for request validation. Dependencies:

Setting up individual forks of the central repository for each team member. Ensuring that team members are familiar with the pull/merge request workflow. Pam's availability and willingness to review and validate pull/merge requests. Rationale:

The chosen approach ensures code quality, version control, and collaboration among team members. Forking allows parallel development without conflicting changes in the central repository. Pam's role as the request validator ensures consistency in code validation and maintains project standards. References:

GitHub Pull Requests Documentation: https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests Review and Approval:

Reviewed and approved by [Your Name], Lead Developer, on [Insert Date]. Updates and Revisions:

None at this time. Conclusion: The decision to fork the central repository and utilize the pull/merge request system with Pam as the request validator enhances our version control and collaboration process. It ensures code quality, consistency, and controlled access to the central repository, aligning with our project's goals of efficient and organized development.

### Design Decision 2: Separate Booking Page for QA Cinema

Introduction

In the QA Cinema website project, we have made a design decision to create a separate booking page for movie screenings instead of dynamically generating booking forms on the same page as the movie listings. This decision was made to simplify the user interface, enhance user experience, and improve the maintainability of the website.

Background

Initially, we considered dynamically generating booking forms for movie screenings on the same page as the movie listings using JavaScript. This approach would allow users to book tickets directly from the movie listing page. However, as the project evolved, we encountered challenges related to the complexity of managing data, URL routing, and the potential for overloading the routes.

Problem Statement

The dynamic generation of booking forms on the same page as movie listings posed several challenges:

Complex Data Management: Managing user selections, movie details, and booking data dynamically on a single page introduced complexity. Overloaded Routes: Incorporating booking functionality within the movie listing routes could lead to overloaded routes, making the code less maintainable. URL Structure: Maintaining a clear and user-friendly URL structure became challenging as the page needed to handle various states and data. Proposed Solution

To address the challenges mentioned above, we decided to create a separate booking page for movie screenings. Here's how this solution works:

Dedicated Booking Page: We have a dedicated HTML page specifically for booking movie screenings. This page provides a clear and focused user interface for booking tickets. Simplified Routing: By separating the booking functionality into its own page, we maintain a clear and straightforward URL structure. Users can access the booking page directly from the movie listing page. Data Flow: The booking page receives data, such as the screening ID and movie details, through URL parameters. This data is used to pre-fill the booking form and provide context to users. Streamlined User Interface: The separate booking page provides a more intuitive and streamlined user interface, improving the overall user experience. Simplified Data Management: Data management becomes more straightforward, as each page has a dedicated purpose and scope. It also allows for better error handling and validation. Benefits

Creating a separate booking page for movie screenings offers several advantages:

Improved User Experience: Users can access a dedicated booking page, making the ticket booking process more user-friendly and intuitive. Clear URL Structure: Maintaining a clear and concise URL structure enhances user understanding and navigation. Simplified Data Management: Data handling becomes more manageable, reducing the risk of errors and improving the reliability of the booking process. Enhanced Maintainability: Separating the booking functionality into its own page improves code organization and maintainability. Flexible Routing: This approach provides flexibility for future enhancements and modifications to the booking process. Conclusion

The decision to create a separate booking page for movie screenings aligns with our goals of simplifying the user experience, enhancing maintainability, and improving the clarity of our URL 
structure. This design decision contributes to a more efficient and user-friendly QA Cinema website, ensuring a smoother booking process for our users while simplifying data management and 
routing on the backend.

# Design Choices 3: Appearance  & Colors 

Aesthetics and Branding: Color plays a crucial role in creating the visual identity and brand recognition of a website. Consistent color schemes and palettes help reinforce brand. 

Colors also have psychological and emotional associations. Different colors can evoke specific emotions or moods. We chose orangered because is can be very energetic and attention grabbing and very often used in advertising. 

The color of text and background must contrast sufficiently to ensure readability. Poor color choices can make content difficult to read, especially for people with visual impairments. Web designers must consider accessibility guidelines to ensure that all users can access and understand the content.


Color can be used to guide users through a website. Buttons, links, and call-to-action elements were highlighted with specific colors to make them stand out and encourage user interaction. This aids in navigation and improves the overall user experience.
---

## 6. Wireframe

Present and describe any wireframes, mockups, or design blueprints for your project:

Link to prototype of user interface(UI):

[Mock Up                                               Home    About Us    What.docx](https://github.com/kesgermany/QA_Cinema/files/12610429/Mock.Up.Home.About.Us.What.docx)

Header
- Logo
- Navigation Menu

Hero Section 
- New Releases Gallery

Features and Services
- Cards, Gallery

Footer
- Footer links 

---

## 7. ERD Diagram

Present and discuss your Entity Relationship Diagram:

Firstly we wanted to see how the movielens DB looked like to take some ideas, ultimatley we decided not to go ahead with how the DB was used in movie lens and opted for our own due to having tables that were not relevant to our specifications. 

![Screenshot 2023-09-04 224559](https://github.com/akber360/QA_Cinema/assets/139133081/3cd74bb5-3dd2-4a3a-add6-08468d9bf2a6) 

Based on our first rundown of posible Tables to exist, a draft ERD was constructed 

![image](https://github.com/akber360/QA_Cinema/assets/139133081/faf22559-731d-4ba4-bef4-25722714fae8)


![Draft_ERD](https://github.com/akber360/QA_Cinema/assets/139133081/cae20d4e-53b7-4fbd-a78d-7d9fe8eb54c5)
This draft would give a visual to the links on the database and would allow us to asses the relationships between them, 

Ultimatly a version 2 of Database tables were discussed and would than be implementned, 
![image](https://github.com/akber360/QA_Cinema/assets/139133081/fcc73d29-137e-454f-b660-fbac0b5d6291)
 
This is the final Working ERD diagram to our Cinema Database which contains the relationships.
![Final_ERD](https://github.com/akber360/QA_Cinema/assets/139133081/6de93f93-0d75-45c7-99e8-224a4d2c8190)


In this database, several tables work in concert to create a comprehensive cinema management system.  

The `User` Table is central, capturing user information for registration, login and payment.  
Movies are cataloged in the `Movie` Table, which includes details like titles, directors, and actors.  
Screenings, including times and capacities, are tracked in the `Screening` Table, linked to specific movies and screens.   
When users book tickets, their data is recorded in the `Booking` Table, including booking dates and total prices, associated with both users and screenings. Further granular details of these bookings, such as ticket types and quantities, are stored in the `BookingDetail` Table.   
Meanwhile, the `Discussion` Table fosters movie-related discussions, collecting topics, content and timestamps.  
Lastly, the `Screen` Table represents various cinema screens, capturing seating capacity data and classifications.  

Although there are no explicit many-to-many relationships in this database, it demonstrates robust interconnections among users, movies, bookings, and discussions, resulting in a comprehensive cinema management platform.


The primary relationships include:

- `User` and `Booking`: The `User` table represents users of the application and is associated with the Booking table, allowing each user to make multiple bookings. This forms a one-to-many relationship where one user can have many bookings.

- `Movie` and `Screening`: The `Movie` table stores information about movies, and the `Screening` table represents individual screenings of those movies. This relationship enables each movie to have multiple screenings, forming a one-to-many relationship from Movie to `Screening`.

- `Screening` and `Booking`: The `Booking` table captures user bookings for specific screenings, creating a one-to-many relationship from `Screening` to `Booking`. Each screening can have multiple bookings, representing the fact that multiple users can book tickets for the same screening.

- `Booking` and `BookingDetail`: The `Booking` table relates to the `BookingDetail` table, which stores details about each booking, such as ticket types and quantities. This relationship forms a one-to-many relationship from `Booking` to `BookingDetail`, where each booking can have multiple booking details.

- `User` and `Discussion`: The User table relates to the `Discussion` table, allowing users to participate in discussions. Each user can create multiple discussion posts or comments, creating a one-to-many relationship from `User` to `Discussion`.



- **[Link/Embed of ERD Diagram]**
- **Key Entities and Relationships**: Discuss the main tables/entities and their connections. (PAM)

---
## 8. CRUD Features

Detail the CRUD (Create, Read, Update, Delete) features of your project:

- **Create**: How do users add new data?
using classmethods like shown here when this function would be called user data such as name email and password would be added to the database ![image](https://github.com/akber360/QA_Cinema/assets/139133081/6a5e5bd1-0507-4b3a-807e-65a56bde0b2d)
Another example of users adding data is when the user is making a moive booking the book-movie method gets called and user choices are craeted on to booking and booking_detailsdatabase
![image](https://github.com/akber360/QA_Cinema/assets/139133081/9fafe03b-4f98-4148-847a-68efe12e5a9a)

- **Read**: How is data retrieved and presented?
From the screening database to show all the screening ID and things such as current cappcity of seats left was all being read by the Screening database using a method called screening_by_movies. this would return the movie id
![image](https://github.com/akber360/QA_Cinema/assets/139133081/6a877c51-a4f1-41c5-91b9-c3f6dfb7e6bd)
 Here is another example of database being read where Movie class is being called by various fuunctions where search function is being implemented also.
![image](https://github.com/akber360/QA_Cinema/assets/139133081/1af4b6fe-f925-41a9-bb0e-606b7a1839e6)


---

## 9. Component Diagram

- **VMS Containers**: Jenkins
- **Description**: A brief explanation of the component diagram and its significance.
- **Link/Embed**: Link to or embed the component diagram.

---

## 10. Pipeline Diagram

- **Diagrams**: Webhooks, environments
- **Description**: Describe the pipeline, its stages, and its role in the CI/CD process.
- **Link/Embed**: Link to or embed the pipeline diagram.

---

## 11. Testing

Unit testing was carried out using the Pytest module as a general testing framework, with Flask-Testing used to allow for testing of the web related functionalities.

- TestBase class:

	The TestBase class inherits from flask_testing’s TestCase class and is used as a base class for the other test classes. It provides functions to configure a test Flask app, sets up and populates a test database, as well as providing a function to clear the session and remove data from the database after each test case.

- TestBasicPages class:

	This class contains tests for the static and more simple dynamic pages of the application, such as the homepage, cinema services, listings, classics pages etc. Each of the functions in this class has an assertion to check that a successful response has been made (status code 200). Another assertion is then made to check that relevant data specific to each page is present in the response data.

- TestSearch:
  
	This class contains tests for the search function, with assertions to check that a successful response has been made (status code 200), as well as assertions to check that the correct data is present in the response data.

- TestAPI:
  
	This class provides tests for the view screenings api, with assertions to check that a successful response has been made (status code 200), as well as assertions to check that relevant data relating to each move is included in the response.data. There is also a function with assertions to check that an apporoptriate error message is included in the response data.

- TestPayment:
  
	This class provides tests for the payment page with a function to check the GET response of the page and ensure the correct data is included in the response data. The second function and it’s assertions check that payment information is collected and correctly added to the User database.

- TestSignup:

	This class has a number of test functions to check the functionality of the Signup page, including functions and assertions to check that Signup details are correctly submitted to the User database, check that the username is unique, ensure that the passwords match as well as to test the password securtiy features.

- TestLogin:

	This class has functions to check the GET response of the page as well as functions which test whether the user as successfully logged into the session, check the response if there is no account associated with the username, as well as a function to check the response if an incorrect password is entered.

- TestLogout:

	This class has functions to check that a user is successfully logged out and assert that the user is no longer in the session as well as checking the user is correctly redirected to the Homepage.

- TestForum:

	This class’s GET function checks that the test discussions are correctly brought in from the Discussions database, as well as functions to check that new posts and comments are correctly added to the Forum page. Included is also a function to ensure the inappropriate language filter is working correctly.

- TestBooking:

	This class’s GET function checks that the correct movie details are included in the response data, as well as a function with assertions to check that the correct details have been added to the Booking database and BookingDetail databases respectively.

- Initalising testing:

	Ensure the DATABASE_URI is assigned to your MySQL testing database:

		export DATABASE_URI=mysql+pymysql://[username]:[password]@[database name]

	Ensure you’re bash shell is in the QA_Cinema folder and run one of the following commands, depending on preference:

		py -m pytest --cov=application --cov-report term-missing

		py -m pytest --cov=application --cov-report term-html

- Results and analysis:

	![Picture5](https://github.com/Tom-Freed/QA_Cinema/assets/91968539/1c075a5a-c310-4aba-a685-ce30249dea51)

 
	We achieved a 99% coverage report on our main application file (routes.py), the remaining 1% is due to unused code in the routes.py file which could be removed in a future code refactoring (see below).

	![Picture1](https://github.com/Tom-Freed/QA_Cinema/assets/91968539/53e4d681-b23a-44bb-b8d9-bf13c317347a)


	The unit tests carried out are relatively robust, however further assertions for some test to ensure that all the relevant data is being provided on each page or all of the inputted data has correctly been added to the relevant database would be beneficial.

	When carrying out testing the initial testing data had to be amended or added to on occasion to ensure functionality was being properly checked. The main example of this was for testing the search function, where in the initial data the movie titles were too similar and formatted in an unrealistic manner for correct testing. Additionally, a third Movie entry was later added to test that the search function was only displaying films relevant to the search entry:

	![Picture2](https://github.com/Tom-Freed/QA_Cinema/assets/91968539/2848fcc2-f173-4188-8358-76e59356b8e7)

	Initial test data

	![Picture3](https://github.com/Tom-Freed/QA_Cinema/assets/91968539/74497409-456c-425c-b8fc-d7c856859e68)

	Amended titles

	![Picture4](https://github.com/Tom-Freed/QA_Cinema/assets/91968539/fbc1b6ff-0bf9-430e-88e0-5eea190ae74e)

	Third Movie database entry added


---

## 12. Risk Assessment

- **Approach**: Describe the methodology used for risk assessment.
- **Key Risks**: Highlight the main risks identified and the proposed mitigation strategies.

The QA Cinemas training project involves the development of a full-stack web application for a cinema chain. This assessment identifies potential technical and learning-related risks that may impact the project's success.
Risk Identification:
1. Technical Complexity
Description: The project's technical requirements, such as integrating third-party services and implementing complex features, may exceed the team's current skill level.
Impact: Delays in development, increased learning curve, and potential project challenges.
Mitigation: Allocate extra time for learning and skill development. Seek guidance from mentors or experienced team members.
2. Scope Creep
Description: Uncontrolled additions or changes to project requirements during development due to a desire for additional features.
Impact: Increased project scope, potential learning overload, and project focus diversion.
Mitigation: Maintain a clear understanding of the project's scope and objectives. Focus on mastering core concepts before adding extra features.
3. Integration Challenges
Description: Difficulty in integrating external services and APIs into the application due to lack of prior experience.
Impact: Delays in development, potential learning barriers, and increased complexity.
Mitigation: Prioritize learning integration techniques and seek assistance from experienced developers or trainers.
4. Resource Constraints
Description: Inadequate availability of training resources, such as documentation or tutorials, for specific technologies.
Impact: Learning challenges, potential project delays, and limited access to knowledge.
Mitigation: Explore a variety of learning resources, such as online tutorials, books, or courses, to bridge knowledge gaps.
5. Learning Curve
Description: The project may involve technologies or concepts that are new to the team, resulting in a steep learning curve.
Impact: Slower progress, potential frustration, and a need for additional time for skill acquisition.
Mitigation: Develop a structured learning plan and allocate time for skill acquisition. Seek guidance from mentors or trainers.
6. External Payment Handling
Description: The project relies on an external payment handler, and no card details will be stored within the application.
Impact: Reduced security responsibilities, but potential challenges in integrating and ensuring seamless payment processing.
7. VM for Apps Stops Functioning
Description: The virtual machine (VM) hosting the application servers may encounter technical issues or crashes, causing disruptions in the application's availability and functionality. This could result in downtime and affect users' access to the application.
Impact: Moderate Likelihood, High Impact
Risk Level: Moderate
8. Pushing Sensitive Info to GitHub
Description: There is a risk of accidentally pushing sensitive information, such as API keys, credentials, or confidential data, to a public or private GitHub repository. This can lead to data breaches, security vulnerabilities, and compliance issues.
Impact: Moderate Likelihood, High Impact
Risk Level: Moderate
9. VScode Ceases to Connect to VM
Description: The connection between Visual Studio Code (VScode) and the virtual machine (VM) used for development may fail, preventing developers from accessing and editing code. This can hinder development and collaboration efforts.
Impact: Low Likelihood, High Impact
Risk Level: Moderate
10. Jenkins VM Ceases to Function
Description: The VM hosting the Jenkins continuous integration/continuous deployment (CI/CD) server may experience technical issues, resulting in the disruption of automated build, test, and deployment processes. This can lead to delays in the software development lifecycle.
Impact: Low Likelihood, High Impact
Risk Level: Moderate
11. VM for DB Stops Functioning
Description: The virtual machine (VM) responsible for hosting the database server may encounter problems or crashes, affecting the availability and reliability of the database. This can lead to data unavailability and potential data loss.
Impact: Moderate Likelihood, High Impact
Risk Level: Moderate
12. Database Hack
Description: There is a risk of a malicious actor gaining unauthorized access to the database, potentially leading to data breaches, data manipulation, or data theft. This can have severe consequences for data security and user privacy.
Impact: Low Likelihood, High Impact
Risk Level: Moderate


| Risk                         | Likelihood     | Impact                   | Risk Level |
|------------------------------|----------------|--------------------------|------------|
| Technical Complexity         | High           | Moderate                 | Moderate   |
| Scope Creep                  | Moderate       | Moderate                 | Moderate   |
| Integration Challenges       | Moderate       | Moderate                 | Moderate   |
| Resource Constraints         | Low            | Low                      | Low        |
| Learning Curve               | Moderate       | Moderate                 | Moderate   |
| External Payment Handling    | Low            | High                     | Moderate   |
| Absence                      | Moderate       | High                     | Moderate   |
| VM for Apps Stops Functioning | Moderate       | High                     | Moderate   |
| Pushing Sensitive Info to GitHub | Moderate    | High                     | Moderate   |
| VScode Ceases to Connect to VM | Low          | High                     | Moderate   |
| Jenkins VM Ceases to Function | Low           | High                     | Moderate   |
| VM for DB Stops Functioning   | Moderate       | High                    | Moderate   |
| Database Hack                | Low            | High                     | Moderate   |


Risk Mitigation:

Emphasize team work as the primary goal of the training project. This is because team members often bring different skills, knowledge, and expertise to the table. By working together, they can complement each other's strengths and compensate for weaknesses, resulting in more well-rounded and effective solutions.

Create a supportive learning environment within the team by encouraging communication and learning.

Regular integration and bug fixes to mitigate integration challenges.

---

## 13. Code Refactoring

- **Screenshots**: Consider embedding or linking to before-and-after screenshots to showcase changes.
- **Overview**: Explain the need and benefits of the refactoring, including aspects like efficiency improvements or readability enhancements.
- **Key Changes**: Detail major changes made, with before-and-after code snippets where useful.

## 14. Deployment

<img width="1440" alt="Screenshot 2023-09-12 at 19 18 49" src="https://github.com/pamswi/QA_Cinema/assets/125991084/ca476045-9268-4463-9c2f-652e97f8505e">

<img width="1440" alt="Screenshot 2023-09-13 at 12 05 09" src="https://github.com/pamswi/QA_Cinema/assets/125991084/187b30f9-b082-4133-9f37-e396aebca25b">


---
## 14. Conclusion

The QA Cinemas training project is an opportunity to enhance technical skills and gain practical experience. By proactively addressing potential risks, focusing on collaboration and learning and ensuring a clear understanding of Devops principles, the team can maximize the benefits of this training project.

---
## 15. Acknowledgements

Thank any individuals, organizations, or resources that were instrumental in the project:

- Person/Resource name: Brief description or reason for acknowledgement.

- AA: I want to thank Earl for his awesome Github repo which I was using as examples to do the booking forms and validators among other things.

---

## 16. References

List all sources, tools, or libraries you referred to during the project:

1. [Stackoverflow](https://stackoverflow.com/) - forum for coding related questions used it for python library and flask related questions
2. Earls Github - Has lots of exmaples on flask routes and forms etc
3. [Geek for Geeks]([https://stackoverflow.com/](https://www.geeksforgeeks.org/) - found how to resolve github issues
4. [W3 Schools](https://www.w3schools.com/) - For various exmaples in Python and HTML 


[Footer or any additional notes or links you want to add]

