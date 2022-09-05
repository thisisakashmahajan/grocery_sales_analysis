# statistical_exploration.py
import pandas as pd

df = pd.read_csv('supermart_grocery_sales.csv')
print(df.columns)
print(df.State.unique())
print(df.City.unique())
