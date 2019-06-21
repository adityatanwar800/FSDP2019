# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 09:13:33 2019

@author: Aditya Tanwar
"""
from PIL import Image
import os
img = Image.open("sample.jpg")

img.thumbnail((75, 75))
print(img.width, img.height)
img.save('thumb_sample1.jpg')
img.show()

img_bw = Image.open("sample.jpg")
img_bw.convert(mode='L').save('sample3.jpg')
img_bw = Image.open("sample3.jpg")
img_bw.show()

img = Image.open("sample.jpg")
                    # startx, starty,width,height
crop_im = img.crop(box=(340, 20, 560, 164))
crop_im.save('crop_sample1.jpg')
img.show()

