#importing image
import image

#grab picture image
img = image.Image("my_image.gif")

#get the dimensions (width & hight) of the picture 
width = img.getWidth()
height = img.getHeight()

#creating an empty image with the width and height of the image
new_img = image.EmptyImage(width, height)

#create for loop to transform the image color to black and white
for row in range(height):
    for col in range(width):
        v = img.getPixel(col,row)
        red = v.getRed()
        blue = v.getBlue()
        green = v.getGreen()
        avg_color = int((red + green + blue)/3)

        v.red = avg_color
        v.green = avg_color
        v.blue = avg_color 
        new_img.setPixel(col,row,v)
        
#display image in a window
win = image.ImageWin("Black and White", width, height)
new_img.draw(win)
