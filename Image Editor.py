from PIL import Image , ImageEnhance , ImageFilter
import os

img1 = Image.open('My photo.jpeg')
#img1.save('My photo.pdf')
#img1.show()

for item in os.listdir():
    if item.endswith('.jpeg'):
     #img1 = Image.open(item) 
     #filename,extension = os.path.splitext(item)
     #img1.save(f'{filename}.png')
#enhancer = ImageEnhance.Sharpness(img1)
#enhancer.enhance(5).save('My photoedited.jpeg')
     #img1 = Image.open('My photo.jpeg')
#enhancer = ImageEnhance.Brightness(img1)
#enhancer.enhance(1.3).save('My photoedited.jpeg')
     img1 = Image.open('My photo.jpeg')
#enhancer = ImageEnhance.Contrast(img1)
#enhancer.enhance(1.3).save('My photoedited.jpeg')
    img1.filter(ImageFilter.GaussianBlur(radius = 5)).save('My photoedited.png')
 


