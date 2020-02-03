"""*************************************************************************************************************

                                              ETS Implementation

*************************************************************************************************************"""
#%% Importing libraries and functions

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from config import get_config
from util_ets import *
from ets_class import *


#%% Loading data

intervals=['Yearly', 'Quarterly', 'Monthly', 'Weekly', 'Daily', 'Hourly']
interval='Monthly'
config=get_config(interval)

print('loading data')
train_path = './data/Train/%s-train.csv' % (interval)
test_path = './data/Test/%s-test.csv' % (interval)

train, test = create_datasets(train_path, test_path)

#%% Model Fitting and Forecasting
if interval=='Hourly':
    cost=[]
    for i in range(len(train)):
        ets = ETS_Class(np.log(train[i][-config['Training_length']:]), Mode=config['Model'], Damped=config['Damped'], Trend=config['Trend'], Seasonal=config['Seasonal'], Seasonal_periods=config['freq'])
        ets.fit(Smoothing_level=config['Smoothing_level'], Smoothing_slope=config['Smoothing_slope'], Smoothing_seasonal=config['Smoothing_seasonal'], Damping_slope=config['Damping_slope'], Optimized=config['Optimized'], Use_boxcox=config['Use_boxcox'])
        fcast_ets=ets.forcast(config['Horizon'])
        cost.append(smape(test[i],np.exp(fcast_ets)))
        
        if i%50==0:
            print('{} out of {}'.format(i,len(train)))
            train_data_series=pd.Series(train[i][-config['Training_length']:])
            temp_len=len(train[i][-config['Training_length']:])
            test_data_series=pd.Series(test[i],index=range(temp_len,temp_len+config['Horizon']))
            fcast_ets_series=pd.Series(np.exp(fcast_ets),index=range(temp_len,temp_len+config['Horizon']))
            ts_pair_plot(pd.concat([train_data_series,test_data_series]),fcast_ets_series, ['g','b'], interval+'time series sampel')
            
    avg_cost=np.mean(cost)
    print('Average Cost for {} Series is {}'.format(interval,avg_cost))
else:
    cost=[]
    for i in range(len(train)):        
        ets = ETS_Class(train[i][-config['Training_length']:], Mode=config['Model'], Damped=config['Damped'], Trend=config['Trend'], Seasonal=config['Seasonal'], Seasonal_periods=config['freq'])
        ets.fit(Smoothing_level=config['Smoothing_level'], Smoothing_slope=config['Smoothing_slope'], Smoothing_seasonal=config['Smoothing_seasonal'], Damping_slope=config['Damping_slope'], Optimized=config['Optimized'], Use_boxcox=config['Use_boxcox'])
        fcast_ets=ets.forcast(config['Horizon'])
        cost.append(smape(test[i],fcast_ets))
        
        if i%50==0:
            print('{} out of {}'.format(i,len(train)))
            train_data_series=pd.Series(train[i][-config['Training_length']:])
            temp_len=len(train[i][-config['Training_length']:])
            test_data_series=pd.Series(test[i],index=range(temp_len,temp_len+config['Horizon']))
            fcast_ets_series=pd.Series(fcast_ets,index=range(temp_len,temp_len+config['Horizon']))
            ts_pair_plot(pd.concat([train_data_series,test_data_series]),fcast_ets_series, ['g','b'], interval+' TS Sample')

    avg_cost=np.mean(cost)
    print('Average Cost for {} Series is {}'.format(interval,avg_cost))

