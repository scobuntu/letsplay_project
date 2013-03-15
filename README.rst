=======================
Setup Instructions
=======================

Run the following to get started. 

    username: eplayground
    password: letsplay

    Run the server 

    - python manage.py runserver

=======================
Troubleshooting
=======================

Q. I deleted the database file, how do I get the content back?

A. First, sync the database: 
       
       > python manage.py syncdb

   Use the content_fixture.json to load the sample data. 

       > python manage.py loaddata content_fixture.json  