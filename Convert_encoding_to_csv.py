import pandas as pd

def main(encodings):
    df1 = pd.read_csv("Excel_Data\\encode.csv")
    df1.drop(df1.columns[0],axis=1)
    for i in encodings:
        i.insert(0, len(df1.index))
        df1.loc[-1] = i
        df1.index = df1.index + 1 
        df1.sort_index()
        df1.to_csv("Excel_Data\\encode.csv",header=True)
    print(df1)
    print('Added Encoding')

df1 = pd.read_csv("Excel_Data\\encode.csv")
import pickle
filename = "Excel_Data\\Encodings.pickle"
pickle.dump(df1, open(filename, 'wb'))