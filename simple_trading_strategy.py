import pandas as pd
import matplotlib.pyplot as plt

file_path = input("Please Input Desired Stock File Name")
From_Date = input("Please Input Desired From Date Ex: 01/07/2022")
Till_Date = input("Please Input Desired Till Date Ex: 30/06/2023")

stock = pd.read_csv(file_path)
close_price = stock.loc[:, "Close"]

new_close = close_price.shift(-1)
stock["New Close"] = new_close

old_close = close_price
stock["Old Close"] = old_close

MAvg10 = close_price.rolling(10).mean()
stock['MAvg10'] = MAvg10

MAvg50 = close_price.rolling(50).mean()
stock['MAvg50'] = MAvg50

Positive_CHG = [1 if stock.loc[x, 'MAvg10'] > stock.loc[x, 'MAvg50'] else 0 for x in stock.index]
stock['Positive_CHG'] = Positive_CHG

stock["Profit"] = [(stock.loc[x, "New Close"]-stock.loc[x, "Old Close"]) if stock.loc[x, 'Positive_CHG'] == 1 else 0 for x in stock.index]

stock = stock.dropna() #use dropna to remove any "Not a Number" data

MAvg10.loc[From_Date:Till_Date].plot(label='MAvg10')
stock['Close'].loc[From_Date:Till_Date].plot(label='Close')
plt.legend()
plt.show()

MAvg50.loc[From_Date:Till_Date].plot(label='MAvg50')
stock['Close'].loc[From_Date:Till_Date].plot(label='Close')
plt.legend()
plt.show()

stock["Profit"].plot()
plt.axhline(y=0, color='red')
plt.legend()
plt.show()

stock['Wealth'] = stock['Profit'].cumsum()
stock['Wealth'].plot(label='Wealth')
plt.legend()
plt.show()

# # stock = stock.dropna() #use dropna to remove any "Not a Number" data
# print(stock)
