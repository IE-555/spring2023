import matplotlib.pyplot as plt
from matplotlib.finance import candlestick2_ohlc
import matplotlib.ticker as ticker
import quandl
import numpy as np

# See
# https://stackoverflow.com/questions/36334665/how-to-plot-ohlc-candlestick-with-datetime-in-matplotlib
#


# Pre-reqs:
# 1)  Install quandl:
#		pip install quandl
#
# 2) Get an api key from
#		https://www.quandl.com/tools/python
#
# 3) Place the api key below:
quandl.ApiConfig.api_key = "YOUR_KEY_GOES_HERE"


# "YYY-MM-DD" format for dates
ticker_symbol	= "INTC"
date1 			= "2018-02-01"
date2 			= "2018-02-28"


def mydate(x,pos):
    try:
        return xdate[int(x)]
    except IndexError:
        return ''



dataSource = "WIKI/%s" % (ticker_symbol)
quotes = quandl.get(dataSource, start_date=date1, end_date=date2, returns="numpy")
print quotes
print quotes.dtype
print quotes['Open']


'''
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)


# Plot the time, open, high, low, close as a vertical line 
# ranging from low to high. Use a rectangular bar to 
# represent the open-close span. If close >= open, use 
# colorup to color the bar, otherwise use colordown.
candlestick2_ohlc(ax, quotes['Open'], quotes['High'], quotes['Low'], quotes['Close'], width=0.6)

xdate = quotes['Date']

ax.xaxis.set_major_locator(ticker.MaxNLocator(6))
ax.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))

# Add lines connecting each day's closing price
x = []
y = []
for i in range(0, len(quotes)):
	x.append(i)
	y.append(quotes[i]['Close'])				# Closing price
plt.plot(x, y)

plt.title(ticker_symbol)

fig.autofmt_xdate()
fig.tight_layout()

plt.show()
'''
