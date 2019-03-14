import pandas as pd
import pickle

df = pd.read_csv("Excel_Data\\encode.csv")

X = df.iloc[:,1:-1]
Y = df.iloc[:,-1]

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
le.fit(Y)
Y = le.transform(Y)
le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
le_name_mapping = dict((v,k) for k,v in le_name_mapping.items())
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

# from keras.models import Sequential
# from keras.layers import Dense
# from keras.utils import np_utils

# clf = Sequential()
# clf.add(Dense(units=100, input_dim=128, activation='relu'))
# clf.add(Dense(units=75, activation='relu'))
# clf.add(Dense(units=50, activation='relu'))
# clf.add(Dense(units=10, activation='softmax'))


# clf.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# clf.fit(X, Y, epochs=40, batch_size=10)

filename = "Models\\MLP_Classifier_Model.pickle"
pickle.dump(clf, open(filename, 'wb'))


