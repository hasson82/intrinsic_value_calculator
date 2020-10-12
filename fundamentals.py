import requests

def get_fundamentals(ticker, mic):
    url = "https://morningstar1.p.rapidapi.com/convenient/fundamentals/yearly/as-reported"

    querystring = {"IncludeTrailing12Months":"True","Ticker": ticker ,"Mic": mic}

    headers = {
        'x-rapidapi-host': "morningstar1.p.rapidapi.com",
        'x-rapidapi-key': "150ae62583mshc15dda1f2be424ap11b7d7jsn4ffa0b80876c",
        'accept': "string"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    fundamentals = response.json()

    return fundamentals
