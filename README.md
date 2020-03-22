# TagAlong application

## Index
[Brief](#brief)
   * [ Gist the application](#)

[Overview of the application](#)
   * [Solution](#)
   
[Architecture](#architecture)
   * [Entity Relationship Diagram](#)
	
[Testing](#testing)
     
[Deployment Stage](#depl)
   * [Tools Used](#tech)
     
[Project tracking](#PTT)

[Risk Assesment](#RA)

[Improvements for the Future](#improve)

[Authors](#auth)

[Acknowledgements](#ack)



<a name="brief"></a>
## The Brief

To create a Flask based application using tools and technologies that help build the CRUD functionality with a database that contains two tables.


<a name="overview"></a>
## Overview

Creation of an application which is called TagAlong that allows users to register their travel interests which includes their hobby, in the place that they are 

doing it and the time of the year that they will be there to do the activity.Users can view plans of everyone and see if any plans align with theirs and then they 

Tag along.


<a name="architecture"></a>
## Architecture
<a name="erd"></a>
### Entity Relationship Diagram
![ERD](/Documents/ERD.png)

As shown in the ERD, the DB consists of two tables which initially was three tables that consisted of a User.As later on to keep the application simple, I removed the User table to have just the hobby-travel plan registerations without login.
The tables have a Many-to-one relation between them as shown, hence I did not need an intermediate table.


<a name="testing"></a>
## Testing

Pytest has been used for testing.Test coverage for the backend is % .
There can be more improvements in the next coming sprints on the testing and application front.


<a name="deployment"></a>
## Deployment Stage

The build, and deployment process is automated using Jenkins, that was triggered whenever there was a push even on GitHub which was setup using a webhook

![Deployment Pipeline](/Documents/CI_pipeline.png)


<a name="Tools"></a>
### Tools Used

* Google Cloud Platform's SQL instance - Database
* Python and Flask framework - Logic
* Jenkins - CI Server
* PyTest - Testing
* [Git](https://github.com/Poonam1390/TagAlong.git) - Version Control Tool
* [Trello](https://trello.com/b/dhgxajA2/tag-along) - Project Tracking
* Google Cloud Platform - Live Environment


<a name="improve"></a>
## Improvements for the Future

At this point, to update the hobby-travel plan , you need to enter the entire data again along with the plan no which is the ID referenced in the table and also to delete the plan you need to enter the plan ID as there is no login involved to delete only your plans registered.

In the coming sprints, I would like to add the login functionality so its easier to do the update and delete functionality.Another improvement would be to add the functionality to send emails to the first created hobby-travel plan if the plan registrered by the user matches with the already created hobby-travel plan.


<a name="tracking"></a>
## Project tracking
![Project tracker](/Documents/Trello_board.png)


<a name="Risks"></a>
## Risk Assesment
![Risk Register](/Documents/Risk_Register.png)


<a name="author"></a>
## Authors

Poonam Udevar Mohankumar

<a name="ack"></a>
## Acknowledgements

* QA consulting and our fantastic instructors
* The amazing and fun cohorts on this DevOps programme
