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
<br/>
fullscreen view of the web app
<img width="2047" alt="Screen Shot 2019-11-11 at 5 18 20 PM" src="https://user-images.githubusercontent.com/45185244/68626450-63e29800-04a9-11ea-9b69-50a671286e5d.png">

<br/>
filtering by mineral group
<img width="518" alt="Screen Shot 2019-11-11 at 5 19 48 PM" src="https://user-images.githubusercontent.com/45185244/68626480-74930e00-04a9-11ea-9011-a2d9fd9e8da4.png">

<br/>
filtering by mineral colour
<img width="518" alt="Screen Shot 2019-11-11 at 5 20 11 PM" src="https://user-images.githubusercontent.com/45185244/68626503-7f4da300-04a9-11ea-9186-c4e0bce2c950.png">

<br/>
searching all fields for terms
<img width="518" alt="Screen Shot 2019-11-11 at 5 20 39 PM" src="https://user-images.githubusercontent.com/45185244/68626530-8a083800-04a9-11ea-92a9-a702ec4554e1.png">

<br/>
responsive view
<img width="413" alt="Screen Shot 2019-11-11 at 5 21 50 PM" src="https://user-images.githubusercontent.com/45185244/68626710-f5eaa080-04a9-11ea-9037-d21091d5e786.png">

<br/>
responsive view 2
<img width="413" alt="Screen Shot 2019-11-11 at 5 22 15 PM" src="https://user-images.githubusercontent.com/45185244/68626729-000c9f00-04aa-11ea-8676-e599fad045f9.png">


