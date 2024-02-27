import os
import cv2
import matplotlib.pyplot as plt



directory_subset = 'image_dataset/subset_7'
file_label_txt = 'labels/labels7.txt'
file_label_to_delte_txt = 'labels/label_to_delete.txt'

train_labels = []

tot = 0

for filename in os.listdir(directory_subset):
    tot = tot+1

indice = 1

with open(file_label_txt, 'a') as f:

    for filename in os.listdir(directory_subset):

        if (filename == '.DS_Store') :
            continue

        pathFile = os.path.join(directory_subset, filename)

        # checking if it is a file
        if os.path.isfile(pathFile):

            print(f'{indice}/{tot}')
            print("PathFile corrente: ", pathFile)
            
            img = cv2.imread(pathFile)

            fig, ax = plt.subplots()
            ax.imshow(img)
            plt.show(block=False)
            plt.pause(0.1)
            
            word = input('Nome immagine: ')

            plt.close(fig)

            if (word == '00') :
                os.remove(pathFile)
                # tupla_delete = filename + ", "
                # with open(file_label_to_delte_txt, 'a') as f1:
                #     f1.write(tupla_delete)
                continue

            elif (word == 'end') :
                break

            tupla = (f'image_dataset/{filename}', None, word)

            print("->",tupla)
            print()
            print()

            train_labels.append(tupla)


            stringToInsert = f'(\'image_dataset/{filename}\', None, \'{word}\'), '

            f.write(stringToInsert)

            indice = indice+1