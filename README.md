# MineralSearch

MineralSearch (based off of the Mineral Catalog project) is a simple Django app that displays over 800 minerals and their attributes. Mineral data is loaded into the database from a Json file. Attributes are shown if they're available. Minerals can be sorted/filtered by first letter, colour, group, and search term. There's a random feature that retrieves a random mineral in the database and displays its attributes. 


<br/>

# installation

1. cd into your directory of projects (or wherever you prefer to keep your clones)
2. git clone ```https://github.com/Marksparkyryan/MineralSearch.git``` to clone the app
3. ```virtualenv .venv``` to create your virtual environment
4. ```source .venv/bin/activate``` to activate the virtual environment
5. ```pip install -r MineralSearch/requirements.txt``` to install app requirements
6. cd into the MineralSearch/mineralsearch directory
7. ```python manage.py migrate``` to apply the existing data and model migrations
8. ```python manage.py runserver``` to serve the site to your local host (in DEBUG mode)
9. visit ```http://127.0.0.1:8000/``` to see some minerals! 


<br/>

# usage

By default, DEBUG mode is set to True in settings.py. This is good for testing but not good for deployment. If deploying, make sure
DEBUG is set to False and secrets are stored correctly.

By default, there is a django-debug-toolbar app installed for continued testing. Remove from installed apps in settings if required.


<br/>

# screenshots
