from flask import Flask, Response
import xml.etree.ElementTree as ET

app = Flask(__name__)



# GET request to fetch all books in XML format
@app.route('/', methods=['GET'])
def welcome():
    return "welcome to pyhton web service"

if __name__ == '__main__':
    app.run()
