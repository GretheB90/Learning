#How many pixels are there in this image:

from PIL import Image #imports the image class from the PIL(Python imaging Library) package.

#This part is to open the image in image viewer to test it works and has the correct direction to the file.

#Loading the image and adds it to the img variable.
img = Image.open('ducksgoesforwalk.png')

#Shows us the image in the default image viewer on the system.
img.show()

#Fetching the dimensions:
wid, hgt = img.size

#Displays the dimensions:
print(str(wid) + 'x' + str(hgt))
