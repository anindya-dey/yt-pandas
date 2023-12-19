# Problem Link:https://leetcode.com/problems/department-top-three-salaries/description/?lang=pythondata

import pandas as pd


def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    emp_dept = employee.merge(right=department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
    emp_dept['rank'] = emp_dept.groupby(by='id_dept')['salary'].rank(method='dense', ascending=False)
    result = emp_dept[emp_dept['rank'] <= 3]
    result = result[['name_dept', 'name_emp', 'salary']]
    result = result.rename(columns={
        'name_dept': 'Department',
        'name_emp': 'Employee',
        'salary': 'Salary'
    })
    return result
