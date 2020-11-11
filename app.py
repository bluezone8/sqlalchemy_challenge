# Import SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# IMPORT SQLALCHEMY MODULES
from sqlalchemy.ext.declarative import declarative_base

# IMPORT PANDAS AND MATPLOTLIB
import matplotlib
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import pandas as pd

# IMPORT DATETIME AND NUMPY
import datetime as dt
import numpy as np



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    return(
        f"Welcome to the Home Page of the Climate Analysis API<br/>"
        f"Available Routes<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/2013-01-01<br/>"
        f"/api/v1.0/2013-01-01/2015-12-31"
    )

# First Route Query
# Define path
@app.route("/api/v1.0/precipitation")
# # Define the function to return the data from the database
def precip():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    ''' Return a Dictionary of All of the Preciptation Measurements for Last 12 Months'''

    # Create query for rainfall between the given dates and save to a dataframe
    precipdata_df=pd.read_sql_query('''
    SELECT date, prcp FROM measurement WHERE date BETWEEN '2016-08-23' AND '2017-08-23' ORDER BY date;''',con=engine)

    # Create a dictionary from the dataframe
    precipdata_dict=precipdata_df.to_dict(orient='index')

    # Close the database link session
    session.close()

    # return JSON of the dictionary data
    return jsonify(precipdata_dict)


# Second route query
# Define the path
@app.route("/api/v1.0/stations")
# Define the function to return the data from the database
def stat():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    ''' Return a List of All of the Weather Stations'''

    # Create query to return the names of all stations and save to a dataframe
    stationdata_df=pd.read_sql_query('''
    SELECT DISTINCT(station) FROM measurement;''',con=engine)

    # Create a list from the dataframe
    stationdata_list=stationdata_df.values.tolist()

    # Close the database link session
    session.close()

    # return JSON of the list data
    return jsonify(stationdata_list)

# Third route query
# Define the path
@app.route("/api/v1.0/tobs")
# Define the function to return the data from the database
def temp():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    '''Return All Dates and Temperature Measurements from the Most Active Station for the Last 12 Months'''

    # Create query to return the dates and rainfall for date range and save to a dataframe
    actstntemps_df=pd.read_sql_query('''
    SELECT date,tobs AS temps FROM measurement
    WHERE station='USC00519281' AND date BETWEEN '2016-08-23' AND '2017-08-23' ORDER BY date;''',con=engine)

    # Create a list from the dataframe
    actstntemps_list=actstntemps_df.values.tolist()

    # Close the database link session
    session.close()

    # return JSON of the list data
    return jsonify(actstntemps_list)

# Fourth route query
# Define the path 
@app.route("/api/v1.0/2013-01-01")
# Define the function to return the data from the database
def startdate():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    '''Return Minimum, Average, and Maximum Temperatures for Period After 2013-01-01'''

    # Create query to return the dates and rainfall for date range and save to a dataframe
    strtdattemps_df=pd.read_sql_query('''
    SELECT date, MIN(tobs),AVG(tobs),MAX(tobs) FROM measurement
    WHERE date >= '2013-01-01'
    GROUP BY date
    ORDER BY date;''',con=engine)

    # Create a list from the dataframe
    strtdattemps_list=strtdattemps_df.values.tolist()

    # Close the database link session
    session.close()

    # return JSON of the list data
    return jsonify(strtdattemps_list)


# Fifth route query
# Define the path 
@app.route("/api/v1.0/2013-01-01/2015-12-31")
# Define the function to return the data from the database
def startend():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    '''Return Minimum, Average, and Maximum Temperatures for the Date Range 2013-01-01 to 2015-12-31'''

    # Create query to return the dates and rainfall for date range and save to a dataframe
    strtendtemps_df=pd.read_sql_query('''
    SELECT date, MIN(tobs),AVG(tobs),MAX(tobs) FROM measurement
    WHERE date BETWEEN  '2013-01-01' AND '2015-12-31'
    GROUP BY date
    ORDER BY date;''',con=engine)

    # Create a list from the dataframe
    strtendtemps_list=strtendtemps_df.values.tolist()

    # Close the database link session
    session.close()

    # return JSON of the list data
    return jsonify(strtendtemps_list)   

# execute the app
if __name__ == '__main__':
    app.run(debug=True)