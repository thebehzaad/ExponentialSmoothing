

def get_config(interval):
    if interval=='Yearly':
        config = {
            'Model': 'Holt',
            'Horizon': 6,
            'freq': 1,
            'Damped': False,
            'Trend': None,
            'Seasonal': None,
            'Smoothing_level':None, 
            'Smoothing_slope':None, 
            'Smoothing_seasonal':None, 
            'Damping_slope':None, 
            'Optimized':True,
            'Use_boxcox':False,
            'Training_length':30                
        }

    elif interval=='Quarterly':
        config = {
            'Model': 'Holt-Winter',
            'Horizon': 8,
            'freq': 4,
            'Damped': False,
            'Trend': 'add',
            'Seasonal': 'add',
            'Smoothing_level':None, 
            'Smoothing_slope':None, 
            'Smoothing_seasonal':None, 
            'Damping_slope':None, 
            'Optimized':True,
            'Use_boxcox':False,
            'Training_length':100            
        }
        
    elif interval=='Monthly':
        config = {
            'Model': 'Holt-Winter',
            'Horizon': 18,
            'freq': 12,
            'Damped': False,
            'Trend': 'add',
            'Seasonal': 'add',
            'Smoothing_level':None, 
            'Smoothing_slope':None, 
            'Smoothing_seasonal':None, 
            'Damping_slope':None, 
            'Optimized':True,
            'Use_boxcox':False,
            'Training_length':240                
        }
        
    elif interval=='Weekly':
        config = {
            'Model': 'Holt',
            'Horizon': 13,
            'freq': 1,
            'Damped': False,
            'Trend': None,
            'Seasonal': None,
            'Smoothing_level':None, 
            'Smoothing_slope':None, 
            'Smoothing_seasonal':None, 
            'Damping_slope':None, 
            'Optimized':True,
            'Use_boxcox':False,
            'Training_length':520                
        }
        
    elif interval=='Daily':
        config = {
            'Model': 'Holt',
            'Horizon': 14,
            'freq': 1,
            'Damped': False,
            'Trend': None,
            'Seasonal': None,
            'Smoothing_level':None, 
            'Smoothing_slope':None, 
            'Smoothing_seasonal':None, 
            'Damping_slope':None, 
            'Optimized':True,
            'Use_boxcox':False,
            'Training_length':98                 
        }
        
    elif interval=='Hourly':
        config = {
            'Model': 'Holt-Winter',
            'Horizon': 48,
            'freq': 24,
            'Damped': False,
            'Trend': 'add',
            'Seasonal': 'add',
            'Smoothing_level':None, 
            'Smoothing_slope':None, 
            'Smoothing_seasonal':None, 
            'Damping_slope':None, 
            'Optimized':True,
            'Use_boxcox':False,
            'Training_length':672              
        }
        
    else:
        print("I don't have that config. :(")
    return config