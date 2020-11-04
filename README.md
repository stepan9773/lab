# lab4 variant 8 (pipenv, python 3.7.*)

## Installing python 

firstly you must set a correct version of python on your machine 
we use a pyenv module to do this.

for linux

```
pip install pyenv 
``` 
for Windows

```
pip install pyenv-win
```
install correct vesion of python

```
pyenv install 3.7.6
```

## Copy repo from github

you must create folder on your machine and open there `cmd`, `powersell`,`bash`, or simple linux `terminal`
create a virtual eviroment by module pipenv or open a PyCharm on this folder and in venv options select pipenv.
and execute comand

```
git clone https://github.com/stepan9773/lab-4.git
```

## Execute app

so if you lucy owner linux machine, you must duwnloud a WSGI server

```
pip install gunicorn 
```
then update a requirements.txt in terminal
```
pipenv update 
```
and pipenv must automaticaly start installing all dependencies for project 

and finaly start a project app by command 
```
gunicorn --bind 0.0.0.0:5000 __init__:app
```

## How use 
On console you will see a HTTP path, execute it on browser and add to him `/api/v1/hello-world-8`.

You will see text messege `Hello World 8` on browser tab.
