import cv2
import time
import numpy as np
#out put
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
#Webcam starting
cap = cv2.VideoCapture(0)

#start by making coad sleep for 2sec
time.sleep(2)
bg = 0

#capturing background for 60 frames
for i in range(60):
    ret, bg = cap.read()

#flipping the background
bg = np.flip(bg,axis=1)

#read the captured frame until the camera is open
while (cap.isopen()):
    ret, img = cv2.read()
    if not ret():
        break
#flipping the image for consistency
img = np.flip(img,axis=1)

#converting the color from BGR to HSV
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Generating mask to detect red color
lower_red = np.array([0, 120, 50])
upper_red = np.array([10, 255, 255])
mask_2 = cv2.inRange(hsv, lower_red, upper_red)


lower_red = np.array([170, 120, 70])
ipper_red = np.array([180 , 255, 255])

mask_2 = cv2.inRange(hsv , lower_red, upper_red)


mask_1 = mask_1 + mask_2

#Open and expand the image where there is mask 1(color)
mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_OPEN, np.ONES((3,3), np.uint8))
mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_DILATE, np.ONES((3,3), np.uint8))

#selecting the only part that doesnot have mask 1 and saving in mask 2
mask_2 = cv2.bitwise_not(mask_1)

#keeping the only part of the image withour the red color(or any other color u may choose)
res_1 = cv2.bitwise_and(img, img, mask = mask_2)
#keeping the only part of the image withour the red color(or any other color u may choose)
res_2 = cv2.bitwise_and(bg, bg, mask = mask_1)

#Generating the final output by merging the res 1 and res 2
final_output = cv2.addWeighted(res_1, 1, res_2, 1, 0)
output_file.write(final_output)

#Displayng the output to the user
cv2.imshow('magic', final_output)
cv2.waitKey(1)
cap.release()
out.release()
cv2.destroyAllWindows()

