import tabula
import pandas as pd

# Read the first PDF and extract data
tables = tabula.read_pdf('gap2019.pdf', pages='all')
df = tables[3]
net_sales = df.iloc[1, :]
gross_margin = df.iloc[2, :]
operating_margin = df.iloc[3, :]
inventory = df.iloc[14, :]

# Read the second PDF and extract data
tables2 = tabula.read_pdf('gap2014.pdf', pages='all')
df1 = tables2[3]
net_sales1 = df1.iloc[1, 1:]
gross_margin1 = df1.iloc[2, 1:]
operating_margin1 = df1.iloc[3, 1:]
inventory1 = df1.iloc[13, 1:]

# Concatenate the data from both DataFrames
result = pd.concat([net_sales, gross_margin, operating_margin, inventory], axis=1, ignore_index=False)
result1 = pd.concat([net_sales1, gross_margin1, operating_margin1, inventory1], axis=1, ignore_index=False)

# Rename the columns in result1 to match the columns in result
result1.columns = result.columns

# Concatenate both DataFrames vertically
concatenated_df = pd.concat([result, result1], axis=0, ignore_index=False)

# Set a common index name
concatenated_df.index.name = 'Fiscal Year'

# Display the concatenated DataFrame
print(concatenated_df)

concatenated_df.to_csv('gap_10k.csv')
