#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import csv

from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


def Temperature():
    GST = pd.read_csv('GlobalSurfaceTemperature.csv').set_index('Year')
    GHG = pd.read_csv('GreenhouseGas.csv').set_index('Year')
    CO2 = pd.read_csv('CO2ppm.csv').set_index('Year')
    
    BIG_TABLE = pd.concat([GHG, CO2, GST], axis=1).fillna(method='ffill').fillna(method='bfill')
    
    upper_model = linear_model.LinearRegression()
    median_model = linear_model.LinearRegression()
    lower_model = linear_model.LinearRegression()
    
    feature_cols = ['N2O','CH4','CO2','CO2 concentrations (NOAA (2017)) (parts per million)']

    upper_model.fit(BIG_TABLE.loc[:2010, feature_cols], BIG_TABLE.loc[:2010,['Upper']])
    median_model.fit(BIG_TABLE.loc[:2010, feature_cols], BIG_TABLE.loc[:2010,['Median']])
    lower_model.fit(BIG_TABLE.loc[:2010, feature_cols], BIG_TABLE.loc[:2010,['Lower']])

    UpperPredict = list(upper_model.predict(BIG_TABLE.loc[2011:, feature_cols]))
    MedianPredict = list(median_model.predict(BIG_TABLE.loc[2011:, feature_cols]))
    LowerPredict = list(lower_model.predict(BIG_TABLE.loc[2011:, feature_cols]))

    error_dists = [
                    mean_absolute_error(BIG_TABLE.loc[2011:,['Upper']], UpperPredict),
                    mean_absolute_error(BIG_TABLE.loc[2011:,['Median']], MedianPredict),
                    mean_absolute_error(BIG_TABLE.loc[2011:,['Lower']], LowerPredict)
                  ]
    # print(error_dists)
    return UpperPredict, MedianPredict, LowerPredict

if __name__ == '__main__':
    result = Temperature()
    print(result[0])
    print(result[1])
    print(result[2])

