import requests
def get_valuation(ticker, mic):
    url = "https://morningstar1.p.rapidapi.com/live-stocks/GetValuation"

    querystring = {"Ticker": ticker,"Mic": mic}

    headers = {
    'x-rapidapi-host': "morningstar1.p.rapidapi.com",
    'x-rapidapi-key': "150ae62583mshc15dda1f2be424ap11b7d7jsn4ffa0b80876c"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    valuation = response.json()
    return valuation 