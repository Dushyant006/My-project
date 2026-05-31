#Explore more datetime function and uses in pandas
import pandas as pd
import numpy as np
date_series = pd.Series(['2023-01-01', '2023-02-15', '2023-03-30'])
date_series = pd.to_datetime(date_series)
print("Original Date Series:")
print(date_series)
print("\nYear:")
print(date_series.dt.year)
print("\nMonth:")
print(date_series.dt.month)
print("\nDay:")
print(date_series.dt.day)
print("\nDay of the week:")
print(date_series.dt.dayofweek)