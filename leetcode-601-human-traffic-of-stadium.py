# Problem Link: https://leetcode.com/problems/human-traffic-of-stadium/description/?lang=pythondata

import pandas as pd


def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium = stadium[stadium['people'] >= 100]
    stadium['row_nb'] = range(len(stadium))
    stadium['id_row_nb_diff'] = stadium.id - stadium.row_nb
    stadium['consecutive_group_size'] = stadium.groupby(by='id_row_nb_diff')['id'].transform('count')
    return stadium[stadium['consecutive_group_size'] >= 3].iloc[:, :3]
