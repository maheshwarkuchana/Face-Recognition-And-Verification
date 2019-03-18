import pandas as pd
import pickle

filename = open("Models\\Names_Class_Mapping.pickle", "rb")
diction = pickle.load(filename)
# print(diction)

diction = dict((v,k) for k,v in diction.items())
print(diction)
df = pd.read_csv("Excel_Data\\encode.csv",index_col = 0)

for i in range(df['name'].count()):
    df.iloc[i,-1] = diction[df.iloc[i,-1]]
print(df.iloc[:,-1])

df.to_csv("Excel_Data\\encode.csv")

# X = df.iloc[:,:-1]

# pred = clf.predict(X)

# print(pred)
