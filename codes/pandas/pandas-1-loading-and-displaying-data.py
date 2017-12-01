import pandas
import numpy
import matplotlib

# READ CSV FILE 
df = pandas.read_csv("../../data/uci-pima-indian-diabetes-data-original.csv")

# Print Dimensions of Data (Rows, Cols)
print("Dimensions of Data", df.shape)

# Print First n Rows
n = 5
print(df.head(n))

# Print Last n Rows
print(df.tail(n))

# Get One Particular Cell Value [col][row]
print(df["age"][1])