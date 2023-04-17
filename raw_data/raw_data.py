import pandas as pd

df = pd.read_csv('E:\\raw_data.csv')

df.isnull().sum()
df.duplicated().sum()
date_cols = ['dob', 'last_purchase_date']

for col in date_cols:
    print(f"Unique values in {col}: {df[col].unique()}")
df['dob'] = pd.to_datetime(df['dob'], format='%d-%m-%Y', errors='coerce', dayfirst=True)
df['last_purchase_date'] = pd.to_datetime(df['last_purchase_date'], format='%d-%m-%Y', errors='coerce', dayfirst=True)
df['gender'] = df['gender'].apply(lambda x: x.lower().capitalize() if isinstance(x, str) else x)
df['marital_status'] = df['marital_status'].apply(lambda x: x.lower().capitalize() if isinstance(x, str) else x)
print(df.head())
print(df.info())
print(df.shape)

df.to_csv('E:\\cleaned_data.csv', index=False)

