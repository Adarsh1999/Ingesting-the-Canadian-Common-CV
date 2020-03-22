# Ingesting-the-Canadian-Common-CV
# Installation
### git clone the repo and come to the directory of the repo in your terminal
## Virtual Environment
```
sudo apt install python3-pip 
```
```
pip3 install --upgrade virtualenv
```
```
sudo apt install virtualenv
```
```
virtualenv -p python3 venv 
```
# Install Requirements
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```

# For running the django server
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py runserver
```



