"""* demand_analysis.py
Objective 4: Investigate demand of each top product over the years In this activity,
the top 5 products which have higher income value are tested for demand over the years. The demand for each month
from 2015 to 2018 is visualized. In an inventory, demand of a product in a month can be defined as total number of
transactions for that product in a month. For example, if a product is sold 50 times in a month, then the demand
value for that month is 50. The demand is irrespective of total sales price, location of outlet, and profit. """

import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv('supermart_grocery_sales_data.csv')

df[['month', 'day', 'year']] = df['order_date'].str.split("/", expand=True)

df = df[['sub_category', 'profit', 'sales', 'month', 'year']]
df['total'] = df['profit'] + df['sales']
df = df.drop(columns=['profit', 'sales'])

top_products = ['Health Drinks', 'Soft Drinks', 'Cookies', 'Breads & Buns', 'Noodles']
"""
# Program to find average income for each product month wise
for each_product in top_products:
    print(each_product)
    pslice = df[df['sub_category'] == each_product]
    for each_year in pslice.year.unique():
        for each_month in pslice.month.unique():
            average = np.average(pslice[pslice['month'] == each_month][pslice['year'] == each_year]['total'])
            average = round(average, 2)
            print(each_month, each_year, average)
"""

# Program to find number of transactions for each product month-wise
for each_product in top_products:
    print(each_product)
    pslice = df[df['sub_category'] == each_product]
    for each_year in pslice.year.unique():
        for each_month in pslice.month.unique():
            transactions = len(pslice[pslice['month'] == each_month][pslice['year'] == each_year])
            print(each_month, each_year, transactions)
