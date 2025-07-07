# TUTORIAL

### How to Install Django?

1. Install Python

2. Setup Vitual Enviornment



        a. python -m venv myworld (or whatever you like )

        b. Windows: myworld\Scripts\activate        <!-- how you activate Venv -->
           MacOS/Unix: source myworld/bin/activate

3. Install Django


        python -m pip install Django

4. Install a Django Project 


        django-admin startproject my_tennis_club (or whatever you like)

5. Install Django App


        cd my_tennis_club (or whatever you named the project)
        python manage.py startapp members (or whatever you like)

## How to run project?

    python manage.py runserver      //on you r project so cd (project name if not on the branch)

## How to get all imports and reinstall on other devices?

    pip freeze > requirements.txt

On Other device:

    pip install -r requirements.txt (create venv first)