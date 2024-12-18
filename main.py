import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dog = pd.read_csv('files/DOGE-USD.csv',
                  parse_dates=True)
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
prices['Doge'] = dog['High']
print(prices.head())
