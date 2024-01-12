# Problem Link: https://leetcode.com/problems/rank-scores/description/?lang=pythondata

import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    sorted_scores = scores.sort_values(['score'], ascending=False)
    sorted_scores['rank'] = sorted_scores['score'].rank(method='dense', ascending=False)
    return sorted_scores[['score', 'rank']]
