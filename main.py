from matplotlib import pylab as plt
import pandas as pd

df = pd.read_csv("housingmarket_madrid.csv")
print(df.columns)
#plt.figure('Price and rooms')
#plt.plot(df.Price.sort_values(ascending=false) ,linewidth=0.8, color = 'r', label = 'Coca Cola Stock')
#plt.plot(df_pep['Date'],df_pep['Close'], linewidth=0.8, color = 'b',label = 'Pepsi Stock' )

plt.xlabel('Rooms')
plt.ylabel(' Price')
plt.legend()


plt.show()