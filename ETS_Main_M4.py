"""*******************************************************************************

                                   ETS Implementation

********************************************************************************"""
#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from util_ets_m4 import *
from ets_class import *
from stldecompose import decompose

#%%

config_plot()

#%% Loading data
 
print('loading data')
interval='Monthly'
intervals=['Daily','Monthly','Quarterly','Yearly']
seasonality=[7,12,4,1]
info = pd.read_csv('../../00- Datasets/M4DataSet/M4-info.csv')
train_path = '../../00- Datasets/M4DataSet/Train/%s-train.csv' % (interval)
test_path = '../../00- Datasets/M4DataSet/Test/%s-test.csv' % (interval)
train, val, test = create_datasets(train_path, test_path, 0)

#%% Train-Test Split

train_data=train[0]
val_data=val[0]
test_data=test[0]

#%% STL Decomposition

"""
index = pd.date_range(start = '20/01/2000', periods=len(train_data),freq='M')
temp=pd.DataFrame(train_data)
temp.set_index(index,inplace=True)
decomp = decompose(temp, period=12)

decomp.plot()
tsplot(pd.Series(decomp.trend.values.reshape(1,-1)[0]), lags=30)
tsplot(pd.Series(decomp.seasonal.values.reshape(1,-1)[0]), lags=30)
tsplot(pd.Series(decomp.resid.values.reshape(1,-1)[0]), lags=30)
"""

#%% Model Fitting and Forecasting

seasonal_para = seasonality[intervals.index(interval)]
ets = ETS_Class(train_data, Mode='Holt-Winter', Damped=False, Trend='add', Seasonal='add', Seasonal_periods=seasonal_para)
ets.fit(Optimized=True)
fcast_ets=ets.forcast(test_data.shape[0])

#%% One-Step Prediction

pred_ets=np.array([])
existing_values=train_data
ets = ETS_Class(existing_values, Mode='Holt-Winter', Damped=True, Trend='add', Seasonal='add', Seasonal_periods=seasonal_para)
ets.fit(Optimized=True)
pred_ets=np.concatenate((pred_ets,ets.forcast(1)))

for i in range(test_data.shape[0]-1):
    existing_values=np.concatenate((existing_values,test_data[i:i+1]))
    ets = ETS_Class(existing_values, Mode='Holt-Winter', Damped=False, Trend='add', Seasonal='add', Seasonal_periods=seasonal_para)
    ets.fit(Optimized=True)
    pred_ets=np.concatenate((pred_ets,ets.forcast(1)))


#%% Plotting Data
    
ts_label = 'Monthly Data'

train_data_series=pd.Series(train_data)
test_data_series=pd.Series(test_data,index=range(len(train_data),len(train_data)+len(test_data)))
fcast_ets_series=pd.Series(fcast_ets,index=range(len(train_data),len(train_data)+len(fcast_ets)))
pred_ets_series=pd.Series(pred_ets,index=range(len(train_data),len(train_data)+len(pred_ets)))

two_timeseries_plot(pd.concat([train_data_series,test_data_series])[-100:],fcast_ets_series, ['g','b'], ts_label)
two_timeseries_plot(pd.concat([train_data_series,test_data_series])[-100:],pred_ets_series, ['g','r'], ts_label)


