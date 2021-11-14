# Load libraries
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Create the database engine
engine = create_engine("sqlite:///data.db")
# View the tables in the database
print(engine.table_names())


# Load hpd311calls without any SQL
hpd_calls = pd.read_sql('hpd311calls', engine)
# View the first few rows of data
print(hpd_calls.head())

# Create a SQL query to load the entire weather table
query = """
SELECT * 
  FROM weather;
"""
# Load weather with the SQL query
weather = pd.read_sql(query, engine)
# View the first few rows of data
print(weather.head())

# Write query to get date, tmax, and tmin from weather
query = """
SELECT date, 
       tmax, 
       tmin
  FROM weather;
"""
# Make a data frame by passing query and engine to read_sql()
temperatures = pd.read_sql(query, engine)
# View the resulting data frame
print(temperatures)

# Create query to get hpd311calls records about safety
query = """
SELECT *
FROM hpd311calls
WHERE complaint_type = 'SAFETY';
"""

# Query the database and assign result to safety_calls
safety_calls = pd.read_sql(query, engine)

# Graph the number of safety calls by borough
call_counts = safety_calls.groupby('borough').unique_key.count()
call_counts.plot.barh()
plt.show()

# Create query for records with max temps <= 32 or snow >= 1
query = """
SELECT *
  FROM weather
  WHERE tmax <= 32
  OR snow >= 1;
"""
# Query database and assign result to wintry_days
wintry_days = pd.read_sql(query, engine)
# View summary stats about the temperatures
print(wintry_days.describe())