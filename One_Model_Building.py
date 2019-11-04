from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import pickle

df = pd.read_csv("Excel_Data\\encode.csv", index_col=0)

X = df.iloc[:,:]
Y = df.iloc[:, -1]

le = LabelEncoder()
le.fit(Y)
Y = le.transform(Y)
le_name_mapping = dict(zip(le.transform(le.classes_), le.classes_))

for key in le_name_mapping.keys():
    one_class_dataframe = X.loc[X['name'] == le_name_mapping[key]]
    X_train = one_class_dataframe.iloc[:,:-1]

    clf = IsolationForest(behaviour='new', max_samples=100, contamination='auto')
    # clf = OneClassSVM()

    clf.fit(X_train)

    filename = "Models\\One_Class_Models\\"+str(le_name_mapping[key])+"_Model.pickle"
    pickle.dump(clf, open(filename, 'wb'))
    print("Dumped "+str(le_name_mapping[key])+" Model")