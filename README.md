# Django Unicorn Comment Demo

This is a small demo project showcasing the dynamic capabilities of Django Unicorn, a library that integrates Django with the Unicorn web server. The demo includes a simple comment system with full CRUD (Create, Read, Update, Delete) functionality.

## Features

- Real-time updates: The demo leverages Django Unicorn to provide real-time communication between the server and the client, allowing for instant updates without page reloads.
- Comment creation: Users can enter a new comment and add it to the comment list.
- Comment deletion: Users can delete individual comments or all comments at once.
- Comment editing: Users can edit existing comments and update them in real-time.

## Installation

1. Clone the repository
2. Create a virtual environment

   `python3 -m venv myenv`

3. Activate the virtual environment:

- On macOS and Linux:
  ` source myenv/bin/activate`
- On Windows:
  ` myenv\Scripts\activate`

4. Install the required dependencies:

   ` pip install -r requirements.txt`

5. Create an env.py file in the project root directory:

   ` touch env.py`

6. Add the necessary environment variables:

   `import os`

   `os.environ.["SECRET_KEY]="your_secret_key_here"`

7. Apply database migrations:

   ` python manage.py migrate`

8. Run the development server:
   `python manage.py runserver`
