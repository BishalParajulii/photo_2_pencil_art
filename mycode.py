import cv2
image = cv2.imread("kale.jpg")

# convert to grey scale
grey_filter = cv2.cvtColor( image , cv2.COLOR_BGR2GRAY)

#invert the color
invert  = cv2.bitwise_not(grey_filter)

#blur the color
blur = cv2.GaussianBlur(invert , (45,45) , 0)

#inverted blurr
invertedBlur = cv2.bitwise_not(blur)


#convert to sketch
sketch = cv2.divide(grey_filter , invertedBlur , scale=256.0)

#save the image
cv2.imwrite("output.png" , sketch)