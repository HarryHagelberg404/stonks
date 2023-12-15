import yfinance as yf
import uniplot as up
from datetime import date, timedelta
import sys

# Input variables
stock_symbol = sys.argv[1]
timestart = int(sys.argv[2])
today_date = date.today()
start_date = today_date - timedelta(days=timestart)
end_date = today_date

# Retrieve stock data using yfinance
data = yf.download(stock_symbol, start=start_date, end=end_date + timedelta(1))
# Extract the Date and Closing Price columns
dates = data.index
closing_prices = data["Close"]

print(f"     Last closing price: {closing_prices.iloc[-1]:.5f}")
# Convert dates to string in a readable format
formatted_dates = dates.strftime("%Y-%m-%d")

# Create a line plot using uniplot
plot = up.plot(closing_prices, range(len(dates)), lines=True, title=f"{stock_symbol} Stock Price Chart ({start_date} - {end_date})")
