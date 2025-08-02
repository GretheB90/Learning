#Resize image:

from PIL import Image #imports the image class from the PIL(Python imaging Library) package.

#Calling in the original image from folder
img = Image.open('ducksgoesforwalk.png')

#Resizing and saving the new version of the image.
new_image = img.resize((500, 500))
new_image.save('ducksgoesforwalk_500.png')

#Shows the new version of the image in the default image viewer of the System.
new_image.show()

#Extra:
#Resize an image with the Thumbnail function:

#img = image.open('ducksgoesforwalk.png')
#img.thumbnail((200, 200))
#img.save('ducksgoesforwalk_500.png')
#print(img.size) # Output: (400, 350)

#The Aspect ratio of the original image remains unchanged. In addition, if the dimension of the original are smaller than that specified
#for the new instance, instead of "blowing up" the image, thumbnail() returns an instance of the same size.

#Additional tip: Use ANTIALIAS filter for high-quality resizing in Pillow by applying the image.ANTIALIAS filter to reduce aliasing and achieve a smoother result.
