import numpy as np
#background1,free,Photo by Craig Adderley from Pexels
#background2,free,Photo by James Wheeler from Pexels
#this article helped me for the eproject:
# https://stackoverflow.com/questions/52179821/python-3-i-am-trying-to-find-find-all-green-pixels-in-an-image-by-traversing-al
#https://stackoverflow.com/questions/765736/using-pil-to-make-all-white-pixels-transparent
from PIL import Image
def composite_image(image,background):
 imagee = Image.open(image).convert('RGB')#make the image rgb
 imageeHSV = imagee.convert('HSV')#make the image HSV
 arrayRGB= np.array(imagee)#use np to array for HSV and RGb
 arrayHSV = np.array(imageeHSV)
 hue = arrayHSV[:,:,0]#get the hue from the image
 minRange,maxRange = 170,250#blue color range, to calculate the pixels, if number is low another value for green will replace it
 minRange = int((minRange * 255) / 360)#adjust the rescale
 maxRange = int((maxRange * 255) / 360)
 blueRange = np.where((hue>minRange) & (hue<maxRange))
 arrayRGB[blueRange] = [0,0,0]#make the pixels after extraction to black
 number = blueRange[0].size

 #if blue image so its ok, if green the belwo code with if will make it.
 if number<32:
    arrayRGB = np.array(imagee)
    arrayHSV = np.array(imageeHSV)
    hue = arrayHSV[:, :, 0]
    min_range,max_range = 105,160
    minRange = int((min_range * 255) / 360)
    maxRange = int((max_range * 255) / 360)
    greenRange = np.where((hue > minRange) & (hue < maxRange))
    arrayRGB[greenRange] = [0, 0, 0]

#now save it and make it with the background
 Image.fromarray(arrayRGB).save('result.png')
 imggg = Image.open('result.png')
 imggg = imggg.convert("RGBA")
 dataaa = imggg.getdata()

 NewLsitForData = []
 for item in dataaa:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
        NewLsitForData.append((0, 0, 0, 0))
    else:
        NewLsitForData.append(item)

 imggg.putdata(NewLsitForData)
 imggg.save("img2.png", "PNG")
 im1 = Image.open(background)
 im2=Image.open('img2.png')

 image6 = im1.convert("RGBA")
 image5 = im2.convert("RGBA")
 image6.paste(image5, (0, 0), image5)
 image6.show()

def main():
   composite_image("jack.jpg","background1.jpg")
   composite_image("guard.jpg","background2.jpg")
if __name__ == '__main__':
    main()
