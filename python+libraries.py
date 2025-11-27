#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("C:/Users/91974/Documents/sales_data.csv")
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')


# # total sales records are in the dataset?

# In[5]:


df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Preview
df.head()


# # What is the overall revenue generated?

# In[6]:


total_revenue = df['Revenue'].sum()
print("Total Revenue: $", total_revenue)


# # Which product category generated the highest revenue?

# In[8]:


category_sales = df.groupby("Category")['Revenue'].sum()
print(category_sales)
category_sales.plot(kind='bar', title="Revenue by Category")
plt.ylabel("Revenue")
plt.show()


# # Which region contributed the most to sales?

# In[9]:


region_sales = df.groupby("Region")['Revenue'].sum()
print(region_sales)
region_sales.plot(kind='pie', autopct='%1.1f%%', title="Revenue by Region")
plt.ylabel("")
plt.show()


# # What are the daily sales trends over time?

# In[10]:


df.groupby("Date")['Revenue'].sum().plot(kind='line', marker='o')
plt.title("Daily Sales Trend")
plt.ylabel("Revenue")
plt.xlabel("Date")
plt.grid(True)
plt.show()


# # What is the summary statistics of sales?

# In[11]:


print(df.describe())


# In[ ]:




