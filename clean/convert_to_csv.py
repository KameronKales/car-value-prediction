import pandas as pd

data_xls = pd.read_excel('auction.xls')
data_xls.to_csv('data.csv', encoding='utf-8', index=True)
