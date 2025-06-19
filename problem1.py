import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df=employee[['salary']].drop_duplicates()
    if N < 0 or N>len(df):
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    new_df=df.sort_values(by=['salary'],ascending=False).head(N).tail(1).rename(columns={'salary':f'getNthHighestSalary({N})'})
    return new_df