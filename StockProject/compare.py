from tradingview_ta import TA_Handler, Exchange, Interval

def analyze_stock(symbol, exchange, screener, interval):
    stock = TA_Handler(
        symbol=symbol,
        exchange=exchange,
        screener=screener,
        interval=interval
    )
    
    # Get the analysis summary
    analysis = stock.get_analysis()

    # Access the indicators dictionary
    indicators = analysis.indicators

    # Access specific indicators, SMA50 and EMA200
    sma50 = indicators.get('SMA50')
    ema200 = indicators.get('EMA200')

    # Check for crossover condition (SMA50 crosses below EMA200)
    crossover_condition = sma50 is not None and ema200 is not None and sma50 > ema200

    # Determine strength and provide recommendations
    if crossover_condition:
        # Check if crossover occurred within the last 1 week
        if stock.interval == Interval.INTERVAL_1_DAY and stock.exchange == 'NSE':
            return f"{symbol}: Strong Sell - SMA50 crossed below EMA200 within the last 1 week."
        elif stock.interval == Interval.INTERVAL_1_DAY and stock.exchange == 'NSE':
            return f"{symbol}: Neutral - SMA50 crossed below EMA200 within the last 1 month."
        else:
            return f"{symbol}: Wait for retest of EMA200."
    else:
        return f"{symbol}: No crossover condition."

# Analyze 'SOLEX'
result_solex = analyze_stock('SOLEX', 'NSE', 'india', Interval.INTERVAL_1_DAY)

# Analyze 'SONUINFRA'
result_sonuinfra = analyze_stock('SONUINFRA', 'NSE', 'india', Interval.INTERVAL_1_DAY)

# Compare the analysis results and make a conclusion
if 'Strong Sell' in result_sonuinfra:
    print("Conclusion: Stock 2 (SONUINFRA) has a strong sell recommendation. Consider selling.")
elif 'Neutral' in result_sonuinfra:
    print("Conclusion: Stock 2 (SONUINFRA) has a neutral recommendation. Monitor for further signals.")
else:
    print("Conclusion: Stock 2 (SONUINFRA) has a wait recommendation. Wait for more information.")

# Print the analysis results for both stocks
print(result_solex)
print(result_sonuinfra)
