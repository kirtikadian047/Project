import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("SampleSuperstore.csv")
print(df)

print(df["Ship Mode"].unique())
print(df["Segment"].unique())
print(df["Country"].unique())
print(df["Region"].unique())
print(df["Sub-Category"].unique())
print(df["Discount"].unique())
print(df["Profit"].unique())
 
df=df.drop(columns=['Ship Mode'])
df.info()
p=df.head(40)

print(df.head(25))

seg=p[p['Segment']=='Corporate']
print(seg.head(25))

cty=df[df['City']=='Los Angeles']
print(cty)
print(cty.head(25))
plt.plot(seg['Quantity'],seg['Profit'])
plt.title('Quantity vs profit')
plt.xlabel('Quantity')
plt.ylabel('profit')
plt.xticks(rotation='vertical')
print(plt.show())

plt.bar(df['Segment'],df['Quantity'])
plt.title('Segment VS Quantity')
plt.xlabel('Segment')
plt.ylabel('Quantity')

plt.xticks(rotation='vertical')
print(plt.show())

Ny=df[df['City']=='New York City']
print(Ny)

dur=df[df['City']=='Durham']
print(dur)

dur_profit=dur['Profit'].sum()
print(dur_profit)

cty_profit=cty['Profit'].sum()
print(cty_profit)

Ny_profit=Ny['Profit'].sum()
print(Ny_profit)

profit_data=[
    ['New York City',62036.9837],
    ['Durham',116.8699],
    ['Los Angeles',30440.757899999997]
    ]
profit_data=pd.DataFrame(profit_data,columns=['City','Profit'])
print(profit_data)
plt.pie(profit_data['Profit'],labels=profit_data['City'],autopct='%0.1f%%.')
plt.show()
