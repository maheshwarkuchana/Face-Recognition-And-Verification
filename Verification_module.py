import pickle
import glob

file = open("Models\\Names_Class_Mapping.pickle",'rb')
name_mapping = pickle.load(file)

loaded_clf = dict()

for filename in glob.glob("Models\\One_Class_Models\\*.pickle"):
    person_name = filename[filename.rfind("\\")+1:].replace("_Model.pickle", "")
    loaded_clf.update({person_name: pickle.load(open(filename,'rb'))})

def main(query, pred):
    
    Person_Name = name_mapping[pred[0]]
    clf = loaded_clf[Person_Name]
    predicted = clf.predict(query)
    print(Person_Name, predicted)
    if predicted[0] == -1:
        return "Unknown"
    else:
        return name_mapping[pred[0]]