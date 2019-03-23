import pandas as pd
from matplotlib import pyplot as plt


def data_plot():
    user_study_json = pd.read_json('user_study.json')
    user_id_need = user_study_json['user_id'].drop_duplicates().sort_values()
    minutes_tmp = user_study_json[['user_id','minutes']].groupby('user_id').sum()
    minutes_need = pd.Series([minutes_tmp['minutes'][x] for x in user_id_need])
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title('StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    ax.plot(user_id_need,minutes_need)
    plt.show()
    return ax

data_plot()
