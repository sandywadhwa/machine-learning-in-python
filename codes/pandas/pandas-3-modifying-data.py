import pandas

# READ CSV FILE 
df = pandas.read_csv("../../data/uci-pima-indian-diabetes-data-processed.csv")

# Print Old Columns
print(df.head())


# Convert Column Values from String to Integer
str_to_int_map = {True : 1, False: 0}
df['diabetes'] = df['diabetes'].map(str_to_int_map)

print(df.head())

# Remove A Column
del df['skin']
print(df.head())