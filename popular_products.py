"""* popular_products.py
Objective 2: To list out the popularity of products by amount of total sales
Each sales earns an overhead profit. When the sales amount and profit is summed up, we get an amount which represents total sales.
In this activity, sub-category level products are listed out by their total sales to show top 5 popular products in inventory

"""
import pandas as pd

df = pd.read_csv('supermart_grocery_sales_data.csv', parse_dates=['order_date'])
data = df[['sub_category', 'sales', 'profit']].copy()

series = data.iloc[:, 1:3].sum(axis=1).rename("total")
data['total'] = series
data = data.drop(columns=['sales', 'profit'])

print(data.groupby(['sub_category']).sum())
