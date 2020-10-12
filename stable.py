from key_ratios import get_key_ratios

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def get_start_year(results):
    start_year = results[0]
    year = int((start_year["startDate"][0:4]))
    return year

def debt_to_equity_grade(dte_list):
    grade = 100
    for i in range(10):
        if dte_list[i] > 0.5:
            grade = 0
    return grade

def book_value_per_share_grade(bvps_list):
    grade = 100
    for i in range(1,10):
        if bvps_list[i] < bvps_list[i-1]:
            grade = 0
    return grade

def earnings_per_share_grade(eps_list):
    grade = 100
    for i in range(1,10):
        if eps_list[i] < eps_list[i-1]:
            grade = 0
    return grade

def plot_line(dte_list, bvps_list, eps_list, start_year, title):
    finish_year = start_year + 10
    x = np.linspace(start_year, finish_year, 10)
    plt.title(title)
    plt.plot([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], 'r--')
    plt.plot(dte_list, label = 'debt to equity', marker = 'o')
    plt.plot(bvps_list, label = 'book value per share')
    plt.plot(eps_list, label = 'earnings per share')
    plt.xlabel('years')
    plt.ylabel('values')
    plt.legend()
    plt.show()

def stable_grade(ticker, stock_data, to_plot):
    debt_to_equity = []
    earnings_per_share = []
    book_value_per_share = []
    results = stock_data["results"]
    start_year = get_start_year(results)
    for i in range (10):
        yearly_results = results[i]
        key_Ratio_financials_section = yearly_results["keyRatioFinancialsSection"]
        book_value_per_share.append(key_Ratio_financials_section["bookValuePerShare"])
        earnings_per_share.append(key_Ratio_financials_section["earningsPerShare"]) 
        key_ratio_statistics_section = yearly_results["keyRatioStatisticsSection"]
        financial_health_liquidity_section = key_ratio_statistics_section["financialHealthLiquiditySection"]
        debt_to_equity.append(financial_health_liquidity_section["debtOrEquity"])
    raw_data = {}
    raw_data["debtToEquity"] = debt_to_equity
    raw_data["bookValuePerShare"] = book_value_per_share
    raw_data["earningsPerShare"] = earnings_per_share
    title = ticker + " values"
    if to_plot:
        plot_line(debt_to_equity, book_value_per_share, earnings_per_share, start_year, title)
    dte_grade = debt_to_equity_grade(debt_to_equity)
    bvps_grade = book_value_per_share_grade(book_value_per_share)
    eps_grade = earnings_per_share_grade(earnings_per_share)
    grades = {}
    grades["debtToEquity"] = dte_grade
    grades["bookValuePerShare"] = bvps_grade
    grades["earningsPerShare"] = eps_grade
    data = {}
    data["rawData"] = raw_data
    data["grades"] = grades
    return data
