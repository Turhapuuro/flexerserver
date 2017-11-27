# Installation instructions (macOSX)

## Python

Check python3 is installed by typing ``` python ``` in terminal.
If python is not installed install it from here https://www.python.org/downloads/


## Backend (macOSX)

1. clone the project
```
git clone https://github.com/Turhapuuro/flexerserver.git
```

2. go inside the cloned project folder
	cd flexerserver

3. create virtual env
	python3 -m venv ~/.virtualenvs/flexerdev

4. activate virtual env
	source ~/.virtualenvs/flexerdev/bin/activate

5. install django to the env
	pip install django

6. test virtual env that django has been installed
	python
	>> import django
	>> print(django.get_version())
	1.11.7 # should print django version here
	(press CTRL + D to exit)

7. launch server
	python manage.py runserver

8. open browser and type in the url bar localhost:8000
	browser should display the application