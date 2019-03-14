from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os
import tqdm
from Convert_encoding_to_csv import main

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True, help="Path to Dataset")

args = vars(ap.parse_args())

imagePaths = list(paths.list_images(args["dataset"]))
Encoding_list_for_storing = []

for (i, imagePath) in enumerate(imagePaths):
    print("[INFO] processing image {}/{}".format(i+1, len(imagePaths)))
    name = imagePath.split(os.path.sep)[-2]
    
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(
        rgb, model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)

    for encoding in encodings:
        encoding = encoding.tolist()
        name = name.replace("Data/Untrained/","")
        name = name.replace("1","")
        encoding.append(name)
        Encoding_list_for_storing.append(encoding)

main(Encoding_list_for_storing)
