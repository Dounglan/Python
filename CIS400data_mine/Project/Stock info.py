#!/usr/bin/env python
# coding: utf-8
# In[3]:


from alpha_vantage.timeseries import TimeSeries
# Your key here
key = '2Z7954OEL53VNE1Z'
ts = TimeSeries(key)
aapl, meta = ts.get_daily(symbol='AAPL')
print(aapl['2020-04-16'])


# In[2]:


from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

# Your key here
key = '2Z7954OEL53VNE1Z'
# Chose your output format, or default to JSON (python dict)
ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key)

# Get the data, returns a tuple
# aapl_data is a pandas dataframe, aapl_meta_data is a dict
aapl_data, aapl_meta_data = ts.get_intraday(symbol='AAPL', interval='5min')
# aapl_sma is a dict, aapl_meta_sma also a dict
aapl_sma, aapl_meta_sma = ti.get_sma(symbol='MSFT')


# Visualization
figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
aapl_data['4. close'].plot()
plt.tight_layout()
plt.grid()
plt.show()


# In[5]:


help(ts)


# In[15]:


import numpy as np
aapl_data
filewrite = open("AAPLApr15.txt", 'w')
#filewrite.write(aapl_data)
np.savetxt(r'c:\data\np.txt',aapl_data.get_values())
filewrite.close()


# In[3]:


#ZOOM
#MSFT
#JPMO
#BANKofAMERICA
aapl_data.get_values


# In[ ]:

