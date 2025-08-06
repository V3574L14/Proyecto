import pandas as pd

df = pd.read_csv("CH_Nationality_List_20171130_v1.csv")

for index, row in df.iterrows():
  print(f"{index + 1}. {row['Nationality']}")