***Chapter I:***


Login / Password admin: admin / 7486

Available users are:
student1, student2, teacher1, teacher2 and admin
The login password for students and teachers is the same: skygate1337

The administrative panel is available here: localhost: 8000 / admin

First link to the API - http: // localhost: 8000 / api / examsheets / - here I used the search by overriding the get method. Typing pk at the end of the link gives you the option of editing a given sheet.

?title=query
?author=query

results are displayed in order, sorting by pk.

Second link to API - http: // localhost: 8000 / api / examsheets / exam / - own search here. The code can be found in exam_sheets / api / filters.py

I assumed that only an administrator can archive and delete sheets. In the current version of the code, archiving does not cause anything - I have not added a filter for teachers that would hide the search results in front of them.



I also attach a database backup. It is in the "database_backup" folder - I left the data to connect to the database intentionally in the settings file - normally I would throw it outside and add a file that stores this data to .gitignore

database name: skygate,
user: skygate,
pass: 1234.


Additional Python modules that I used in the project are in the requirements.txt file