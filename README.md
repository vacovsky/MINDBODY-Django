# mboapi-django
A demonstration showing how to build an integration with the MINDBODY SOAP API using Python 3 and Django 1.8.  I did this in my spare time, so bugs are likely.  I'll try to fix them as I find them.

https://mboapi-django.herokuapp.com


## Initial Setup - Linux 
###### (If someone wants to make a quick setup for windows, that would be helpful.)


### Step 1. Create a virtual environment in the root fof the project folder

```
virtualenv -p /usr/bin/python3.4 venv
```

### Step 2. Activate the virtual environment

```
. venv/bin/activate
```

### Step 3. Install required modules using pip

```
pip install -r requirements.txt
```

### Step 4. Populate the mboapi_djangodemo/SECRETS.py file with your credentials

```
SOURCENAME = 'yousourcename'  #SourceName to be used in all API Calls in this project
SOURCEPASS = 'yoursourcepass'  #SourceName Password to be used in all API calls

# (this should be populated from some other place, not hard coded.  However, since this is just a demonstration, you can of course plop them in here and make API calls until the cows come home.)

USERNAME = 'youruser'  
USERPASS = 'yourpass'  # staff credentials, etc

# SiteIDs to be used in all API Calls - should ALWAYS match for SourceCredentials and UserCredentials nodes.  If you are new to the MINDBODY API, you should probably use site ID -99 until you have everything coded the way you like it.  Otherwise, charges could be incurred.
SITEIDs = []


# optional stuff if you have a mail service.  handles contact form stuff, and whatever else the developer decides to hook up.  Form for comments is disabled because I didn't want anyone abusing it.

MAIL_SERVER = ''
MAIL_SERVER_USER = ''
MAIL_SERVER_PASS = ""
MAIL_SERVER_ADMIN = ''  #email address of mail administrator

# !!!!!! DO NOT FORGET TO SET THIS!!!!!!  
# This is what protects your session data, cookies, etc.  Very important that it's STRONG!
APPLICATION_SECRET = ""
```

### Step 5. If all the modules installed, you should be able to fire up the application.  

######While in your virtual environment, run
```
python3 manage.py syncdb
python3 manage.py runserver
```

### Step 6. Once the application is running, browse to localhost:8000 to see the results.
