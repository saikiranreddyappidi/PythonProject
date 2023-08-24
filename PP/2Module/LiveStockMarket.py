import yfinance as yf
import pandas
import matplotlib.pyplot as plt

# for google
# tik = yf.Ticker("GOOGL")
# for microsoft
tik = yf.Ticker("MSFT")
print(tik.info)
df = pandas.DataFrame(tik.history(period="5d", interval="5m"))
# df.to_csv("GOOGL.csv")
# df=pandas.read_csv("GOOGL.csv")
df.plot()
plt.show()
exit(5)
