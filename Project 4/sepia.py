#importing image
import image

#grab picture image
img = image.Image("my_image.gif")

#get the dimensions (width & hight) of the picture 
width = img.getWidth()
height = img.getHeight()

#creating an empty image with the width and height of the image
new_img = image.EmptyImage(width, height)

#create for loop to transform the image color to old timey
for row in range(height):
    for col in range(width):
        v = img.getPixel(col,row)
        red = v.getRed()
        blue = v.getBlue() 
        green = v.getGreen()
        new_red = int(red * 0.393) + int(green * 0.769) + int(blue * 0.189)
        new_green = int(red * 0.349) + int(green * 0.686) + int(blue * 0.168)
        new_blue = int(red * 0.272) + int(green * 0.534) + int(blue * 0.131)
        
        if new_red > 255:
            new_red = 255
        elif new_green > 255:
            new_green = 255
        elif new_blue > 255:
            new_blue = 255
            
        v.red = new_red
        v.green = new_green 
        v.blue = new_blue
        new_img.setPixel(col,row,v)
        
#display image in a window
win = image.ImageWin("Old timey Image", width, height)
new_img.draw(win)
