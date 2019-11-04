import pickle
import Verification_module
import numpy as np
import pandas as pd

file = open("Models\\SVC_Linear_Model.pickle",'rb')
clf = pickle.load(file)
file = open("Models\\Names_Class_Mapping.pickle",'rb')
name_mapping = pickle.load(file)

def main(query):
    pred = clf.predict(query)
    print(pred)
    return Verification_module.main(query, pred)
    
