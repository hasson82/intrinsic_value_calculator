import requests

def get_key_ratios(ticker, mic, api_key):
    url = "https://morningstar1.p.rapidapi.com/convenient/keyratios"

    querystring = {"Mic": mic ,"Ticker":ticker, "IncludeTrailing12Months" :"true"}

    headers = {
        'x-rapidapi-host': "morningstar1.p.rapidapi.com",
        'x-rapidapi-key': api_key,
        'accept': "string"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    stock_data = response.json()
    return stock_data
