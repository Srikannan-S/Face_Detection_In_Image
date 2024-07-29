import cv2

alg="haarcascade_frontalface_default.xml"

# Loading the algorithm

haar_cascade=cv2.CascadeClassifier(alg)

# Reading the image

img=cv2.imread("cricket.jpg")

# Converting into Gray_Scale

Gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Getting the Co-ordinates

face=haar_cascade.detectMultiScale(Gray_img,1.3,3)

for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),2)
cv2.imshow("Face_Detection",img)

cv2.waitKey(5000)
cv2.destroyAllWindows()
