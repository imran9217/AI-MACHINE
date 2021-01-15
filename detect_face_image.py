import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('lepo.png')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()
from tkinter import *
# from PIL import Image
from tqdm import tqdm



loop =tqdm(total = 5000, position=0,leave =False)
for k in range(5000):
    loop.set_description("Loading...".format(k))
    loop.update(1)
loop.close

from tqdm.auto import tqdm
for i in tqdm(range(100000001)):
    print()
    print("",end='\t')
    loop = tqdm(total=5000, position=0, leave=False)
    for k in range(3000):
        loop.set_description("Loading... FACE ...".format(k))
        loop.update(1)




def loading_fun():
    lod_root =Tk()
    lod_root.state('zoomed')
    lod_root.configure(bg='brown')

    # im = Image.open('g.gif')

    # im=PhotoImage(file="g.gif")
    # lable_1 =Label(lod_root, image=im)
    # lable_1.pack(expand=100)





    lod_root.mainloop()


loading_fun()