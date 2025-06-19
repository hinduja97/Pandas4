import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    second=employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(second)>=2:
        result=second.head(2).tail(1)
    else:
        result=pd.Series([None])
    return pd.DataFrame({'SecondHighestSalary':result.reset_index(drop=True)})