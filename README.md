# Project Description:
My project is a task management system that allows users to create tasks, track time entries, and generate reports. It's built using Python and SQLAlchemy.
### Code Structure:
* cli.py: This file contains the command-line interface (CLI) for my project. Users interact with my application through commands provided in this script.
* dbstuff.py: This file is responsible for setting up my database, creating a session, and initializing the database schema. It uses SQLAlchemy to communicate with the SQLite database.
* models.py: This file defines my database models using SQLAlchemy's declarative base. It outlines the structure of the database tables and their relationships.

### Database Structure:
My project's database consists of the following tables:
* users: Stores user information, including a unique username and password. Users have a one-to-many relationship with tasks, time entries, and reports.
* tasks: Represents tasks created by users. Tasks have a one-to-many relationship with time entries.
* time_entries: Records time entries associated with tasks. Each time entry tracks the start time, end time, and duration of work.
* reports: Stores user-generated reports, which may include summaries of tasks and time entries.


### User Actions (cli.py):
* Create User: Users can create new accounts by providing a username and password. The system checks for existing usernames to ensure uniqueness.
* Login: Registered users can log in with their username and password, gaining access to their account.
* Create Task: Authenticated users can create new tasks by providing a task title. The system associates the task with the logged-in user.
* Delete Task: Users can delete tasks by specifying their username and the title of the task to delete. The system ensures the task belongs to the specified user.
* Display Tasks: Users can view their tasks by providing their username. The system lists all tasks associated with that user.
* Generate Report: Users can generate reports, which may include task summaries and time entries for specific users.
* Delete User: Authenticated users can delete their accounts, along with associated tasks and time entries.

## Licence
MIT licence.