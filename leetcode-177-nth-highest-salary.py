# Problem Link: https://leetcode.com/problems/nth-highest-salary/description/?lang=pythondata

import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, n: int) -> pd.DataFrame:
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)
    nth_df = employee[employee['rank'] == n]
    nth_salary = None if len(nth_df) == 0 else nth_df['salary'].iloc[0]
    nth_col_name = f'getNthHighestSalary({n})'
    return pd.DataFrame({nth_col_name: [nth_salary]})
