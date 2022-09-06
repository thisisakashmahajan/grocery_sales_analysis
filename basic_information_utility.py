# basic_information_utility.py
import pandas as pd

df = pd.read_csv('supermart_grocery_sales_data.csv', parse_dates=['order_date'])

# Total records in dataset
print('Total records in dataset: %.0f' % len(df))
print('---------------')

# The dates between the records are collected
print('The dates between records are collected')
print('Start date: ', min(df.order_date))
print('End date: ', max(df.order_date))
print('---------------')

# Unique regions where goods are sold
print('Unique Regions of sales:')
for region in df.region.unique():
    print(region)
print('---------------')

# Print the major categories
print('Major categories of products:')
for category in df.category.unique():
    print(category)
print('---------------')

# Print all the subcategories with their corresponding major category
print('Sub categories and their corresponding major category')
df = df.sort_values(by='category')
for minor in df.sub_category.unique():
    caught = 0
    for i in range(len(df)):
        if df.iloc[i]['sub_category'] == minor:
            print(minor, " - ", df.iloc[i]['category'])
            caught = 1
        if caught == 1:
            break
print('------ Complete -------')
