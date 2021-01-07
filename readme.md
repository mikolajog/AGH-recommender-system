# Recommendation system for elective course selection

The application was created for my BSc. thesis "Recommendation system for elective course selection for AGH UST students"  in 2021.

## About project
Coming soon...

#### Run
1. Graph Database:
Install and run graph database from https://neo4j.com/download/ . Edit in flask-api/Neo4jConnector.py : config.DATABASE_URL with proper data. 

2. Back-end:
From the root directory:
```
cd flask-api
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
export FLASK_APP=app.py
flask run
```


3. Front-end:
From the root directory:
```
cd frontend
nvm use
npm install
npm start
```

In order to add fields of study use prepared script located at flask-api/db_scripts . 

## Author

* **Mikołaj Ogarek** - *Full-stack developer* 


