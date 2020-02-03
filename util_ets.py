
import pandas as pd
import numpy as np
from matplotlib import dates
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
from collections import namedtuple

#%%

def read_file(file_location):
    series = []
    ids = []
    with open(file_location, 'r') as file:
        data = file.read().split("\n")

    for i in range(1, len(data) - 1):
    # for i in range(1, len(data)):
        row = data[i].replace('"', '').split(',')
        series.append(np.array([float(j) for j in row[1:] if j != ""]))
        ids.append(row[0])

    series = np.array(series)
    return series


def create_datasets(train_file_location, test_file_location):
    train = read_file(train_file_location)
    test = read_file(test_file_location)
    return train, test



def ts_stat_plot(y, lags=None, figsize=(12, 7)):
    
    assert isinstance(y, pd.Series), 'Input series y should be of type pd.Series'
        
    with plt.style.context(style='bmh'):
        plt.figure(figsize=figsize)
        layout = (2,2)
        ts_ax = plt.subplot2grid(layout, (0,0), colspan=2)
        acf_ax = plt.subplot2grid(layout, (1,0))
        pacf_ax = plt.subplot2grid(layout, (1,1))
        
        y.plot(ax=ts_ax)
        p_value = adfuller(y)[1]
        ts_ax.set_title('Time Series Analysis Plots\n Dickey-Fuller: p={0:.5f}'.format(p_value))
        smt.graphics.plot_acf(y, lags=lags, ax=acf_ax)
        smt.graphics.plot_pacf(y, lags=lags, ax=pacf_ax)
        plt.tight_layout()
        plt.savefig('diff_ts_plot.png', format='png')


def ts_pair_plot(y1,y2, color, y_label):
    # y is Series with index of datetime
    assert isinstance(y1, pd.Series)
    assert isinstance(y2, pd.Series)
    
    fig, ax = plt.subplots()
    ax.set_ylabel(y_label)
    ax.plot(y1.index, y1, color[0])
    ax.plot(y2.index, y2, color[1])
    fig.set_size_inches(8, 4)
    plt.tight_layout()
    plt.savefig(y_label + '.png', dpi=300)
    plt.show()

# average time series

def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def smape(y_true,y_pred):
    return np.mean(np.abs(y_true-y_pred)/(np.abs(y_true)+np.abs(y_pred)))*200
