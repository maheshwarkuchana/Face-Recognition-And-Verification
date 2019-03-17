import face_recognition
import cv2
import pickle
import pandas as pd
import predict_faces

image = cv2.imread("C:\\Users\\Anonymous\\Documents\\GitHub\\Face-Recognition-Neural-Networks\\Test_Images\\3.jpg")

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

boxes = face_recognition.face_locations(rgb, model='hog')
encodings = face_recognition.face_encodings(rgb, boxes)

names = []

for encoding in encodings:
    encoding = [encoding.tolist()]
    name = predict_faces.main(encoding)
    names.append(name)

for ((top, right, bottom, left), name) in zip(boxes, names):
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    y = top-15 if top - 15 > 15 else top+15
    cv2.putText(image, name, (left, y),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

image = cv2.resize(image, (0, 0), fx=0.2, fy=0.2)
cv2.imshow("Image", image)
cv2.waitKey()
cv2.destroyAllWindows()
