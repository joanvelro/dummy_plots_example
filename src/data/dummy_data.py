import pandas as pd


# Load dummy data
df = pd.read_excel('../../data/dummy_data.xlsx', 'Data')
demand = df[6:]
demand.reset_index(inplace=True, drop=True)
demand.rename(columns={1: 'product_1', 2: 'product_2', 3: 'product_3', 4: 'product_4'}, inplace=True)
demand = demand[['product_1', 'product_2', 'product_3', 'product_4']]
demand.to_csv('../data/dummy_data.csv', index=False)
