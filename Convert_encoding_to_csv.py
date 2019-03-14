import pandas as pd


# df = pd.read_csv("Encodings.csv")

# for index, row in df.iterrows():
#     l = row['encodings'].split(",")
#     lo = []
#     for i in l:
#         i = i.replace('[',"")
#         i = i.replace(']',"")
#         try:
#             i = float(i)
#         except:
#             continue
#         lo.append(i)
#     lo.append(row['names'])
#     print(index)
#     df1.loc[index] = lo

# df1.to_csv("encode.csv",header=True)

def main(encodings):
    df1 = pd.read_csv("Excel_Data\\encode.csv")
    df1.drop(df1.columns[0],axis=1)
    for i in encodings:
        i.insert(0, len(df1.index))
        # print(type(i))
        df1.loc[-1] = i
        df1.index = df1.index + 1 
        df1.sort_index()
        # df1.loc[len(df1.index)+1] = i
        # print(len(df1.index))
        df1.to_csv("Excel_Data\\encode.csv",header=True)
    print(df1)

print('Added Encoding')