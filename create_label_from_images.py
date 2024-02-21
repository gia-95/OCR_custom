import os
import cv2
import matplotlib.pyplot as plt



directory = 'image_dataset'
train_labels = []

with open('labels.txt', 'w') as f:

    for filename in os.listdir(directory):

        if (filename == '.DS_Store') :
            continue

        pathFile = os.path.join(directory, filename)

        # checking if it is a file
        if os.path.isfile(pathFile):

            print("PathFile corrente: ", pathFile)
            
            img = cv2.imread(pathFile)

            fig, ax = plt.subplots()
            ax.imshow(img)
            plt.show(block=False)
            plt.pause(1)
            
            word = input('Nome immagine: ')

            plt.close(fig)

            if (word == '0') :
                continue
            elif (word == 'end') :
                break

            tupla = (pathFile, None, word)

            print("tupla insert --> ", tupla)
            print()
            print()

            train_labels.append(tupla)


            stringToInsert = f'(\'{pathFile}\', None, \'{word}\'), '

            f.write(stringToInsert)