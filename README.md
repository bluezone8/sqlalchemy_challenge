# SQL ALCHEMY CHALLENGE
___________
### Purpose
The purpose of this repository is to store files related to the Hawaii Climate Analysis  
___
### Analytical Tool Choice and Rationale
This analysis utilized 2 primary tools and quite a number of subordinate tools.  
1.  The first tool utilized is a an SQL database in the form of an SQLite file. This file is used to maintain the weather data used for the analysis.  
2.  The second tool utilized is Python.  Within Python, a number of modules were used to provide specific functionalities to certain parts of the analysis.  Pandas was used to provide functionality for converting the database data to a format that is readily accesible and able to be analyzed in Python, namely dataframes. Matplotlib provided the charting functionality for the included figures and Numpy was used to provide some numerical calculation functionality.  SQL Alchemy was ultilized to provide a connection to the database through Python which allowed for the ability to query the data in the database directly from Python. This precluded the need to have to work in multiple applications simultaneously (ie the need to query the database from the database application and do additional analysis in python).  Flask was used to facilitate the ability to create a web api to access certain parts of the data analysis from the web.  
____
### Approach
In general, there is little about the analysis that involves a choice of preference in different approaches.  However, there is one noteworthy area in which this choice is true. In querying the database from Python, persoinal preference will dictate whether one will utlize exclsively Python code or call SLQ queries from Python.  For this analysis, the choice was made to go with the latter option to maximize the value of the analysis as a learning exercise. 

An additional point worth noting is the inclusion of the Bonus Challenge analysis for the same aforementioned reason.  
__________
### Included Items
1.  The Jupyter Notebook containing all of the code for th initial analysis as well as the Bonus analysis.  (climate_starter.ipynb)  
2.  A copy of the Jupyter Notebook exported as an HTML file to facilitate viewing the Notebook in color in a browser without opening Jupyter notebooks.(climate_starter.html) 
3.  The Python application that creates the web api to access some of the data analysis from a web site. (app.py)
