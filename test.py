import pandas as pd
import pickle

filename = open("Models\\One_Class_Models\\"+str("Maheshwar")+"_Model.pickle", "rb")
clf = pickle.load(filename)

df = pd.read_csv("Excel_Data\\predict.csv",index_col = 0)
print(df)

X = df.iloc[:,:-1]

pred = clf.predict(X)

print(pred)
