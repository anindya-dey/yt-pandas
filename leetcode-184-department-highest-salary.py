# Problem Link: https://leetcode.com/problems/department-highest-salary/description/?lang=pythondata

import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    emp_dept = employee.merge(right=department, how='inner', left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
    emp_dept['rank'] = emp_dept.groupby(by='id_dept')['salary'].rank(method='dense', ascending=False)
    result = emp_dept[emp_dept['rank'] < 2][['name_dept', 'name_emp', 'salary']]
    return result.rename(columns={
        'name_dept': 'Department',
        'name_emp': 'Employee',
        'salary': 'Salary'
    })