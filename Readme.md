[//]: <> (Titles)
# RestApi:
-The goal of the task is to build a simple backend application that accepts valid German
license plates, stores them in a database and provides an endpoint to retrieve all stored
plates. Secondly, we want to build a similarity search over the database .

# Main libraries used:

 1. Flask - Web framework for python
 2. Flask-SQLAlchemy- adds support for SQLAlchemy ORM.



### Requirements
- python 3.8 or above

### Setting up Environment
- Create virtual environment
```
 python venv venv   

```
- Activate virtual environment
```
 venv/Scripts/activate.bat

```
-install requirements
```
pip install -r app/requirements.txt
```

**Available Configuration Parameters**

This data can be got by running `python app/config.py`

Need to change this environment variable in docker-compose file 
```
user_name: <class 'str'>
password: <class 'str'>
host: <class 'str'>
db_name: <class 'str'>
port: <class 'int'>
```


| Parameter | datatype | Description| Required | Default |
| - | - | - | - | - |
|user_name| string | user_name to connect postgres| true | |
|password | string | password to connect postgres | true | |
|host | string | host to connect postgres | true | |
|db_name | string | database to connect postgres | true | |
|port | integer | Port for RabbitMQ | false | 5432 |

**app**

## Users endpoint

### POST http://localhost:5002/plate

### REQUEST
    {
        "plate": "M-BB123"
    }
### RESPONSE
    {
    "message": "car plate number added to database successfully!"
    }



### GET http://localhost:5002/plate

### RESPONSE
       {
      "car_details": [
        {
          "plate": "A-B123",
          "timestamp": "2022-09-29T12:53:26Z"
        }
      ]
    }

### GET http://localhost:5002/search-plate?key=ABC123&levenshtein=4

### RESPONSE
    {
    "ABC123": [
        {
            "plate": "BFB23",
            "timestamp": "2022-09-27T12:47:09Z"
        },
        {
            "plate": "BFB23",
            "timestamp": "2022-09-27T13:08:12Z"
        }
    ]
}

**Using with Docker-Compose**

- Build docker image

```
docker-compose build
```

- Start docker-compose

```
docker-compose up -d
```

### Logging

- To log the log information and exception.All log information are captured in log.txt file.



### Unit Test

- Unit test are integrated for each component of the Tool. Unit test can be run using below command.
- Unit testing requires postrges and flaskapi to be running in docker container

```
python app/test_api.py
```


### swagger

### url : http://localhost:5002/
