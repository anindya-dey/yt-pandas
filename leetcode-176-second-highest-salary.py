# Problem Link: https://leetcode.com/problems/second-highest-salary/description/?lang=pythondata

import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)
    second_highest_sal = employee[employee['rank'] == 2]['salary']
    result = pd.DataFrame(
        {'SecondHighestSalary': [None if len(second_highest_sal) == 0 else second_highest_sal.iloc[0]]})
    return result
