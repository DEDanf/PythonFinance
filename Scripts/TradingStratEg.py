##Example of workflow for testing a strategy

import pandas as pd
import matplotlib.pyplot as plt

ms = pd.read_csv('/Users/danielw.y.fong/Documents/Coding/Finance/Data/microsoft2014-2018d.csv')

ms['MA10'] = ms['Close'].rolling(10).mean()
ms['MA50'] = ms['Close'].rolling(50).mean()
ms = ms.dropna()

ms['Shares'] = [1 if ms.loc[ei, 'MA10']>ms.loc[ei, 'MA50'] else 0 for ei in ms.index]
ms['CloseTmr'] = ms['Close'].shift(-1)
ms['Profit'] = [ms.loc[ei, 'CloseTmr'] - ms.loc[ei, 'Close'] if ms.loc[ei, 'Shares']==1 else 0 for ei in ms.index]

plt.plot(ms['Profit'])
plt.axhline(y=0, color='red')
plt.show()

ms['PnL'] = ms['Profit'].cumsum()
plt.plot(ms['PnL'])
plt.show()
