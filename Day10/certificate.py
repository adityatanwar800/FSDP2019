# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:58:20 2019

@author: Aditya Tanwar
"""
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("C:\\Users\Aditya Tanwar\\Desktop\\FSSDP2019\\Day10\\templates.jpg")
draw = ImageDraw.Draw(img)
selectFont = ImageFont.truetype("arial.ttf", size = 40)
achiv= input("enter the achivement")
name= input("enter the name")

draw.text( (330,260), achiv, (255,0,0), font=selectFont)
draw.text( (340,410), name, (255,0,0), font=selectFont)
img.save( 'certi.jpg', "JPEG", resolution=100.0)    
      