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
##### *Also download Elastic Search from the official website for the setup according to your os*
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


## Api endpoints 

```
GET http://127.0.0.1:8000/order_by_default
GET http://127.0.0.1:8000/data/?q=Viewcount
GET http://127.0.0.1:8000/data/?q=Score
GET http://127.0.0.1:8000/pages/<page-no.>/?q=ViewCount
GET http://127.0.0.1:8000/pages/<page-no>/?q=Score
GET http://127.0.0.1:8000/search/?q=<string-to-search>
GET http://127.0.0.1:9200/smart_search/questions/_search/?q=<string-to-search>

```

