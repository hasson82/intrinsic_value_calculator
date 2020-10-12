from math import pow
MARGIN_OF_SAFETY = 0.25

def get_dilutes_eps(stock_fundamentals):
    results = stock_fundamentals["results"]
    ttm = results[5]
    income_statement = ttm["incomeStatement"]
    eps = income_statement["earningsPerShare"]
    dilutes_eps = eps["diluted"]
    return dilutes_eps

def get_net_income(stock_fundamentals):
    results = stock_fundamentals["results"]
    ttm = results[-1]
    income_statement = ttm["incomeStatement"]
    net_income = income_statement["netIncome"]
    return net_income

def get_depreciation_and_amortization(stock_fundamentals):
    results = stock_fundamentals["results"]
    ttm = results[-1]
    cash_flow_statement = ttm["cashflowStatement"]
    operating_activity = cash_flow_statement["operatingActivity"]
    depreciation_and_amortization = operating_activity["depreciationAndAmortization"]
    return depreciation_and_amortization

def get_long_term_debt(stock_fundamentals):
    results = stock_fundamentals["results"]
    ttm = results[-1]
    balance_sheet = ttm["balanceSheet"]
    liab_and_stock_equity = balance_sheet["liabAndStockEquity"]
    liabilities = liab_and_stock_equity["liabilities"]
    long_term_debt = liabilities["longTermDebt"]
    return long_term_debt

def get_equity(stock_fundamentals):
    results = stock_fundamentals["results"]
    ttm = results[-2]
    balance_sheet = ttm["balanceSheet"]
    liab_and_stock_equity = balance_sheet["liabAndStockEquity"]
    stockholders_equity = liab_and_stock_equity["stockholdersEquity"]
    total_stockholders_equity = stockholders_equity["totalStockholdersEquity"]
    return total_stockholders_equity

def calculate_growth(stock_fundamentals):
    net_income = get_net_income(stock_fundamentals)
    depreciation_and_amortization = get_depreciation_and_amortization(stock_fundamentals)
    long_term_debt = get_long_term_debt(stock_fundamentals)
    equity = get_equity(stock_fundamentals)
    numerator = net_income - depreciation_and_amortization
    denominator = equity + long_term_debt
    growth = (numerator / denominator)
    normalized_growth = growth * (1 - MARGIN_OF_SAFETY)
    return normalized_growth
    

def get_price_per_earning_5_year_avg(stock_valuation):
    collapsed = stock_valuation["Collapsed"]
    rows = collapsed["rows"]
    price_per_earning = rows[1]
    assert(price_per_earning["label"] == "Price/Earnings")
    datum = price_per_earning["datum"]
    price_per_earning_5_year_avg = datum[11]
    return float(price_per_earning_5_year_avg)

def calculate_intrinsic_values(stock_fundamentals, stock_valuation, years_ahead, yearly_yield):
    growth = calculate_growth(stock_fundamentals)
    eps = get_dilutes_eps(stock_fundamentals)
    price_per_earnings_5_year_avg = get_price_per_earning_5_year_avg(stock_valuation)
    price_in_5_years = eps * price_per_earnings_5_year_avg * pow((1+ growth),years_ahead)
    yearly_yield = yearly_yield / 100
    discount_rate = pow((1+ yearly_yield), years_ahead)
    intrinsic_value = price_in_5_years / discount_rate
    return intrinsic_value