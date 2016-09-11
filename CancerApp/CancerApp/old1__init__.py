import flask
from flask import Flask
import numpy as np
import pandas as pd

#--------- MODEL IN MEMORY --------------#

# Read the scientific data on breast cancer survival, 
# Build a LogisticRegression predictor on it

def data_read():
    patients = pd.read_csv("haberman.data", header=None)



#--------- URLs and WEB PAGES -----------#
app = Flask(__name__)

# Homepage
#@app.route("/")
#def hello():
#    return "adding comments - copied data over!"

def viz_page_example():
    """
    Homepage:  server our visualization page, awesome.html
    """
    with open("awesome.html", 'r') as viz_file:
         return viz_file.read()

#viz_page_example()

@app.route("/")
def viz_page():
    """
    Homepage:  server our visualization page, awesome.html
    """
    #viz_page_example()
    filen = "awesome.html"
    #with open("awesome.html", 'r') as viz_file:
    #     return viz_file
         #return viz_file.read()

    #return filen
    #return "take 8"
    return "yes"
    #return 

if __name__ == "__main__":
    #app.run()
    app.run(debug = True)



