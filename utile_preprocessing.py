import random
import cv2
import numpy as np

def salt_and_pepper(img): 

    # Getting the dimensions of the image 
    row , col, n = img.shape
      
    # Randomly pick some pixels in the 
    # image for coloring them white 
    # Pick a random number between 300 and 10000 
    number_of_pixels = random.randint(1000, 8000) 
    for i in range(number_of_pixels): 
        
        # Pick a random y coordinate 
        y_coord=random.randint(0, row - 1) 
          
        # Pick a random x coordinate 
        x_coord=random.randint(0, col - 1) 
          
        # Color that pixel to white 
        img[y_coord][x_coord] = 255
          
    # Randomly pick some pixels in 
    # the image for coloring them black 
    # Pick a random number between 300 and 10000 
    # number_of_pixels = random.randint(300 , 10000) 
    # for i in range(number_of_pixels): 
        
    #     # Pick a random y coordinate 
    #     y_coord=random.randint(0, row - 1) 
          
    #     # Pick a random x coordinate 
    #     x_coord=random.randint(0, col - 1) 
          
    #     # Color that pixel to black 
    #     img[y_coord][x_coord] = 0
          
    return img 





def noisy_averageBlurring (image, kX, kY) :
    return cv2.blur(image, (kX, kY))

def noisy_gaussianBlurring (image, kX=5, kY=5) :
    return cv2.GaussianBlur(image, (kX, kY), 0)

def noisy_medianBlurring (image, k=3) :
    return cv2.medianBlur(image, k)