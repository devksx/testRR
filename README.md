__Teacher Directory__
__Technical Assessment__

PROJECT DESCRIPTION
===================

This repository is containing Teacher Directory Web Application made using - Django framework of Python3. This Application will allow all site visitors to access the teacher directory and view individual teacher's informartion. Only authorized users can see upload files to import data. CSV file containing teachers records and ZIP file containing all images has to be used respectively for data import.

HOW TO RUN - INSTRUCTIONS
=========================
make sure you have following installed on your PC: git, python3 installed and added to environment variable PATH

1. Open git bash where you want to copy this code and clone this repository using ``$git clone "https://github.com/Karishma0210/testRR.git"`` command.
2. move to testRR/ using ``$cd testRR`` command and shift to master branch using ``$git checkout master``.
3. you can type `$ls` to comfirm whether you have teacherdir/ folder present and move to teacherdir using ``$cd teacherdir`` command.
4. install and create virtualenv on windows, type- ``$pip install virtualenv``, ``$pip install virtualenvwrapper-win``, ``$mkvirtualenv envname``* commands one after the other. <br/>or <br/>for linux, type- ``python -m venv envname``
5. To activate virtualenv on windows - ``$source envname/Scripts/activate``* <br/> for linux, ``$source envname/bin/activate``
6. make sure now you are in teacherdir where requirements.txt is also installed. install dependencies - ``$pip install -r requirements.txt``/ ``$python3 -m pip install -r requirements.txt`` (in case you have python2 and python3 both installed)
7. run ``$python manage.py migrate`` to migrate database files.
8. Run server using command - ``$python manage.py runserver`` and go to any browser to open url:127.0.0.1:8000/
<br/>
_*Any commands not found/ conflicting commands in windows might be due to path envirnments. so any command not working - just try writting command's actual path (e.g. ``$C:/Windows/System32/mkvirtualenv envname`` instead of ``$mkvirtualenv envname``*_.
<br/>
The Teacher directory Web App's home page has all the teachers, you can log in to the system using email - 'testuser@gmail.com' with password - 'testmode'.<br/>
Once logged in, you will be able to see import files and clear database buttons on home and teachers page.<br/>
You have to import csv and zip file as provided in technical assesement specifications.<br/>
The sample test files are given in sampleFiles folder in repository.

for any suggestions/ feedback/ issues on this project contact me on - karishma.sk02@gmail.com
<br/>

.
<br/>
.
<br/>
---Thank you---
