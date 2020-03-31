# Ingesting-the-Canadian-Common-CV
# Installation
```
git clone https://github.com/Adarsh1999/Ingesting-the-Canadian-Common-CV.git
```
* #### There are 2 methods to run the project 1. docker file and another manual setup.

# Method 1: For Running project From Docker File


### Creating a Database (Sqlite3)

```
 docker-compose up
```
# Method 2: By setting up project manually

### *Setting Environment Variables*
```
shell
export ES_HOST="localhost"
export ES_PORT="9200"
```
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

##### *For setting up Elastic Search in Windows*
Download msi package from https://www.elastic.co/guide/en/elasticsearch/reference/current/windows.html

#### For checking Elastic search is working
Go to browser and paste this ` localhost:9200/ `
## Install Requirements
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```
 ```
 sudo apt-get install -y sqlite3 libsqlite3-dev
 ```
```
sqlite3 db.sqlite3 ".database"
 ```

## For running the django server
```
python populate.py
```
```
python manage.py migrate
```
```
python manage.py runserver
```


