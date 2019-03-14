import face_recognition
import cv2,glob

# imagePath = "C:\\Users\\Anonymous\\Documents\\Visual_Studio_files\\PyFiles\\Face_Recognition\\Test-Face-Recognition\\Data\\1.jpg"

images = glob.glob("Data/Untrained/Abhilash_A/*.jpg")
i = 0
for imagePath in images:
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb, model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)

    
    for (top, right, bottom, left) in boxes:
        
        # left = int(left-200)
        # top = int(top-300)
        # right = int(right+200)
        # bottom = int(bottom+200)

        # cv2.rectangle(image, (left, top), (right, bottom), (255, 0, 0), 3)
        # y = top-15 if top - 15 > 15 else top+15

        img = image[top:bottom,left:right]
        cv2.imwrite('Data/Untrained/1/'+str(i)+'.jpg', img)
        print(i)
        i +=1
    
    

# image = cv2.resize(image, (0, 0), fx=0.2, fy=0.2)
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()