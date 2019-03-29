#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import csv

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


def Temperature():
    temp = pd.read_csv('GlobalSurfaceTemperature.csv')
    temp = temp.iloc[:,1:].set_index(pd.to_datetime(temp.Year.astype('str')))
    # print(temp.head())
    # print(temp.tail())
    gas = pd.read_csv('GreenhouseGas.csv')
    gas = gas.iloc[:,1:].set_index(pd.to_datetime(gas.Year.astype('str')))
    co2 = pd.read_csv('CO2ppm.csv')
    co2 = co2.iloc[:,1:].set_index(pd.to_datetime(co2.Year.astype('str')))
    co2.columns = ['CO2PPM']
    df = pd.concat([gas, co2, temp], 1)
    gas_part = df.iloc[:,:4].fillna(method='ffill').fillna(method='bfill')
    # print(gas_part.head())
    # print(gas_part.tail(10))
    data = gas_part['1970':'2010']
    test = gas_part['2010':'2017']

    errors = []

    model = LinearRegression().fit(data, df['1970':'2010'].Median)
    median = pd.np.round(model.predict(test), 3)
    model = LinearRegression().fit(data, df['1970':'2010'].Upper)
    upper = pd.np.round(model.predict(test), 3)
    model = LinearRegression().fit(data, df['1970':'2010'].Lower)
    lower = pd.np.round(model.predict(test), 3)
    return list(upper), list(median), list(lower)

if __name__ == '__main__':
    result = Temperature()
    print(result[0])
    print(result[1])
    print(result[2])
