import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator


def co2_gdp_plot():
    data_tb = pd.read_excel('ClimateChange.xlsx', tablename='Data')
    gdp_raw = data_tb[data_tb['Series code']=='NY.GDP.MKTP.CD']
    co2_raw = data_tb[data_tb['Series code']=='EN.ATM.CO2E.KT']

    gdp_value = gdp_raw[gdp_raw.columns[6:]].replace({'..':np.nan})
    gdp_value = gdp_value.fillna(method='ffill', axis=1)
    gdp_value = gdp_value.fillna(method='bfill', axis=1)
    gdp_value['sum'] = gdp_value.apply(lambda x: x.sum(), axis=1)
    gdp = pd.concat([gdp_raw['Country code'], gdp_value['sum']], axis=1)

    co2_value = co2_raw[co2_raw.columns[6:]].replace({'..':np.nan})
    co2_value = co2_value.fillna(method='ffill', axis=1)
    co2_value = co2_value.fillna(method='bfill', axis=1)
    co2_value['sum'] = co2_value.apply(lambda x: x.sum(), axis=1)
    co2 = pd.concat([co2_raw['Country code'], co2_value['sum']], axis=1)

    # normalization
    gdp_min = gdp['sum'].min()
    gdp_max = gdp['sum'].max()
    gdp['sum'] = gdp['sum'].apply(lambda x: (x - gdp_min) / (gdp_max - gdp_min))
    co2_min = co2['sum'].min()
    co2_max = co2['sum'].max()
    co2['sum'] = co2['sum'].apply(lambda x: (x - co2_min) / (co2_max - co2_min))

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('GDP-CO2')
    ax.set_xlabel('Countries')
    ax.set_ylabel('Values')
    
    # plt.xticks will print only what it receive
    in_codes = lambda x: gdp['Country code'][x + gdp.index[0]]
    codes = ['CHN', 'USA', 'GBR', 'FRA','RUS']
    xticks_name, xticks_position = [], []
    for x in range(len(gdp)):
        if in_codes(x) in codes:
            xticks_position.append(x)
            xticks_name.append(in_codes(x))
    plt.xticks(xticks_position, xticks_name, rotation='vertical')
    
    co2_sum = ax.plot(range(len(co2)), co2['sum'], color='blue', label='CO2-SUM')
    gdp_sum = ax.plot(range(len(gdp)), gdp['sum'], color='orange', label='GDP-SUM')
    ax.legend()

    # fig = plt.subplot()
    plt.show()

    china_co2 = round(float(co2[co2['Country code']=='CHN']['sum']), 3)
    china_gdp = round(float(gdp[gdp['Country code']=='CHN']['sum']), 3)
    china = [china_co2, china_gdp]
    return ax, china


if __name__ == '__main__':
    print(co2_gdp_plot())
