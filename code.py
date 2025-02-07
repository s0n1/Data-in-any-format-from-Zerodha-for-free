import requests  # Importing the requests library to make HTTP requests
import pandas as pd  # Importing pandas for data manipulation and analysis
import datetime  # Importing datetime to handle date and time objects

# Setting the start and end dates for fetching historical market data
start_date = datetime.datetime(2015, 2, 2)  # Start date in YYYY, MM, DD format
end_date = datetime.datetime(2015, 3, 30)  # End date in YYYY, MM, DD format

token = "_________"  # Token representing the instrument (stock or asset) to fetch data for, this will be a mumber that you will find at the end of the URL of the stock in kite website
timeframe = "minute"  # Timeframe for historical data (minute-wise data in this case), this can be, hour, day, weeks, month

enctoken = "______________"
# Authentication token required to access the Zerodha Kite API

# Setting the request headers including authorization
header = {
    "Authorization": f"enctoken {enctoken}"
}

# Constructing the API URL for fetching historical data from Zerodha Kite API
url = f"https://kite.zerodha.com/oms/instruments/historical/{token}/{timeframe}"

# Defining request parameters
param = {
    "oi": 1,  # Open Interest (OI) data included
    "from": start_date.strftime("%Y-%m-%d"),  # Formatting start date as string
    "to": end_date.strftime("%Y-%m-%d")  # Formatting end date as string
}

# Creating a session for making HTTP requests
session = requests.session()

# Sending a GET request to fetch historical data
response = session.get(url, params=param, headers=header)
data = response.json()["data"]["candles"]  # Extracting the candle data from the response

# Converting the data into a pandas DataFrame for easy manipulation and analysis
df = pd.DataFrame(data, columns=["datetime", "open", "high", "low", "close", "volume", "oi"])

# Printing the DataFrame to verify the fetched data
print(df)
