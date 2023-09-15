# QA Cinema

The project goal is to create a cinema website that allows users to buy tickets for movies they wish to see.

## Table of Contents
1. [Introduction](#1-introduction)
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
14. [Installation Deployment and testing](#14-installation-Deployment-testing)
15. [Conclusion](#15-conclusion)
16. [Acknowledgements](#16-acknowledgements)
17. [References](#17-references)



 
## 1. Introduction

Introduce the project's purpose, goals, and high-level overview.

The project goal is to create a cinema website that allows users to buy tickets for movies they wish to see.

---

## 2. Project Structure

- **Directory Structure**: Describe the organizational structure of your directories and files.
- **Main Components**: Explain the primary components/modules of your application and their roles.
- **Flow**: If applicable, describe the flow or sequence in which different parts of your project interact.

---

## 3. Tech Stack

Detail all the technologies you used in this project:

- **Languages**: (Python, JavaScript, HTML, CSS)
- **Frameworks**: (Flask)
- **Databases**: (SQlite, MySQL)
- **Deployment**: ( Docker)
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

---

## 6. Wireframe

Present and describe any wireframes, mockups, or design blueprints for your project:

- **[Link to Wireframe]**
- **Design Notes**: Any specific components or flow mechanisms to highlight?

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
- **Read**: How is data retrieved and presented?
- **Update**: How can data be modified?
- **Delete**: How can data be removed? Any safeguards?

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

- **What You Did**: Describe the testing steps, scenarios, and any innovative methods applied.
- **Testing Analysis**: Detail the problems you faced during testing and how you overcame them.
- **Strategy**: Explain the testing approach, the types of tests employed (unit, integration, etc.), and any tools or frameworks used.
- **Results**: Summarize key findings, link to detailed results or reports if available.

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



---
## 14. Installation Deployment and testing

The QA Cinemas training project is an opportunity to enhance technical skills and gain practical experience. By proactively addressing potential risks, focusing on collaboration and learning and ensuring a clear understanding of Devops principles, the team can maximize the benefits of this training project.

---
## 15. Conclusion

The QA Cinemas training project is an opportunity to enhance technical skills and gain practical experience. By proactively addressing potential risks, focusing on collaboration and learning and ensuring a clear understanding of Devops principles, the team can maximize the benefits of this training project.

---
## 16. Acknowledgements

Thank any individuals, organizations, or resources that were instrumental in the project:

- Person/Resource name: Brief description or reason for acknowledgement.

- AA: I want to thank Earl for his awesome Github repo which I was using as examples to do the booking forms and validators among other things.

---

## 17. References

List all sources, tools, or libraries you referred to during the project:

1. [Name of Source](URL) - Brief description of the source.


[Footer or any additional notes or links you want to add]

