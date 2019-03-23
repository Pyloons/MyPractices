import pandas as pd

def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)

    date_data = pd.to_datetime(data['Date'])
    volume_data = list(data['Volume'])
    time_line = pd.Series(volume_data,index=date_data)
    second_volume = time_line.resample('Q').sum().sort_values()[-2]

    return second_volume

