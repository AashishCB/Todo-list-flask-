# Todo list
Manage your work by adding things needed to be done, mark them on completion, delete when unnecessary.

### Required dependencies to install on your virtual environment or the system

#### flask
` pip install flask `

#### flask_sqlalchemy
` pip install flask-sqlalchemy `

#### flask_migrate
` pip install Flask-Migrate `

#### flask_login
` pip install flask-Login `

#### flask_wtf
` pip install Flask-WTF `

#### wtforms.validators
` pip install wtforms-validators `

#### wtforms
` pip install WTForms `

> project will throw errors in case all dependencies are not installed.

--------------------------------------------------------------------

### To run the project,

1. Open the cmd or terminal in the project folder where app.py file is located.

2. Run the following commands to setup the database,

` flask db init `

` flask db migrate -m "new tables" `

` flask db upgrade `

> The following process should not throw any errors, warnings can be ignored.

3. After that, you will see new folders and files inside the project, which does means that database has been set.

4. Run the below command to start the project.

` python app.py `

or 

` python3 app.py `

5. Now you will see link like 'http://127.0.0.1:5000/' or something like that, open the link in browser

6. You will reach the home page of the project and you will have your todo list web app ready to use.