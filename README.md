### CRUDApplication
 Test task CRUD application

### Instruction manual (windows)

#### 1. Install Python MySQL, Git

#### 2. Setup virtual environment
```bash
# Create virtual environment
>>>python -m venv venvcrud

#Activate virtual environment
>>>venvcrud\Scripts\activate.bat
```

#### 3. Clone git repository
```bash
git clone "https://github.com/Manisha-Bayya/simple-django-project.git"
```

#### 4. Install requirements
```bash
cd CRUDApplication
pip install -r requirements.txt
```

#### 5. Edit project settings

Edit Database configurations with your MySQL configurations in the file CRUDApplication/UsersAPI/settings.py 
Search for DATABASES section.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'usersdb',
        'USER': '<mysql-user>',
        'PASSWORD': '<mysql-password>',
        'HOST': '<mysql-host>',
        'PORT': '<mysql-port>',
    }
}

#### 6. Load sample data into MySQL
```bash
# open mysql bash
mysql -u <mysql-user> -p

# Give the absolute path of the file
mysql> source ~/CRUDApplication/MySQL.sql
mysql> exit;

```

#### 7. Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver
```

#### 8. Check Api by Postman or Python Requests Library
```bash
# Install Requests Library
>>>pip install requests
>>>import requests

# User registration http://127.0.0.1:8000/api/v1/users/
>>>response = requests.post("http://127.0.0.1:8000/api/v1/users/",  data={'username':'user1', 'password': 'passWord1'})
>>>response.text
'{"id":14,"username":"user1","first_name":"","last_name":"","is_active":true,"last_login":null,"is_superuser":false}'

# Get a token http://127.0.0.1:8000/api-token-auth/
>>>response = requests.post("http://127.0.0.1:8000/api-token-auth/",  data={'username':'user1', 'password': 'passWord1'})
>>>response.text
'{"token":"b55b3833cfefdcbe702fc16485c4fbb69fbe50a8"}'

# Make changes with PUT http://127.0.0.1:8000/api/v1/users/14/
>>>response = requests.put("http://127.0.0.1:8000/api/v1/users/14/", headers = {'Authorization': 'token b55b3833cfefdcbe702fc16485c4fbb69fbe50a8'},  data={'username':'user1', 'password': 'passWord1', 'first_name': 'user14' })
response.text
'{"id":14,"username":"user1","first_name":"user14","last_name":"","is_active":true,"last_login":null,"is_superuser":false}'

# Make changes PATCH 
>>>response = requests.patch("http://127.0.0.1:8000/api/v1/users/14/", headers = {'Authorization': 'token b55b3833cfefdcbe702fc16485c4fbb69fbe50a8'},  data={'last_name': 'last user14' })
>>>response.text
'{"id":14,"username":"user1","first_name":"user14","last_name":"last user14","is_active":true,"last_login":null,"is_superuser":false}'

# Delete the user
>>> response=requests.delete("http://127.0.0.1:8000/api/v1/users/14/", headers = {'Authorization': 'token b55b3833cfefdcbe702fc16485c4fbb69fbe50a8'})
```
