=======================
Setup Instructions
=======================

Run the following to get started. 
    
    Create the database

    - python manage.py syncdb
    
    Load the sample data provided 

    - python manage.py loaddata content_fixture.json 

    Run the server 

    - python manage.py runserver 

=======================
Django Project Template
=======================

This is basic Django project template.

Project layout
==============

{{ project_name }}/settings/
    contains project settings for production and development

requirements/
    contains project requirements for production and deveopment

templates/
    project wide templates (404 and 500 included)

static/
    for storing project-wide static files

public/
    default destination for ``collectstatic``

