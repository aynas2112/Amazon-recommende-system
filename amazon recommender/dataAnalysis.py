import pandas as pd
from pandas_profiling import ProfileReport
df=pd.read_csv('ratings_Electronics (1).csv')
print(df)
profile=ProfileReport(df)
profile.to_file(output_file="report.html")