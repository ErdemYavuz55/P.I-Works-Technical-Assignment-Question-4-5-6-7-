#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

file_path = 'country_vaccination_stats.csv'
df = pd.read_csv(file_path)

df.head()
#df.shape
#df.isnull().sum()


# In[7]:


# Question 4 - Question 5
def fill_missing_vaccinations(data):
    countries = data['country'].unique()
    for country in countries:
        country_data = data[data['country'] == country]
        min_vaccination = country_data['daily_vaccinations'].min()
        if pd.isna(min_vaccination):
            min_vaccination = 0
        data.loc[data['country'] == country, 'daily_vaccinations'] = country_data['daily_vaccinations'].fillna(min_vaccination)
    return data

df_filled = fill_missing_vaccinations(df)


# In[14]:


# Question 6
median_vaccinations = df_filled.groupby('country')['daily_vaccinations'].median()

top_3_countries = median_vaccinations.nlargest(3)
print(top_3_countries)


# In[15]:


# Question 7
total_vaccinations_on_date = df_filled[df_filled['date'] == '1/6/2021']['daily_vaccinations'].sum()
print(total_vaccinations_on_date)


# In[ ]:




