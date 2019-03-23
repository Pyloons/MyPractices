import numpy as np
import pandas as pd
from pandas import DataFrame
import json


def analysis(file, user_id):
    times = 0
    minutes = 0
    with open(file) as f:
        us = json.loads(f.read())
    usdf = DataFrame(us)

    times = len(usdf[usdf['user_id']==user_id])
    minutes = usdf[usdf['user_id']==user_id]['minutes'].sum()

    return times, minutes

