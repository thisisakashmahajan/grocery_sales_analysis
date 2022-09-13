# citywise_sales_profit.py
import pandas as pd

df = pd.read_csv('supermart_grocery_sales_data.csv', parse_dates=['order_date'])
# print(df.columns)

df = df[['city', 'category', 'profit']]  # Replace 'profit' column with 'sales' column
# print(df.groupby(by='city', axis=0).mean())

city = df.city.unique()
category = df.category.unique()

# This program creates sales amount average per category and city wise
for each_city in city:
    counts = []
    # print(each_city, '--------')
    for each_category in category:
        sales = 0
        count = 0
        for i in range(len(df)):
            if df.iloc[i]['city'] == each_city and df.iloc[i]['category'] == each_category:
                sales = sales + df.iloc[i]['profit']
                count = count + 1
        counts.append(sales / count)
    for i in counts:
        print(i, end='\t')
    print()
