# Problem Link: https://leetcode.com/problems/employees-earning-more-than-their-managers/description/?lang=pythondata

import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    emp_mgr = employee.merge(right=employee, left_on='managerId', right_on='id', how='inner', suffixes=['_emp', '_mgr'])[['name_emp', 'salary_emp', 'name_mgr', 'salary_mgr']]
    result = emp_mgr[emp_mgr['salary_emp'] > emp_mgr['salary_mgr']][['name_emp']]
    return result.rename(columns={'name_emp':'Employee'})