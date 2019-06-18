# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 18:02:18 2019

@author: Aditya Tanwar
"""

from PIL import Image 
 
from PIL import ImageFont
from PIL import ImageDraw
def main(): 
    try: 
        #Relative Path 
        #Image on which we want to paste 
        img = Image.open("C:\\Users\\Aditya Tanwar\\Desktop\\FSSDP2019\\Day10\\id02.jpg")  
          
        #Relative Path 
        #Image which we want to paste 
        img2 = Image.open("C:\\Users\\Aditya Tanwar\\Desktop\\FSSDP2019\\Day10\\photo02.jpg")  
        img.paste(img2, (260, 120)) 
        
          
        #Saved in the same relative location 
        img.save("pasted.jpg") 
          
    except IOError: 
        pass
  
if __name__ == "__main__": 
    main()

img = Image.open("C:\\Users\Aditya Tanwar\\Desktop\\FSSDP2019\\Day10\\pasted.jpg")
draw = ImageDraw.Draw(img)
selectFont = ImageFont.truetype("arial.ttf", size = 18)
comp=input("enter the company namne :")
name= input("ENTER the name :")
serial= input("ENTER the serial:")
valid= input("ENTER the valid upto:")
date=input("ENTER the date :")
unit= input("ENTER the unit:")
nos=input("ENTER the number:")

draw.text((110,30),comp,(255,0,0),font=selectFont)
draw.text( (310,320), name, (255,0,0), font=selectFont)
draw.text( (310,350), serial, (255,0,0), font=selectFont)
draw.text( (310,390), valid, (255,0,0), font=selectFont)
draw.text( (310,420), date, (255,0,0), font=selectFont)
draw.text( (310,450), unit, (255,0,0), font=selectFont)
draw.text( (310,480), nos, (255,0,0), font=selectFont)

img.save( 'id1.jpg', "JPEG", resolution=100.0)  