import pandas as pd
import pickle


class Encodings_to_CSV:

    df = pd.read_csv("Excel_Data\\encode.csv", index_col=0)

    def __init__(self, df):
        Encodings_to_CSV.df = df

    def Update_Pickle():
        filename = "Excel_Data\\Encodings.pickle"
        pickle.dump(Encodings_to_CSV.df, open(filename, 'wb'))

    def main(encodings):
        print(Encodings_to_CSV.df.shape)

        for i in encodings:
            count = Encodings_to_CSV.df['name'].count()
            Encodings_to_CSV.df.loc[count+1] = i
            Encodings_to_CSV.df.to_csv("Excel_Data\\encode.csv", header=True)

        print(Encodings_to_CSV.df.shape)
        print('Added Encoding')
        Encodings_to_CSV.Update_Pickle()