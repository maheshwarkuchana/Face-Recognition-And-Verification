import pandas as pd
import pickle
import numpy as np

df = pd.read_csv("Excel_Data\\encode.csv")

X = df.iloc[:,1:-1]
Y = df.iloc[:,-1]

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
Y = le.fit_transform(Y)

le_name_mapping = dict(zip(le.transform(le.classes_), le.classes_))
print(le_name_mapping)
filename = "Models\\Names_Class_Mapping.pickle"
pickle.dump(le_name_mapping, open(filename, 'wb'))

# from sklearn.ensemble import RandomForestClassifier
# clf = RandomForestClassifier()
# clf.fit(X,Y)

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier()
clf.fit(X,Y)

# from sklearn.svm import SVC
# clf = SVC(kernel='linear')
# clf.fit(X,Y)

# from sklearn.svm import SVC
# clf = SVC(kernel='rbf')
# clf.fit(X,Y)

# from sklearn.ensemble import AdaBoostClassifier
# clf = AdaBoostClassifier()
# clf.fit(X,Y)

filename = "Models\\MLP_Classifier_Model.pickle"
pickle.dump(clf, open(filename, 'wb'))


