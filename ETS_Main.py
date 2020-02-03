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
from stldecompose import decompose

#%% 

config_plot()


#%% Loading data

intervals=['Yearly', 'Quarterly', 'Monthly', 'Weekly', 'Daily', 'Hourly']
interval='Quarterly'
config=get_config(interval)

print('loading data')
train_path = './data/Train/%s-train.csv' % (interval)
test_path = './data/Test/%s-test.csv' % (interval)

train, test = create_datasets(train_path, test_path)

#%% Model Fitting and Forecasting

cost=[]
for i in range(len(train)):
    if i%1000==0:
        print('{} out of {}'.format(i,len(train)))
    ets = ETS_Class(train[i][-config['Training_length']:], Mode=config['Model'], Damped=config['Damped'], Trend=config['Trend'], Seasonal=config['Seasonal'], Seasonal_periods=config['freq'])
    ets.fit(Smoothing_level=config['Smoothing_level'], Smoothing_slope=config['Smoothing_slope'], Smoothing_seasonal=config['Smoothing_seasonal'], Damping_slope=config['Damping_slope'], Optimized=config['Optimized'], Use_boxcox=config['Use_boxcox'])
    fcast_ets=ets.forcast(config['Horizon'])
    cost.append(smape(test[i],fcast_ets))

avg_cost=np.mean(cost)
print('Average Cost for {} Series is {}'.format(interval,avg_cost))

#%% One-Step Prediction

#pred_ets=np.array([])
#existing_values=train_data
#ets = ETS_Class(existing_values, Mode='Holt-Winter', Damped=True, Trend='add', Seasonal='add', Seasonal_periods=seasonal_para)
#ets.fit(Optimized=True)
#pred_ets=np.concatenate((pred_ets,ets.forcast(1)))
#
#for i in range(test_data.shape[0]-1):
#    existing_values=np.concatenate((existing_values,test_data[i:i+1]))
#    ets = ETS_Class(existing_values, Mode='Holt-Winter', Damped=False, Trend='add', Seasonal='add', Seasonal_periods=seasonal_para)
#    ets.fit(Optimized=True)
#    pred_ets=np.concatenate((pred_ets,ets.forcast(1)))


#%% Plotting A Sample Data
    
#ts_label = 'Monthly Data'
#
#train_data_series=pd.Series(train_data)
#test_data_series=pd.Series(test_data,index=range(len(train_data),len(train_data)+len(test_data)))
#fcast_ets_series=pd.Series(fcast_ets,index=range(len(train_data),len(train_data)+len(fcast_ets)))
#pred_ets_series=pd.Series(pred_ets,index=range(len(train_data),len(train_data)+len(pred_ets)))
#
#two_timeseries_plot(pd.concat([train_data_series,test_data_series])[-100:],fcast_ets_series, ['g','b'], ts_label)
#two_timeseries_plot(pd.concat([train_data_series,test_data_series])[-100:],pred_ets_series, ['g','r'], ts_label)


