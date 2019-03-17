import os
os.chdir('C:\\Users\\Anonymous\\Documents\\GitHub\\Face-Recognition-Neural-Networks\\Data\\Trained\\Maheshwar1')
i = 211

for file in os.listdir():
      src = file
      dst = str(i)+".jpg"
      os.rename(src, dst)
      i += 1
