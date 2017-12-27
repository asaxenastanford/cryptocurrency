import requests

# set up twilio 
from twilio.rest import Client
# Twilio Account SID and Auth Token
client = Client("ACccab7c080046b07164cbd6ce8be7720e", "eb69728002b879b6edccc3d6b73541d0")

# Set the request parameters
base_url = 'https://bittrex.com/api/v1.1'
end_point_market = '/public/getmarkets'
end_point_ticker = '/public/getticker'
url_market = base_url + end_point_market
url_ticker = base_url + end_point_ticker

# Do the HTTP get request
market_response = requests.get(url_market)

# Check for HTTP codes other than 200
if market_response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Decode the JSON response into a dictionary and use the data
market_info = market_response.json()

# Print out prices of currencies  
market_list = market_info['result']
message = ""

counter = 0;

for market in market_list:
	if counter < 10:
		market_name = market['MarketName']
		# the bittrex api does not appear to have getticker information for BTC-GAM, as such an if statement is used to avoid errors
		try:
			price_response = requests.get(url_ticker + "?market=" + market_name)
			if market_response.status_code == 200:
				price_info = price_response.json()
				price = str(price_info['result']['Last'])
				#print("Market: " + market_name + ", Price: " + price)
				message = message + "Market: " + market_name + ", Price: " + price + "\n"
				counter += 1; 
			else:
				print('Status:', response.status_code, 'Problem with the request. Exiting.')
				exit()
		except TypeError:
			print("Skip: " + market_name)

message_intro = "\n" + "Here are prices for the first " + str(counter) + " cryptocurrencies on bittrex \n" 

client.messages.create(to="+16504216840", 
                       from_="+14084127207 ", 
                       body=message_intro+ message)