### Installation

##### install python3 for you platform

##### clone the repo and change into the root folder

```
git clone git@github.com:iamkhaya/ubausa.git
cd ubuasa
```

##### install and activate a virtual environment for your platform

```
python3 -m venv venv
source ./venv/bin/activate
```

##### install requirements
```
pip install -e .
```

##### create dummy  data (make sure you have a mysql database called `ubausa` )
```
python manage.py seed_app
```

##### run the application
```
python manage.py runserver
```


###### login
browse to `http://localhost:8000/backend` with credentials

```
test_1.ubausa.com, test
```

browse to `http://localhost:8000/backend/admin` with credentials

click on the cards or client link
