# display

display is an application to create profiles of a person and display them

# Dependecies

* python3
* pip
* virtualenv

# Build and Run

1. Clone the Repository

```shell
git clone https://github.com/an-isolated-pawn/city-mall-assignment
cd city-mall-assignment
```

2.Make virtual environment setup

```shell
virtualenv .venv
```

3.Activate your environment

```shell
source .venv/bin/activate
```

4.Install requirements

```shell
pip install -r requirement.txt
```

5.Create a MySql database named profile and a database user "ujjval" and password "Ujjval@123"


6.Migrate Files

```shell
python manage.py makemigrations
python manage.py migrate
```

7.Make a Superuser

```shell
python manage.py createsuperuser
```


Press Ctrl-D

8.Run the app(on localhost:8000)

```shell
python manage.py runserver
```