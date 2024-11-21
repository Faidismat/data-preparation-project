import pandas as pd
df = pd.read_csv("U:\data-science-project\Iris.csv")
print(df.head())

df = df.dropna()
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
print("\nData after cleaning:")
print(df.head())
