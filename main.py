import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dog = pd.read_csv('files/DOGE-USD.csv',
                  parse_dates=['Date'], index_col='Date')

# print(dog)

btc = pd.read_csv(
    'files/btc-market-price.csv',
    header=None,
    names=['Timestamp', 'Price'],
    index_col=0,
    parse_dates=True)
# print(btc)

eth = pd.read_csv('files/eth-price.csv', parse_dates=True, index_col=0)
prices = pd.DataFrame(index=btc.index)
prices.head()
prices['Bitcoin'] = btc['Price']
prices['Ether'] = eth['Value']
prices['Doge'] = dog['High'].reindex(prices.index).bfill()
# print(prices)
prices = prices.bfill()


correlation = prices.corr()
print(correlation)

std_values = prices.std()
print(std_values)

daily_change = prices.pct_change() * 100
print(daily_change.describe())

prices.plot(figsize=(12,6))
plt.show()
# vidurkis btc
prices['Bitcoin_MA'] = prices['Bitcoin'].rolling(window=7).mean()
prices['Ether_MA'] = prices['Ether'].rolling(window=7).mean()
prices['Doge_MA'] = prices['Doge'].rolling(window=7).mean()
prices[['Bitcoin', 'Bitcoin_MA']].plot(figsize=(12, 6), title="Bitcoin kainos ir 7 dienų vidurkis")
plt.show()


# tendencija

prices['Bitcoin_MA30'] = prices['Bitcoin'].rolling(window=30).mean()
prices['Bitcoin_MA90'] = prices['Bitcoin'].rolling(window=90).mean()
prices['Ether_MA30'] = prices['Ether'].rolling(window=30).mean()
prices['Ether_MA90'] = prices['Ether'].rolling(window=90).mean()
prices['Doge_MA30'] = prices['Doge'].rolling(window=30).mean()
prices['Doge_MA90'] = prices['Doge'].rolling(window=90).mean()

plt.figure(figsize=(14, 8))
plt.subplot(3, 1, 1)
plt.plot(prices['Bitcoin'], label='Bitcoin', alpha=0.6)
plt.plot(prices['Bitcoin_MA30'], label='Bitcoin MA30', color='orange')
plt.plot(prices['Bitcoin_MA90'], label='Bitcoin MA90', color='red')
plt.title("Bitcoin kainos ir slankieji vidurkiai")
plt.legend()
# Ether tendencijos
plt.subplot(3, 1, 2)
plt.plot(prices['Ether'], label='Ether', alpha=0.6)
plt.plot(prices['Ether_MA30'], label='Ether MA30', color='orange')
plt.plot(prices['Ether_MA90'], label='Ether MA90', color='red')
plt.title("Ether kainos ir slankieji vidurkiai")
plt.legend()

# Doge tendencijos
plt.subplot(3, 1, 3)
plt.plot(prices['Doge'], label='Doge', alpha=0.6)
plt.plot(prices['Doge_MA30'], label='Doge MA30', color='orange')
plt.plot(prices['Doge_MA90'], label='Doge MA90', color='red')
plt.title("Doge kainos ir slankieji vidurkiai")
plt.legend()

plt.tight_layout()
plt.show()

