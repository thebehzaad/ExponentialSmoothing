"""****************************************************************************************


****************************************************************************************"""
#%% Importing Libraries

import numpy as np
import pandas as pd
import warnings
from statsmodels.tsa.holtwinters import SimpleExpSmoothing, Holt, ExponentialSmoothing 

#%%

class ETS_Class:
    def __init__(self, ts, Mode, Damped=False, Trend=None, Seasonal=None, Seasonal_periods=None):
        self.mode=Mode
        self.ts=ts
        if Mode=='Simple':
            self.exp_smoothing=SimpleExpSmoothing(ts)
        elif Mode=='Holt':
            self.exp_smoothing=Holt(ts, damped=Damped)
        elif Mode=='Holt-Winter':   
            self.exp_smoothing=ExponentialSmoothing(ts, damped=Damped, trend=Trend, seasonal=Seasonal, seasonal_periods=Seasonal_periods)

    def fit(self, Smoothing_level=None, Smoothing_slope=None, Smoothing_seasonal=None, Damping_slope=None, Optimized=False, Use_boxcox=False):
        warnings.filterwarnings('ignore')
        if self.mode=='Simple':
           self.fit_results=self.exp_smoothing.fit(smoothing_level=Smoothing_level, optimized=Optimized) 
        elif self.mode=='Holt':
           self.fit_results=self.exp_smoothing.fit(smoothing_level=Smoothing_level, smoothing_slope=Smoothing_slope, damping_slope=Damping_slope, optimized=Optimized)  
        elif self.mode=='Holt-Winter':
           self.fit_results=self.exp_smoothing.fit(smoothing_level=Smoothing_level, smoothing_slope=Smoothing_slope, smoothing_seasonal=Smoothing_seasonal, damping_slope=Damping_slope, optimized=Optimized, use_boxcox=Use_boxcox)
        
    def forcast(self, pred_horizon):                
        fcast_ets_values= self.fit_results.forecast(steps=pred_horizon)        
        
        return fcast_ets_values
    
