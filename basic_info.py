"""
* basic_info.py
Investigate the correlation of various quantitative parameters in dataset
This activity reduces the number of columns being analyzed to avoid extra data being taken for testing and analysis.
The outcome of this activity is the list of correlated columns or data.
"""
import pandas as pd

df = pd.read_csv('supermart_grocery_sales_data.csv', parse_dates=['order_date'])

# Basic information of the dataset
print(df.describe())

print('---------------')

# Print all the subcategories with their corresponding major category
print('Sub categories and their corresponding major category:')
df = df.sort_values(by='category')
for minor in df.sub_category.unique():
    caught = 0
    for i in range(len(df)):
        if df.iloc[i]['sub_category'] == minor:
            print(minor, " - ", df.iloc[i]['category'])
            caught = 1
        if caught == 1:
            break

print('---------------')

# Print unique values for a particular column
column_name = 'city'
print('Unique {0} records:'.format(column_name))
for each_item in df[column_name].unique():
    print(each_item)
