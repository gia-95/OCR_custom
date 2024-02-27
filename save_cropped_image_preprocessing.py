import keras_ocr
import matplotlib.pyplot as plt
import tensorflow as tf # 2.14.0
import cv2
import img_preprocess
import os

detector = keras_ocr.detection.Detector(weights='clovaai_general')
print()

cartella_documenti = 'documenti'

cartella_dataset = 'image_dataset'

numero_immagine = 1
numero_immagini_salvate = 0

# Cicla su tutti i documenti
for file_name in os.listdir(cartella_documenti) :
    if (file_name == '.DS_Store') :
            continue

    print(f'Analizzo file: {file_name}...')
    
    image_original = keras_ocr.tools.read(f'{cartella_documenti}/{file_name}')

    # Bounding-boxes immagine corrente
    boxes_orignial = detector.detect(images=[image_original])[0]    
    
    for idx,box in enumerate(boxes_orignial) :

        try :
            # Trasforma arrai in INT
            box = box.astype('int64')
            # Ritaglia bounding-box corrente da immagine...
            parola_cropped = image_original[box[0][1]:box[2][1], box[0][0]:box[2][0] ]    

            # Per renderla formato giusto per funzioni
            cv2.imwrite("temp.png", parola_cropped)
            img_cropped = cv2.imread('temp.png')

            # Addrizza immagine
            imagine_addrizzata = img_preprocess.addrizzaImmagine(box, img_cropped)
            cv2.imwrite("temp_addrizza.png", imagine_addrizzata)
            imagine_addrizzata = cv2.imread('temp_addrizza.png')

            # Regola contrasto e luminosità
            imagine_elaborata = img_preprocess.aggiustaContrasto(imagine_addrizzata)
            cv2.imwrite("temp_contrastoLuminosita.png", imagine_elaborata)
            imagine_elaborata = cv2.imread('temp_contrastoLuminosita.png')

            # SALVA IMMAGINE IN CARTELLA -> 'image_dataset'
            nome_img_da_salvare = f'image_dataset2/img_{numero_immagine}.png'
            cv2.imwrite(nome_img_da_salvare, imagine_elaborata)

            # incrementa contatore immagine
            numero_immagine = numero_immagine + 1

        except:
            print(f'Errore in immagine: {file_name}')
            numero_immagini_salvate = numero_immagini_salvate - 1
            
            
    numero_immagini_salvate = numero_immagini_salvate + idx + 1
    print(f'Bounding-boxes trovate: ',idx)
    print()

print("TOTALI:", numero_immagini_salvate)
    
    