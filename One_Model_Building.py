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
le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
le_name_mapping = dict((v, k) for k, v in le_name_mapping.items())

for key in le_name_mapping.keys():
    one_class_dataframe = X.loc[X['name'] == le_name_mapping[key]]
    
    X_train = one_class_dataframe.iloc[:,:-1]

    clf = OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
    clf.fit(X_train)

    filename = "Models\\One_Class_Models\\"+str(le_name_mapping[key])+"_Model.pickle"
    pickle.dump(clf, open(filename, 'wb'))
    print("Dumped "+str(le_name_mapping[key])+" Model")