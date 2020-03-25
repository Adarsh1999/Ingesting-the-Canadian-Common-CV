# Ingesting-the-Canadian-Common-CV
# Installation
#### git clone the repo and come to the directory of the repo in your terminal

# For Running project From Docker File

## Running the Project
### *Setting Environment Variables*
```
shell
export ES_HOST="localhost"
export ES_PORT="9200"
```

### *Creating a Database (Sqlite3)*
```
sqlite3 db.sqlite3 ".database"
 ```
```
 docker-compose up
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
# Install Requirements
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```

# For running the django server
```
python populate.py
```
```
python manage.py migrate
```
```
python manage.py runserver
```


# Api endpoints 

```
GET http://127.0.0.1:8000/order_by_default
GET http://127.0.0.1:8000/data/?q=Viewcount
GET http://127.0.0.1:8000/data/?q=Score
GET http://127.0.0.1:8000/pages/<page-no.>/?q=ViewCount
GET http://127.0.0.1:8000/pages/<page-no>/?q=Score
GET http://127.0.0.1:8000/search/?q=<string-to-search>
GET http://127.0.0.1:9200/smart_search/questions/_search/?q=<string-to-search>



```

