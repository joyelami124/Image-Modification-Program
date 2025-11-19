# Integrity Pledge: The work I am submitting is my own J.O

#-------------------------
# Name: Joshua Oyelami
# Program: L9Q1JO.py
#-------------------------

from PIL import Image

# Purpose: correct the colords on the right half of the pictures

def correct_rhs(picture):
    
    pumpkin = picture
    
    width, height = pumpkin.size
    
    
    for x in range(width):
        for y in range(height):
            if x >= width // 2:
                
                r, g, b = pumpkin.getpixel((x,y))
                
                newr = 255 - r
                newg = 255 - g
                newb = 255 - b
                
                
                pumpkin.putpixel((x,y), (newr,newg,newb))
                

    return pumpkin
            
# Purpose: correct the bottom half of the picture         
        
def correct_bottom(picture):
    
    pumpkin = picture
    
    width, height = pumpkin.size
    
    
    for x in range(width):
        for y in range(height):
            if y >= height // 2:
                
                r, g, b = pumpkin.getpixel((x,y))
                
                if (r, g, b) == (255,190,10):
                
                    pumpkin.putpixel((x,y), (255,255,0))
                
    
    return pumpkin    
    
# Purpose: correct the rectangle turning it into the right color gradient
    
def vary_rect_h(picture):
    
    pumpkin = picture
    
    width, height = pumpkin.size
    
    rect_width = int(0.9 * width)
    rect_height = int(0.08 * height)
    
    rect_y_start = int(0.85 * height)
    rect_y_end = int(rect_y_start + rect_height)
    
    rect_x_start = int(width - rect_width) // 2
    rect_x_end = int(rect_x_start + rect_width)
    
    
    for x in range(rect_x_start, rect_x_end):
        for y in range(rect_y_start, rect_y_end):
            
            transition = (x - rect_x_start) / rect_width
            
            green = int(transition * 255)
            
            pumpkin.putpixel((x,y),(0,green,0))
            
    return pumpkin
    
    
    
def correct_picture(picture):
    
    pic = Image.open(picture)
    
    pic = correct_rhs(pic)
    
    pic.save("pumpkin1.png")

    pic = correct_bottom(pic)
    
    pic.save("pumpkin2.png")
    
    pic = vary_rect_h(pic)
    
    pic.show()
    
correct_picture("pumpkin.png")