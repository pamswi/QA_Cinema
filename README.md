# QA_Cinema
Final-project:

Fibonacci story points in agile estimation
Introduction:
In Agile and Scrum methodologies, estimating the complexity and effort of user stories is crucial for effective project planning. The Fibonacci sequence is a widely adopted method for assigning story points, providing a structured approach to relative estimation.
Understanding the Fibonacci Sequence:
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
It starts with 0 and 1 and continues as follows: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
Each number in the sequence represents a story point, which is used to estimate the complexity of user stories.
Stages of process:
CONSENSUS
ESTIMATION
DISCUSSION
Benefits of Using Fibonacci Story Points:
Relative Sizing: Story points allow for relative comparison of complexity.
Flexibility: The Fibonacci sequence accommodates a wide range of task sizes.
Focus on Discussion: Estimation sessions foster team discussion and understanding.
Velocity Tracking: Story points aid in tracking team velocity for capacity planning.

Design Decision 1: Forking Central Repository and Using Pull/Merge Requests with Pam as Request Validator

Title: Forking Central Repository and Pull/Merge Requests

Date: [Insert Date]

Background:
In the QA Cinemas project, we need to establish a workflow for collaborative development and version control. To ensure a systematic and controlled approach to code changes, we have decided to fork the central repository on GitHub and utilize the pull/merge request system, with Pam as the central repository request validator.

Alternatives:

Direct Commit to Central Repository: Allowing team members to directly commit changes to the central repository without a forking and pull/merge request process.
Different Request Validator: Choosing a different team member or an automated system as the request validator.
Pros and Cons:

Alternative	Pros	Cons
Direct Commit to Central Repo	Simple and quick, less overhead.	Lack of control and validation of code changes.
Different Request Validator	Distributed responsibility, multiple validators.	Potential inconsistency in validation process.
Chosen Solution:
We have chosen to fork the central repository on GitHub and utilize the pull/merge request system with Pam as the central repository request validator for the following reasons:

It provides a structured and controlled approach to code changes, ensuring code quality and consistency.
Forking allows team members to work on changes independently and submit them for review.
Pam's experience and expertise make her an ideal candidate for request validation.
Dependencies:

Setting up individual forks of the central repository for each team member.
Ensuring that team members are familiar with the pull/merge request workflow.
Pam's availability and willingness to review and validate pull/merge requests.
Rationale:

The chosen approach ensures code quality, version control, and collaboration among team members.
Forking allows parallel development without conflicting changes in the central repository.
Pam's role as the request validator ensures consistency in code validation and maintains project standards.
References:

GitHub Pull Requests Documentation: https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests
Review and Approval:

Reviewed and approved by [Your Name], Lead Developer, on [Insert Date].
Updates and Revisions:

None at this time.
Conclusion:
The decision to fork the central repository and utilize the pull/merge request system with Pam as the request validator enhances our version control and collaboration process. It ensures code quality, consistency, and controlled access to the central repository, aligning with our project's goals of efficient and organized development.


Design Decision One: Separate Booking Page for QA Cinema

Introduction

In the QA Cinema website project, we have made a design decision to create a separate booking page for movie screenings instead of dynamically generating booking forms on the same page as the movie listings. This decision was made to simplify the user interface, enhance user experience, and improve the maintainability of the website.

Background

Initially, we considered dynamically generating booking forms for movie screenings on the same page as the movie listings using JavaScript. This approach would allow users to book tickets directly from the movie listing page. However, as the project evolved, we encountered challenges related to the complexity of managing data, URL routing, and the potential for overloading the routes.

Problem Statement

The dynamic generation of booking forms on the same page as movie listings posed several challenges:

Complex Data Management: Managing user selections, movie details, and booking data dynamically on a single page introduced complexity.
Overloaded Routes: Incorporating booking functionality within the movie listing routes could lead to overloaded routes, making the code less maintainable.
URL Structure: Maintaining a clear and user-friendly URL structure became challenging as the page needed to handle various states and data.
Proposed Solution

To address the challenges mentioned above, we decided to create a separate booking page for movie screenings. Here's how this solution works:

Dedicated Booking Page: We have a dedicated HTML page specifically for booking movie screenings. This page provides a clear and focused user interface for booking tickets.
Simplified Routing: By separating the booking functionality into its own page, we maintain a clear and straightforward URL structure. Users can access the booking page directly from the movie listing page.
Data Flow: The booking page receives data, such as the screening ID and movie details, through URL parameters. This data is used to pre-fill the booking form and provide context to users.
Streamlined User Interface: The separate booking page provides a more intuitive and streamlined user interface, improving the overall user experience.
Simplified Data Management: Data management becomes more straightforward, as each page has a dedicated purpose and scope. It also allows for better error handling and validation.
Benefits

Creating a separate booking page for movie screenings offers several advantages:

Improved User Experience: Users can access a dedicated booking page, making the ticket booking process more user-friendly and intuitive.
Clear URL Structure: Maintaining a clear and concise URL structure enhances user understanding and navigation.
Simplified Data Management: Data handling becomes more manageable, reducing the risk of errors and improving the reliability of the booking process.
Enhanced Maintainability: Separating the booking functionality into its own page improves code organization and maintainability.
Flexible Routing: This approach provides flexibility for future enhancements and modifications to the booking process.
Conclusion

The decision to create a separate booking page for movie screenings aligns with our goals of simplifying the user experience, enhancing maintainability, and improving the clarity of our URL structure. This design decision contributes to a more efficient and user-friendly QA Cinema website, ensuring a smoother booking process for our users while simplifying data management and routing on the backend.



Risk Assessment for QA Cinemas Training Project
Project Overview:

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

Conclusion:

The QA Cinemas training project is an opportunity to enhance technical skills and gain practical experience. By proactively addressing potential risks, focusing on collaboration and learning and ensuring a clear understanding of Devops principles, the team can maximize the benefits of this training project.


