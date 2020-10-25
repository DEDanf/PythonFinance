import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

ms = pd.read_csv('/Users/danielw.y.fong/Documents/Coding/Finance/Data/microsoft2014-2018d.csv')

##Map out the Log returns of the dataset along with the pdf of the stock.

ms['LogReturn'] = np.log(ms['Close']).shift(-1) - np.log(ms['Close'])

mu = ms['LogReturn'].mean()
print(mu)
sigma = ms['LogReturn'].std(ddof=1)

density = pd.DataFrame()
density['x'] = np.arange(ms['LogReturn'].min()-0.01, ms['LogReturn'].max()+0.01, 0.001)
density['pdf'] = norm.pdf(density['x'], mu, sigma)

ms['LogReturn'].hist(bins=50, figsize=(15, 8))
plt.plot(density['x'], density['pdf'], color='red')
plt.show()

##Calc prob that stock will drop over a certain % in a day, -0.05 -> -5%

prob_return1 = norm.cdf(-0.05, mu, sigma)
print('The Probability is ', prob_return1)

##Calc prob for a longer period of time, e.g. year or here 220 days

mu220 = 220*mu
sigma220 = (220**0.5) * sigma
print('The probability of dropping over 40% in 220 days is ', norm.cdf(-0.4, mu220, sigma220))

print(220**0.5)

##Calc VAR for 5%ile

VaR = norm.ppf(0.05, mu, sigma)
print('Single day value at risk ', VaR)