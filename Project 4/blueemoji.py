#importing image
import image

#create empty image with width 50 and height 50
img = image.EmptyImage(50,50)

#create a blue pixel
blue_pixel = image.Pixel(0,0,250)

#create black pixel
black_pixel = image.Pixel(0,0,0)

#fill the image in with the blue pixel
for col in range(50):
    for row in range(50):
        img.setPixel(col,row,blue_pixel)

#make the left eye with the black pixel 
for col in range(5,20):
    for row in range(10,25):
        img.setPixel(col,row,black_pixel)
    

#make the right eye with the black pixel 
for col in range(30,45):
    for row in range(10,25):
        img.setPixel(col,row,black_pixel)

#make the mouth for the face
for col in range(10,40):
    for row in range(35,45):
        img.setPixel(col,row,black_pixel)        
    

#display image in a window
win = image.ImageWin("Blue Background", 50,50)
img.draw(win)


