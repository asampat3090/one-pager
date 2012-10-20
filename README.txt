Automated One-Pager README

Setting up the computer: 

	1.	Make sure Python is installed (python 2.6.5 - 2.7 is best; just not python 3 as there are some minor differences)
	2.	Make sure Django is installed 
		⁃	visit https://docs.djangoproject.com/en/dev/topics/install/ for full details

Setting up the database (Note, we are using a sqlite3 database created locally for ease of access - just a path is required): 

	1.	Open up 'one_pager/settings.py' from the project root
	2.	Edit the 'NAME' parameter within DATABASES to point a local .db file. Use the file systems absolute path. (ex. /Users/asampat3090/django_projects/proj-data.db) - note that the file does not not need to exist; if it doesn't it will be created.

Run the development server: 

	1.	Navigate to project root (there should be a manage.py file within it)
	2.	Run the command 'python manage.py runserver'. - This will start a development server at http://127.0.0.1:8000

Usage Instructions: 

Adding Tasks, SubTasks, and Meetings:

	1.	In a browser, navigate to http://127.0.0.1:8000/admin/auto_one_pager_app
	2.	You can add new Tasks, SubTasks, and Meetings by clicking 'Add New' next to the corresponding item
	3.	You can click on the items themselves to obtain a list of Tasks, SubTasks, or Meetings
		⁃	You can edit the actual time spent throughout the week and update the value

Exporting the Tasks at the end of the week: 

	1.	In a browser, navigate to http://127.0.0.1:8000/auto_one_pager_app. You should see a "File Exported!" message.
	2.	Navigate to the project root to access the 'one_pager.txt' file.