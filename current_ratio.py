from key_ratios import get_key_ratios

def get_current_ratio(stock_data):
    results = stock_data["results"]
    ttm = results[10]
    key_ratio_statics_section = ttm["keyRatioStatisticsSection"]
    financial_health_liquidity_section = key_ratio_statics_section["financialHealthLiquiditySection"]
    current_ratio = financial_health_liquidity_section["currentRatio"]
    return current_ratio
     
