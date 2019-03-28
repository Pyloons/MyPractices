# _*_ codig: utf-8 _*_
import pandas as pd


def co2():
    # Read raw tables
    data_tb = pd.read_excel('ClimateChange.xlsx', sheetname='Data')
    country_tb = pd.read_excel('ClimateChange.xlsx', sheetname='Country')

    # Deal with the total emission of every contry
    data_filted = data_tb[data_tb['Series code']=='EN.ATM.CO2E.KT']

    emission_log = data_filted.loc[:,[x for x in range(1990,2012)]]
    emission_log = emission_log.replace({'..':None})
    emissions = emission_log.fillna(method='ffill', axis=1)
    emissions = emissions.fillna(method='bfill', axis=1)
    #emissions['sum'] = emissions.sum(1)
    emissions['sum'] = emissions.apply(lambda x:x.sum(), axis=1)

    data_need = pd.concat([data_filted['Country name'], emissions['sum']], axis=1)

    # Get the income group of every country
    country_category = country_tb.loc[:,['Country name','Income group']]

    # Get every raw data to fill the result
    raw_static = pd.merge(country_category, data_need)
    print(raw_static[raw_static['sum'].isin([0])])
    print(raw_static[raw_static['sum'].isnull()])
    raw_static = raw_static.replace({0.0:None})
    print(raw_static[raw_static['sum'].isin([0])])
    print(raw_static[raw_static['sum'].isnull()])
    raw_static = raw_static.dropna()
    print(raw_static[raw_static['sum'].isin([0])])
    print(raw_static[raw_static['sum'].isnull()])

    #income_cate = [x for x in raw_static['Income group'].drop_duplicates()]
    income_cate = [
                   'High income: OECD',
                   'High income: nonOECD',
                   'Low income',
                   'Lower middle income',
                   'Upper middle income'
                  ]
    
    results = pd.DataFrame(columns=['Income group','Sum emissions','Highest emission country','Highest emissions','Lowest emission country','Lowest emissions'])

    for i in range(len(income_cate)):
        group = income_cate[i]
        sum_emi = raw_static[raw_static['Income group']==group]['sum'].sum()
        high_id = raw_static[raw_static['Income group']==group]['sum'].idxmax()
        low_id = raw_static[raw_static['Income group']==group]['sum'].idxmin()
        high_con = raw_static.loc[high_id]['Country name']
        high_emi = raw_static.loc[high_id]['sum']
        low_con = raw_static.loc[low_id]['Country name']
        low_emi = raw_static.loc[low_id]['sum']
        results.loc[i] = [group,sum_emi,high_con,high_emi,low_con,low_emi]

    results = results.set_index('Income group')
    return results.sort_index()
    
if __name__ == '__main__':
    print(co2())

