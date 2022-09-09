# popular_products.py
import pandas as pd

df = pd.read_csv('supermart_grocery_sales_data.csv', parse_dates=['order_date'])
# print(df.head())

# Two level experiment - category and sub-category
# 1. Select category and all quantitative fields
data = df[['category', 'sales', 'profit']]
print(data.groupby(['category']).mean())

print('----------------------------------')

# 2. Select sub-category and all quantitative fields
data = df[['sub_category', 'sales', 'profit']]
print(data.groupby(['sub_category']).mean())
