import pandas

# READ CSV FILE 
df = pandas.read_csv("../../data/uci-pima-indian-diabetes-data-original.csv")

# Find Correlation
correlation = df.corr()

print("SHAPE: ", correlation.shape)
print(correlation)