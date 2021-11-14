import requests
import pandas as pd
import matplotlib.pyplot as plt


# Load the daily report to a data frame
pop_in_shelters = pd.read_json('dhs_daily_report.json')
print(pop_in_shelters.describe())

try:
    # Load the JSON with orient specified
    df = pd.read_json("dhs_report_reformatted.json",
                      orient="split")

    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census",
            y="total_individuals_in_shelter")
    plt.show()

except ValueError:
    print("pandas could not parse the JSON.")


api_url = "https://api.yelp.com/v3/businesses/search"
headers = {"Authorization": "Bearer {}".format(api_key)}
params = {"term": 'cafe', "location": "NYC"}

# Get data about NYC cafes from the Yelp API
response = requests.get(api_url,
                        headers=headers,
                        params=params)
# Extract JSON data from the response
data = response.json()
# Load data to a data frame
cafes = pd.DataFrame(data['businesses'])
# View the data's dtypes
print(cafes.dtypes)


# Create dictionary to query API for cafes in NYC
parameters = {"term": 'cafe',
              "location": "NYC"}
# Query the Yelp API with headers and params set
response = requests.get(api_url,
                        headers=headers,
                        params=parameters)
# Extract JSON data from response
data = response.json()
# Load "businesses" values to a data frame and print head
cafes = pd.DataFrame(data["businesses"])
print(cafes.head())
