# app/robo_advisor.py

import requests
import json

# utility function to convert float or integer to USD-formatted string (for printing)
# 

def to_usd(my_price):
    return "${0:,.2f}".format(my_price) #>12,000.71

#
# INFO REQUESTS
#

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get(request_url)
# print(type(response)) #> class 'requests.models.Response'>
# print(response.status_code) #> 200
# print(response.text) # dictionary, string

# quit()

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

# breakpoint()

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys())

latest_day = dates[0] # "2019-02-20" TODO: Sort this so that the lastest day is first

latest_close = tsd[latest_day]["4. close"]


# breakpoint()





print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm") #TODO: Program the daytime module
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")