import requests
def get_valuation(ticker, mic, api_key):
    url = "https://morningstar1.p.rapidapi.com/live-stocks/GetValuation"

    querystring = {"Ticker": ticker,"Mic": mic}

    headers = {
    'x-rapidapi-host': "morningstar1.p.rapidapi.com",
    'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    valuation = response.json()
    return valuation 