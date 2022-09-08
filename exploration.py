import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.chdir("D:\GCOEN\Data Science with Python\Excel Data Files")
df = pd.read_csv('mobile_price_range_data.csv')
df.head()
df.shape
df.dtypes
df.isnull().sum()
df['price_range'].value_counts()

plt.scatter(df['int_memory'], df['ram'])
plt.xlabel('Internal Memory')
plt.ylabel('Ram')
plt.show()
sns.scatterplot(df['int_memory'], df['ram'], hue=df['price_range'])
plt.show()

plt.scatter(df['m_dep'], df['mobile_wt'])
plt.xlabel('Mobile Depth')
plt.ylabel('Mobile Weight')
plt.show()
sns.scatterplot(df['m_dep'], df['mobile_wt'], hue=df['price_range'])
plt.show()

plt.scatter(df['sc_h'], df['sc_w'])
plt.xlabel('Screen Height')
plt.ylabel('Screen Width')
plt.show()
sns.scatterplot(df['sc_h'], df['sc_w'], hue=df['price_range'])
plt.show()

plt.scatter(df['battery_power'], df['talk_time'])
plt.xlabel('Battery Power')
plt.ylabel('Maximum Talktime')
plt.show()
sns.scatterplot(df['battery_power'], df['talk_time'], hue=df['price_range'])
plt.show()