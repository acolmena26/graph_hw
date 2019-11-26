from matplotlib import pylab as plt
import pandas as pd

pd.plotting.register_matplotlib_converters()

df1 = pd.read_csv("AMZN.csv")
print(df1.head())
df1['Date'] = pd.to_datetime(df1.Date)

mean = df1["Close"].mean()

df3 = pd.read_csv("BABA.csv")
df3['Date'] = pd.to_datetime(df3.Date)

plt.figure("Alibaba Stock")
plt.plot(df1["Date"], df1["Close"], 'r-', linewidth=0.6, label="Amazon stock price, mean="+str(mean))
plt.plot(df3["Date"], df3["Close"], 'b-', linewidth=1, label="Alibaba")
plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.show()