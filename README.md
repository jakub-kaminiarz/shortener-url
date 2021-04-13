CONTENTS OF THIS MAIN FOLDER
---------------------
- .gitignore
- Lib
- pyvenv.cfg
- README.md
- Scripts
- src
- urlshortener.sublime-project
- urlshortener.sublime-workspace

INTRODUCTION
------------
Project based on Python and django, shortening the URLs to more user-friendly, ready-to-use form.

REQUIREMENTS
------------
- python 3.8 or newer
- django 3 or newer

INSTALLATION
------------
Follow the official site instructions to install both: python (https://www.python.org/downloads/) and django (https://www.djangoproject.com/download/)

HOW TO RUN
------------
For Windows users ONLY !!! :

1) Unzip the downloaded zip file
2) Open Command Line
3) Navigate to the folder containing the unzipped file
4) Call the command: "url_shortenerScriptsactivate" to start the python virtual environment
5) call the command: "cd url_shortener\src",
6) call the command: "python manage.py runserver" to start the local server,
7) open a browser and paste the local site address: "http://127.0.0.1:8000"

HOW TO USE
------------
On the main page, the user can enter a URL (a long one that we want to shorten). 
The application validates the entered address (the requirements regulate the correctness of the entered address when it contains ".com"). 
An incorrectly entered address results in the "Invalid URL - no .com" message.
When the address verification is successful, a new view is displayed to the user.
Depending on whether the entered address exists in the database or not, the message will be displayed accordingly:
 - Object created successfully :) - when the address has not yet been found in the database,
 - Object already exists :( - if the address has already existed in the database
The user will be shown the previously entered URL link (with "http://" added if it does not exist).
It is possible to paste the generated link in the convention <127.0.0.1:8000>/<generated short code>.
Alternatively, the user can click on the "Or go directly to the link" link.
The user has the possibility to switch to the first view by clicking the "+New" link.

After going to "http://127.0.0.1:8000/admin" and logging in with:
login - jakubkam
password - Haslo123

We get access to the administrator panel. 
From this level, it is possible to view and edit the database of addresses along with the created short code.


