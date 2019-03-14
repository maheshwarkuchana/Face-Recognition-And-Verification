import pickle

file = open("Models\\MLP_Classifier_Model.pickle",'rb')
clf = pickle.load(file)
file = open("Models\\Names_Class_Mapping.pickle",'rb')
name_mapping = pickle.load(file)

def main(query):
    pred = clf.predict(query)
    return name_mapping[pred[0]]
