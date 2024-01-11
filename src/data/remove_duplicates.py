import pandas as pd

df = pd.read_csv("./data/housing_data.csv")
df = df.drop_duplicates(subset="id")
df.to_csv("./data/housing_data.csv", index=False)
