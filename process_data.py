import pandas as pd
df0= pd.read_csv("data/daily_sales_data_0.csv")
df1= pd.read_csv("data/daily_sales_data_1.csv")
df2= pd.read_csv("data/daily_sales_data_2.csv")
df= pd.concat([df0,df1,df2])
df= df[df['product']=='pink morsel']
df['price']= df['price'].str.replace('$', '').astype(float)
df['sales']= df['quantity']*df['price']
df= df[['sales', 'date', 'region']]
print(df.head())
df.to_csv("data/formatted_sales_data.csv", index = 'false')
# Data processing completed