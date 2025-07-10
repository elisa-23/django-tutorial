# TUTORIAL

### How to Install Django?

1. Install Python

2. Setup Vitual Enviornment



        a. python -m venv venv (or whatever you like ) <!-- on macOS: python3 -m venv venv -->

        b. Windows: venv\Scripts\activate        <!-- how you activate Venv -->
           MacOS/Unix: source venv/bin/activate

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

## How to create a table for model?

        python manage.py makemigrations members (or whatever you named your child folder)

If it doesn't work look at settings.py to see if you added it to the installed apps

If it worked there should be a new file in your migrations folder.

Then run: 

        python manage.py migrate

## How to edit the data?

        python manage.py shell (run this first to activate the shell)
        >>> from members.models import Member (or whatever you named it)
        >>> Member.objects.all()

Returns: 

        <QuerySet []>

To add a record:

        >>> member = Member(firstname='Emil', lastname='Refsnes')
        >>> member.save()

To add multiple records at once:

        >>> member1 = Member(firstname='Tobias', lastname='Refsnes')
        >>> member2 = Member(firstname='Linus', lastname='Refsnes')
        >>> member3 = Member(firstname='Lene', lastname='Refsnes')
        >>> member4 = Member(firstname='Stale', lastname='Refsnes')
        >>> member5 = Member(firstname='Jane', lastname='Doe')
        >>> members_list = [member1, member2, member3, member4, member5]
        >>> for x in members_list:
        ...   x.save()
        ...
        >>>

To see table values:

        >>> Member.objects.all().values()

Other functions for the data: [text](https://www.w3schools.com/django/django_update_data.php)

To close py shell: run exit() or quit()