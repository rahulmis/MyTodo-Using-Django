# MyTodo-Using-Django
* This is a Simple Todo Web App using Django where we can add some tasks, mark as complete and we can delete tasks *

# Deployed Project Link - 
> [Link of Deployed Project on Heroku - Click Here](https://mytodo2021.herokuapp.com/)

![Demo Image](https://github.com/rahulmis/MyTodo-Using-Django/blob/main/demo1.png)


## You have to follow following steps to run this project

### 1. Run this command on your terminal 
       1. git clone https://github.com/rahulmis/MyTodo-Using-Django.git
       2. cd MyTodo-Using-Django
### 2. Create virtual enviroment to install required libraries 
       1. pip install virtualenv
       2. virtualenv venv
       3. pip install -r requirements.txt
### 3. Now Run the project
       1. python manage.py makemigrations
       2. python manage.py migrate
       3. python manage.py create superuser
       4. python manage.py runserver
### 4. Open Link And Access Admin Page
open this link on your browser `http://127.0.0.1:8000/`

* To Access Admin Page goto `http://127.0.0.1:8000/admin` and enter `username` and `password` of your superuser
