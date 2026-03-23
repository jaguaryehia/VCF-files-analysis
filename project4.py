import pandas as pd

df=pd.read_csv('DATA1.csv')
# Find the duplicated values in the 'Name' column

duplicated_rows = df[df.duplicated(subset=['gene_assignment'], keep=False)]

print(duplicated_rows)
# # Get all rows with duplicated values in the 'Name' column
# for i in duplicated_names:
#     if i != '---':
#         print(i)

# print(duplicated_names)
# for i in duplicated_names:
#     if i != '---':
#         df[i]= i