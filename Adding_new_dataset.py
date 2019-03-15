from imutils import paths
import face_recognition
import argparse
import cv2
import os
from Encodings_to_CSV import Encodings_to_CSV


class Adding_new_dataset:

    def main():
        ap = argparse.ArgumentParser()
        ap.add_argument("-d", "--dataset", required=True,
                        help="Path to Dataset")
        args = vars(ap.parse_args())

        imagePaths = list(paths.list_images(args["dataset"]))

        Adding_new_dataset.encode_faces(args, imagePaths)

    def encode_faces(args, imagePaths):
        Encodings_list = []

        for (i, imagePath) in enumerate(imagePaths):
            print("Encoding Image {}/{}".format(i+1, len(imagePaths)))
            name = imagePath.split(os.path.sep)[-2]

            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            boxes = face_recognition.face_locations(rgb, model='hog')
            encodings = face_recognition.face_encodings(rgb, boxes)

            for encoding in encodings:
                encoding = encoding.tolist()
                name = name.replace("Data/Trained/", "")
                encoding.append(name)
                Encodings_list.append(encoding)

        Encodings_to_CSV.main(Encodings_list)


Adding_new_dataset.main()
