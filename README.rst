=====================================
Installing This Wireframe from Source
=====================================

Get the source
==============

Create and cd to a nice spot to check it out the code::

    mkdir -p ~/my_projects/AI5_wireframe/
    cd ~/my_projects

(Of course, switch out "my_projects" with whatever you call your main source directory,
and "AI5_wireframe" with whatever you want the root of the source tree for this wireframe
to be called)

Clone the repo
--------------

from github::

    git clone https://github.com/jkafader/archiveit.git



Install Python 3.3
==================

https://www.python.org/downloads/release/python-335/

I downloaded the python 3.3.5 installer dmg. Run through the steps for the installer, 
then locate the python3.3 executable it installed. You'll use it when creating a virtualenv
below.



Install virtualenv Globally
===========================

Use the freshly-installed python3.3 to install virtualenv globally::

    pip3.3 install virtualenv



Create a virtualenv in working directory
=========================================

In your working directory, you'll now need a complete virtualenv. This is how you 
initialize the virtualenv to work with python3.3::

    virtualenv -p /path/to/python3.3 AI5_wireframe



Install binary packages with pip
================================

Now the pip magic happens. Use it to initialize the entire set of packages you'll need
to run the dev server::

    cd AI5_wireframe

    source bin/activate

    pip install -r requirements.txt



Start a Django server
=====================

Finally, you'll need to initialize the django environment. First, cd to the directory 
containing manage.py::

    cd wireframe

Then, tell django to initialize the database. This will allow you to create a superuser
account for yourself at the same time::

    python manage.py syncdb

    (create yourself a superuser)

Now, update the initialized database to the current South migration state::

    python manage.py migrate archiveit

    python manage.py migrate accounts

Finally, run the server process::

    python manage.py runserver_plus

This should tell you that you have a server running on 127.0.0.1:8000



Initialize the application state
================================

1. Point your browser to http://localhost:8000/admin

2. Login with your superuser credentials from "Start a Django Server" above.

3. Navigate to the account creation screen, http://localhost:8000/admin/accounts/account/add

4. Fill in the form, Creating a StorageQuota with the [+] button.

5. Create a User Profile for your super user, http://localhost:8000/admin/accounts/userprofile/add
   (this is basically a pointer from your user object to your account object. It's based
   on an older django approach of using a OneToOneField to extend Users, rather than
   subclassing an abstract User class. This approach is deprecated and will be fixed.)




Navigate to the wireframe app
=============================

1. Point your browser to http://localhost:8000/


