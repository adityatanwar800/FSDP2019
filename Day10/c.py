# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 17:08:52 2019

@author: Aditya Tanwar
"""
from PIL import Image 
 
from PIL import ImageFont
from PIL import ImageDraw
def main(): 
    try: 
        #Relative Path 
        #Image on which we want to paste 
        img = Image.open("C:\\Users\\Aditya Tanwar\\Desktop\\FSSDP2019\\Day10\\templates.jpg")  
          
        #Relative Path 
        #Image which we want to paste 
        img2 = Image.open("C:\\Users\\Aditya Tanwar\\Desktop\\FSSDP2019\\Day10\\Forsk.jpg")  
        img.paste(img2, (420, 470)) 
          
        #Saved in the same relative location 
        img.save("pasted_picture.jpg") 
          
    except IOError: 
        pass
  
if __name__ == "__main__": 
    main()

img = Image.open("C:\\Users\Aditya Tanwar\\Desktop\\FSSDP2019\\Day10\\pasted_picture.jpg")
draw = ImageDraw.Draw(img)
selectFont = ImageFont.truetype("arial.ttf", size = 40)
achiv= input("ENTER the achivement :")
name= input("ENTER the name :")
date=input("ENTER the date :")

draw.text( (330,260), achiv, (255,0,0), font=selectFont)
draw.text( (340,410), name, (255,0,0), font=selectFont)
draw.text( (190,482), date, (255,0,0), font=selectFont)

img.save( 'certi.jpg', "JPEG", resolution=100.0)    
      
