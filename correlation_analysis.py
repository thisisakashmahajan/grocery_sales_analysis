# correlation_analysis.py
import pandas as pd
import numpy as np


def round_off(amount):
    return round(amount, 3)


df = pd.read_csv('supermart_grocery_sales_data.csv', parse_dates=['order_date'])
# print(df.head())

# Select only the quantitative fields
df = df[['sales', 'discount', 'profit']]
# print(df.columns)

# Using NumPy library functions to calculate correlation
# 1. Correlation between sales amount and discount
correlation = np.corrcoef(df.sales, df.discount)
print('Correlation between Sales and Discount:', round_off(correlation[0][1]))

# 2. Correlation between sales amount and profit
correlation = np.corrcoef(df.sales, df.profit)
print('Correlation between Sales and Profit:', round_off(correlation[0][1]))

# 3. Correlation between profit and discount
correlation = np.corrcoef(df.profit, df.discount)
print('Correlation between Profit and Discount:', round_off(correlation[0][1]))
