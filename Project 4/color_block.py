#create a color block
import image

#create empty image with width 100 and height 100
img = image.EmptyImage(100,100)

#create all color pixels you want
red_pixel = image.Pixel(250,0,0)
green_pixel = image.Pixel(0,250,0)
blue_pixel = image.Pixel(0,0,250)

#fill in upper left corner with red
for col in range(0,50):
    for row in range(0,50):
        img.setPixel(col,row,red_pixel)

#fill in upper right corner with blue
for col in range(50,100):
    for row in range(0,50):
        img.setPixel(col,row,blue_pixel)

#fill in lower left corner with green
for col in range(0,50):
    for row in range(50,100):
        img.setPixel(col,row,green_pixel)

#fill in lower right corner with red
for col in range(100,50):
    for row in range(50,100):
        img.setPixel(col,row,red_pixel)

#display image in a window
win = image.ImageWin("Color Block",100,100)
img.draw(win)
