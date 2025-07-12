#importing image
import image

#grab picture image
img = image.Image("my_image.gif")

#get the dimensions (width & hight) of the picture 
width = img.getWidth()
height = img.getHeight()

#creating an empty image with the width and height of the image
new_img = image.EmptyImage(width, height)

#create for loop to flip horizontal the image 
for row in range(height):
    for col in range(width):
        v = img.getPixel(col,row)
        new_img.setPixel(height-1-col,width-1-row,v)
        

win = image.ImageWin("Flipped Cat Image",width,height)

new_img.draw(win)
