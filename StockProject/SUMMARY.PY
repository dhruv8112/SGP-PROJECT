from tradingview_ta import TA_Handler, Exchange, Interval

# Create a TA_Handler object
tesla = TA_Handler(
    symbol='TSLA',
    exchange='NASDAQ',
    screener='america',
    interval=Interval.INTERVAL_1_MINUTE
)

# Get the analysis summary
analysis = tesla.get_analysis()

# Access the indicators dictionary
indicators = analysis.indicators



# Print or use the EMA indicator as needed
print(indicators)
