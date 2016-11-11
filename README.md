# NotesApplication
## The Application is a CLI(Command line Interface) app built using python and postgresql.
## It has the following features:
1. A user creating a note
2. A user browsing through the notes
3. Getting rid of a note
4. Searching for a note
5. Importing notes from a csv file
6. Exporting notes to a csv file
7. Synchronising notes with firebase.

# Dependencies
## There are quite a number of modules the app employs including:
1. docopt: A tool for commandline argument parsing and implementations.
2. psycopg2: A postgresql database Adapter library for python
3. pyfiglet: A library to aid in beautification and user Interface for a command line App.
4. tabulate: A module to Pretty-print tabular data in Python.
5. termcolor: A library to provision a rich aid in colors regarding CLI.
6. python-firebase: A helper to making API requests to firebase

# Installation and Setup
*Navigate to a directory of your choice on the terminal
* Clone the respository
* Navigate to the repo's folder on your computer
* Using virtual environment: pip install -r requirements.txt
* Next is to set up the databse by exporting the db.sql file into postgresql and the way to do it is just issue the folowing command in while inside the repo directory: psql -h hostname -d databasename -U username -f db.sql.
* Find the functions.py file and pass the credentials regarding a username and password for accessiblity of the database by the application. 
*Acivate the virtual environment by issuing the following command: . venv/bin/activate
* Run the app by keying in the following command on terminal(when the virtual environment is activated): python my_program.py -i

# Thats it!

