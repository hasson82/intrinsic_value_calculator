from stock import Stock
from key_ratios import get_key_ratios
from stable import stable_grade
from current_ratio import get_current_ratio
from intrinsic_value import calculate_intrinsic_values
from fundamentals import get_fundamentals
from valuation import get_valuation
from time import sleep

def run_stock_anlysis(ticker, mic):
    years_ahead = 5
    yearly_yield = 9
    print("start stock anlysis")
    ''' constructor iof stock class'''
    stock = Stock()

    ''' use API to get data '''
    raw_stock_data = get_key_ratios(ticker, mic)
    stock.set_raw_stock_data(raw_stock_data)

    ''' check current ratio '''
    current_ratio = get_current_ratio(raw_stock_data)
    stock.set_current_ratio(current_ratio)

    ''' check if company is stable ''' 
    data = stable_grade(ticker ,raw_stock_data, True)
    grades = data["grades"]
    ten_years_span = data["rawData"]
    stock.set_grades(grades["debtToEquity"], grades["bookValuePerShare"], grades["earningsPerShare"])

    ''' calculate intrinsic value '''
    '''
    if(stock.perform_initial_test() == True):
        stock_fundamentals = get_fundamentals(ticker, mic)
        stock_valuation = get_valuation(ticker, mic)
        intrinsic_value = calculate_intrinsic_values(stock_fundamentals, stock_valuation, 5, 9)
        print("intrinsic_value is {}".format(intrinsic_value))
    '''
    
    stock_fundamentals = get_fundamentals(ticker, mic)
    sleep(1) #need to sleep because of API limit
    stock_valuation = get_valuation(ticker, mic)
    intrinsic_value = calculate_intrinsic_values(stock_fundamentals , stock_valuation, years_ahead, yearly_yield)
    print("intrinsic_value is {}".format(intrinsic_value))


if __name__ == "__main__":
    run_stock_anlysis("csco", "XNAS")