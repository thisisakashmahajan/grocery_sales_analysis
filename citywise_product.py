# citywise_product.py
import pandas as pd

df = pd.read_csv('supermart_grocery_sales_data.csv', parse_dates=['order_date'])
# print(df.columns)
df = df[['city', 'category']]

# print('No. of cities:', len(df.city.unique()))

# for each_city in df.city.unique():
#    print(each_city)

# print(df.groupby(by='city', axis=0).count())
city = df.city.unique()
category = df.category.unique()

for each_city in city:
    counts = []
    # print(each_city, '--------')
    for each_category in category:
        count = 0
        for i in range(len(df)):
            if df.iloc[i]['city'] == each_city and df.iloc[i]['category'] == each_category:
                count = count + 1
        counts.append(count)
    for i in counts:
        print(i, end=' ')
    print()
