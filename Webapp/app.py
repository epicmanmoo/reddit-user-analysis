from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to AWS RDS Database
connectionRoute = open('DBCredentials.txt', "r")
path = connectionRoute.read()

app.config['SQLALCHEMY_DATABASE_URI'] = path



db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
