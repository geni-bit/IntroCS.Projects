"""
Before changing any code below, run this to
make sure eiffel.gif and image.py are in the
correct folder
"""

import image

#grab picture
img = image.Image("eiffel.gif")
#get dimensions of picture
width = img.getWidth()
height = img.getHeight()

#create blank canvas
new_img = image.EmptyImage(width, height)

for row in range(height):
    for col in range(width):
        v = img.getPixel(col,row)
        red = v.getRed()
        blue = v.getBlue()
        green = v.getGreen()
        #change color intensities by filling in the assignment and uncommenting
        v.red = blue
        v.green = red
        v.blue = green
        new_img.setPixel(col,row,v)

#create window/canvas with correct dimensions
win = image.ImageWin("Inverted Eiffel", width, height)
new_img.draw(win)
