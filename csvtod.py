import pandas as pd
df = pd.read_csv("data.csv")
print("First 5 rows:", df.head())
print("Last 5 rows:", df.tail())
print("Column Info:")
df.info()
print("Statistical Summary:", df.describe())
