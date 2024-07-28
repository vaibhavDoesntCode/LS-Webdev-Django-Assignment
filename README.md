# LS-Webdev Final Assignment
# Basic Tweeting Website
## Overview
This is a basic tweet application built using Django. The app provides user authentication (login and signup) and allows users to post, edit, and delete their tweets. Users can also view tweets posted by other users

## Features
- User authentication (login and signup)
- Create, edit, and delete tweets
- View tweets from all users

## Requirements

- Python 3.x
- pip (Python package installer)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vaibhavDoesntCode/LS-Webdev-Django-Assignment.git
   ```
2. **Create and activate a virtual environment**
   * on Windows:
     ~~~bash
     python -m venv venv
     venv\Scripts\activate
     ~~~
    * On macOS and Linux:
      ~~~bash
      python -m venv venv
      source venv/bin/activate
      ~~~
  3. Install the required packages
     ~~~bash
     pip install -r requirements.txt
     ~~~
  4. Run the development server
     ~~~bash
     python manage.py runserver
     ~~~
  5. Open any browser and type http://127.0.0.1:8000/login/ or click [here](http://127.0.0.1:8000/login/)
## Usage
1. **Sign Up:**
- Navigate to the signup page.
- Fill in the required details and submit the form to create a new account.
2. **Log In:**
- Navigate to the login page.
- Enter your credentials and log in to the application.
3. **Create a Tweet:**
- Once logged in, you can create a new tweet by filling out the tweet form and submitting it.
4. **Edit a Tweet:**
- Navigate to the tweet you want to edit.
- Click the edit button, make your changes, and save the tweet.
5. **Delete a Tweet:**
- Navigate to the tweet you want to delete.
- Click the delete button to remove the tweet.
6. **View Other Users' Tweets:**
- Browse the homepage to see tweets from other users.

