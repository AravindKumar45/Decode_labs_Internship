import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("DEcode_labs_sales_data.csv")

print(df.head())

print(df.describe())


#Total Revenue

print("Total Revenue in (USD):  ")
print(df['TotalPrice'].sum())

#Total Sales By Region
print("Total Sales By Region")
print(df.groupby('Region')['TotalPrice'].sum())

#Total Sales By Product

print("Total Sales By Product")
Product_sales=df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False)

print(df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False))

#Monthly Sales

print("Monthly Sales")
Monthly_sales=df.groupby('OrderedMonth')['TotalPrice'].sum()

print(df.groupby('OrderedMonth')['TotalPrice'].sum())


plt.bar(Product_sales.index, Product_sales.values)
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product-wise Sales")
plt.show()