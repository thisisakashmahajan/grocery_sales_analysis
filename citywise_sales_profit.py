"""
* citywise_sales_profit.py
For the selected products namely soft drink, cold drink, Cookies, Breads & Buns, and Noodles top-selling cities
can be found. . In this way, a vendor of these products can target the cities to promote their products and services
associated with the top 5 selling products.
"""

import pandas as pd

df = pd.read_csv('supermart_grocery_sales_data.csv', parse_dates=['order_date'])

df = df[['city', 'sub_category', 'profit']]
top_products = ['Health Drinks', 'Soft Drinks', 'Cookies', 'Breads & Buns', 'Noodles']
cities = df.city.unique()

for city in cities:
    print(city, end='\t')
    for product in top_products:
        product_profit = 0
        for i in range(len(df)):
            if df.iloc[i]['city'] == city and df.iloc[i]['sub_category'] == product:
                product_profit = product_profit + df.iloc[i]['profit']
        print(round(product_profit, 2), end='\t')
    print('\n')
