import keras_ocr
# import matplotlib.pyplot as plt
import random
import cv2


directory_images = 'images_cf2'
file_labels = 'labels/labels_cf2.txt'

total_digits = '0123456789ABCDEFGHILMNOPQRSTUVZ'
letters_alph = 'ABCDEFGHILMNOPQRSTUVZ'
numbers_aplh = '0123456789'
fonts = ['fonts/40474_VerdanaBold.ttf', 'fonts/TitilliumWeb-Bold.ttf', 'fonts/TitilliumWeb-Regular.ttf', 'fonts/TitilliumWeb-SemiBold.ttf']

fonts_temp = ['fonts/TitilliumWeb-SemiBold.ttf']

def generate_random_CF(): 
    # es. 'GHLCVN 65 H 05 H 501 N'
    cf_random_array = []

    # 6 lettere
    for n in range(6) :
        lettera_random = letters_alph[random.randint(0, len(letters_alph)-1)]
        cf_random_array.append(lettera_random)

    # 2 numeri 
    for n in range(2) :
        numero_rand = numbers_aplh[random.randint(0, len(numbers_aplh)-1)]
        cf_random_array.append(numero_rand)

    # 1 lettera
    for n in range(1) :
        lettera_random = letters_alph[random.randint(0, len(letters_alph)-1)]
        cf_random_array.append(lettera_random)

    # Prime 2 numeri
    for n in range(2) :
        numero_rand = numbers_aplh[random.randint(0, len(numbers_aplh)-1)]
        cf_random_array.append(numero_rand)

    # 1 lettera
    for n in range(1) :
        lettera_random = letters_alph[random.randint(0, len(letters_alph)-1)]
        cf_random_array.append(lettera_random)

    # 3 numeri
    for n in range(3) :
        numero_rand = numbers_aplh[random.randint(0, len(numbers_aplh)-1)]
        cf_random_array.append(numero_rand)

    # 1 lettera
    for n in range(1) :
        lettera_random = letters_alph[random.randint(0, len(letters_alph)-1)]
        cf_random_array.append(lettera_random)


    cf_random = '' 
    for ele in cf_random_array: 
        cf_random += ele

    return cf_random


def generate_rand_image_and_text() :
    
    font = 'fonts/40474_VerdanaBold.ttf'
    width = 350

    image, line = keras_ocr.data_generation.draw_text_image(
        generate_random_CF(), 
        fontsize=25, 
        height=35, 
        width=width, 
        fonts={
            total_digits: font
        },
        thetaX=0,
        thetaY=0,
        thetaZ=0, 
        )    
    text = keras_ocr.data_generation.convert_lines_to_paragraph(line)

    return image, text


def add_noise(img): 
  
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



def main(numero_immagini_to_create=10) :

    with open(file_labels, 'w') as f:

    
        for n in range(numero_immagini_to_create) :
            image, text = generate_rand_image_and_text()

            image = add_noise(image)

            nome_immagine = f'img_{n+1}.jpg'

            cv2.imwrite(f'{directory_images}/{nome_immagine}', image)

            tupla = f'(\'{directory_images}/{nome_immagine}\', None, \'{text.lower()}\'), '
            
            f.write(tupla)

main(8000)
            

# for n in range(20) :
#     image, text = generate_rand_image_and_text()
#     plt.imshow(image)
#     plt.pause(1)
#     plt.close()
