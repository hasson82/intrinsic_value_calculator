import requests

def get_fundamentals(ticker, mic, api_key):
    url = "https://morningstar1.p.rapidapi.com/convenient/fundamentals/yearly/as-reported"

    querystring = {"IncludeTrailing12Months":"True","Ticker": ticker ,"Mic": mic}

    headers = {
        'x-rapidapi-host': "morningstar1.p.rapidapi.com",
        'x-rapidapi-key': api_key,
        'accept': "string"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    fundamentals = response.json()

    return fundamentals
