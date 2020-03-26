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
##### *Setting up Elastic Search*
```
sudo apt update
sudo apt install apt-transport-https
sudo apt install openjdk-8-jdk
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
sudo sh -c 'echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" > /etc/apt/sources.list.d/elastic-7.x.list'
sudo apt-get update && sudo apt-get install elasticsearch
sudo systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service
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

 1. Endpoint to return posts in `chronological order`
GET http://127.0.0.1:8000/default/
2. Endpoint to return posts in `order by viewcount`
GET http://127.0.0.1:8000/data/?q=view-count
3.  Endpoint to return posts in `order by score`
GET http://127.0.0.1:8000/data/?q=score
4. Endpoint to return posts in **paginated** `order by viewcount`
GET http://127.0.0.1:8000/pages/`page-no`/?q=view-count
> *Dont forget to replace `page-no` by page-number example 1,2,3...
5. Endpoint to return posts in **paginated** `order by score`
GET http://127.0.0.1:8000/pages/`page-no`/?q=view-count
> *Dont forget to replace `page-no` by page-number example 1,2,3...
6. Display Answers endpoint
The Display answers endpoint is a very sophisticated endpoint having the following features:
- Display Answers based on question id having one or more answers.
>GET http://127.0.0.1:8000/answers/id/?id=<answer-id>
- Display Answers based on question id having no answers.
>GET http://127.0.0.1:8000/answers/id/?id=<answer-id>

