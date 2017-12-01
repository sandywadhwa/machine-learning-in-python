import pandas

# READ CSV FILE 
df = pandas.read_csv("../../data/uci-pima-indian-diabetes-data-processed.csv")

number_of_trues = len(df.loc[df['diabetes']==True])
number_of_false = len(df.loc[df['diabetes']==False])

total = number_of_false + number_of_trues

print("True Percentage: {0:.2f}%".format((number_of_trues/total)*100))
print("False Percentage: {0:.2f}%".format((number_of_false/total)*100))