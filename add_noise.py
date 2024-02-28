import cv2
import matplotlib.pyplot as plt
import utile_preprocessing as up
import os
import utile_labels as ul
import random



labels = ul.get_labels_tot()
print(len(labels))


directory_to_read = 'image_dataset/subset_2'
direcotry_to_write_image = 'image_dataset_noise'
file_labels = 'labels/noisy_labels.txt'
rand_array = [3, 5]


with open(file_labels, 'a') as f:

    for filename in os.listdir(directory_to_read):
        
        pathFile = f'{directory_to_read}/{filename}'

        image = cv2.imread(pathFile)

        filename_gauss = f'{direcotry_to_write_image}/noise_gauss_{filename}'
        gaussian_blur = up.noisy_gaussianBlurring(image, 5, 5)
        cv2.imwrite(filename_gauss, gaussian_blur)


        filename_median = f'{direcotry_to_write_image}/noise_median_{filename}'
        median_blur = up.noisy_medianBlurring(image, random.choice(rand_array)) # 3 o 5
        cv2.imwrite(filename_median, median_blur)


        word_to_insert = 'xxx'
        for (path, neinte, word) in labels :
            if (path.split('/')[1] == filename) :
                word_to_insert = word
                break


        string_gauss = f'(\'image_dataset/noise_gauss_{filename}\', None, \'{word_to_insert}\'), '
        string_median = f'(\'image_dataset/noise_median_{filename}\', None, \'{word_to_insert}\'), '

        f.write(string_gauss)
        f.write(string_median)

        break
    


    