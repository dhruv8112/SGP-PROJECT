from tradingview_ta import TA_Handler, Exchange, Interval

# Create a TA_Handler object
symbol = 'SOLEX'
exchange = 'NSE'
screener = 'india'
interval = Interval.INTERVAL_1_DAY  # Using daily candles

tesla = TA_Handler(
    symbol=symbol,
    exchange=exchange,
    screener=screener,
    interval=interval
)
# Get the analysis summary
analysis = tesla.get_analysis()

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
    if tesla.interval == Interval.INTERVAL_1_DAY and tesla.exchange == 'NSE':
        print("Strong Sell: SMA50 crossed below EMA200 within the last 1 week.")
    elif tesla.interval == Interval.INTERVAL_1_DAY and tesla.exchange == 'NSE':
        print("Neutral: SMA50 crossed below EMA200 within the last 1 month.")
    else:
        print("Wait for retest of EMA200.")
