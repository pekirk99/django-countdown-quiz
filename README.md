# Django Quiz Game with a Countdown Timer

A simple Django quiz game project with dynamic questions and a countdown timer. This project demonstrates Django fundamentals like models, views, templates, and JavaScript integration for interactive features.

---

## Features

- Dynamic quiz questions with multiple-choice options.
- Countdown timer for added challenge.
- Automatic score calculation.

---

## Setup Instructions

### 1. Create a Virtual Environment

- Create and activate a virtual environment to isolate dependencies.
- Install Django.

### 2. Set Up the Project

- Use `django-admin` to create the project and app.
- Add the app to `INSTALLED_APPS` in the project settings.
- Verify the setup by starting the server.

### 3. Create the Question Model

- Define a model to store quiz questions, options, and the correct answer.
- Apply migrations to update the database schema.
- Register the model in the Django admin for easy question management.

---

## Views and URLs

- Create a view to display quiz questions, accept answers, and calculate the score.
- Map the view to a URL in the app's `urls.py`.
- Include the app's URLs in the project's main `urls.py`.

---

## Templates

### Quiz Template

- Create a template to dynamically render questions and options.
- Add a JavaScript countdown timer to enforce a time limit.

### Result Template

- Create a template to display the user's score after quiz submission.

---

## Run and Test

- Start the development server.
- Visit the app in your browser to test the quiz functionality.

---

## Demo

![image](https://github.com/user-attachments/assets/b0b5fc93-31d2-4ca9-9c7d-3dfa8fb936fd)
![image](https://github.com/user-attachments/assets/f9bd3bbb-8a70-44e0-b81e-bbdf30dbe6b6)
![image](https://github.com/user-attachments/assets/34d8626e-7c16-493b-82da-1b9316df69c0)
![image](https://github.com/user-attachments/assets/3ce65d63-abf9-40e8-a580-d3135ace0b5f)

---

## Future Enhancements

- Add user authentication to track individual scores.
- Implement a leaderboard for competitive play.
- Organize questions into categories or difficulty levels.

---

This README provides a high-level overview of the project and its setup. For more detailed implementation, refer to the source code in this repository.
