import os
os.chdir('C:\\Users\\Anonymous\\Documents\\Visual_Studio_files\\PyFiles\\Face_Recognition\\Test-Face-Recognition\\Data\\Abhilash_A')
i = 1

for file in os.listdir():
      src = file
      dst = "Abhilash_A"+str(i)+".jpg"
      os.rename(src, dst)
      i += 1
