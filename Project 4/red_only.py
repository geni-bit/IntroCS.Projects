#importing image
import image

#grab picture image
img = image.Image("my_image.gif")

#get the dimensions (width & hight) of the picture 
width = img.getWidth()
height = img.getHeight()

#creating an empty image with the width and height of the image
new_img = image.EmptyImage(width, height)

#create for loop to transform the image color to red
for row in range(height):
    for col in range(width):
        v = img.getPixel(col,row)
        v.setBlue(0)
        v.setGreen(0)
        new_img.setPixel(col,row,v)
        
#display image in a window
win = image.ImageWin("Red Cat Image", width, height)
new_img.draw(win)
