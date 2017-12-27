import requests

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
for market in market_list:
	market_name = market['MarketName']
	# the bittrex api does not appear to have getticker information for BTC-GAM, as such an if statement is used to avoid errors
	if market_name != "BTC-GAM":
		price_response = requests.get(url_ticker + "?market=" + market_name)
		if market_response.status_code == 200:
			price_info = price_response.json()
			price = str(price_info['result']['Last'])
			print("Market: " + market_name + ", Price: " + price)
		else:
			print('Status:', response.status_code, 'Problem with the request. Exiting.')
			exit()