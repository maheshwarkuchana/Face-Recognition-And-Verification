import face_recognition
import cv2
import glob


images = glob.glob("C:/Users/Anonymous/Downloads/1/*.jpg")
i = 0
for imagePath in images:
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb, model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)

    
    for (top, right, bottom, left) in boxes:
        img = image[top:bottom,left:right]
        cv2.imwrite('Data/Trained/Temp/'+str(i)+'.jpg', img)
        print(i)
        i +=1
