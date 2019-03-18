from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import pickle
import numpy as np


class Build_Model:

    df = pd.read_csv("Excel_Data\\encode.csv")
    le_name_mapping = dict()

    def __init__(self, df):
        Build_Model.df = df
        X = df.iloc[:, 1:-1]
        Y = df.iloc[:, -1]
        Build_Model.Label_Encoding(X, Y)

    def label_encoding(X, Y):
        le = LabelEncoder()
        Y = le.fit_transform(Y)
        Build_Model.le_name_mapping = dict(
            zip(le.transform(le.classes_), le.classes_))
        Build_Model.training_model(X, Y)

    def saving_model(clf):
        filename = "Models\\Names_Class_Mapping.pickle"
        pickle.dump(Build_Model.le_name_mapping, open(filename, 'wb'))
        filename = "Models\\MLP_Classifier_Model.pickle"
        pickle.dump(clf, open(filename, 'wb'))

    def training_model(X, Y):
        clf = MLPClassifier()
        clf.fit(X, Y)
        Build_Model.saving_model(clf)
