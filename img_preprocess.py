import cv2
import numpy as np

# NOT NOISE
def remove_noise(image):
    return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15)

# Rotate image
def rotate(image, angle) :
    # rotate the image to deskew it
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h),
        flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


# Aggiusta rotazione
def addrizzaImmagine(box, image_notNoise) :
    diff_Y_angoli = box[1][1] - box[0][1] 
    stringa_stampa = 'Rotazione immagine:'

    # print(box)
    # print("Diff Y:", diff_Y_angoli)

    # compreso tra 2 e 6
    if (diff_Y_angoli > 2 and diff_Y_angoli <= 6) :
        gradi_rotazione = 1
        # print(f'{stringa_stampa} {gradi_rotazione}°')
        return rotate(image_notNoise, gradi_rotazione)
    
    # compreso tra 6 e 12
    elif (diff_Y_angoli >= 6 and diff_Y_angoli <= 12) :
        gradi_rotazione = 2
        # print(f'{stringa_stampa} {gradi_rotazione}°')
        return rotate(image_notNoise, gradi_rotazione)
    
    # compreso tra 13 e 15
    elif (diff_Y_angoli >= 13 and diff_Y_angoli <= 15) :
        gradi_rotazione = 3
        # print(f'{stringa_stampa} {gradi_rotazione}°')
        return rotate(image_notNoise, gradi_rotazione)
    
    # compreso tra 16 e 20
    elif (diff_Y_angoli >= 16 and diff_Y_angoli <= 20) :
        gradi_rotazione = 4
        # print(f'{stringa_stampa} {gradi_rotazione}°')
        return rotate(image_notNoise, gradi_rotazione)

    # compreso tra -2 e -6
    if (diff_Y_angoli < -2 and diff_Y_angoli >= -6) :
        gradi_rotazione = -1
        # print(f'{stringa_stampa} {gradi_rotazione}°')
        return rotate(image_notNoise, gradi_rotazione)
    
    # compreso tra -6 e -12
    elif (diff_Y_angoli <= -6 and diff_Y_angoli >= -12) :
        gradi_rotazione = -2
        # print(f'{stringa_stampa} {gradi_rotazione}°')
        return rotate(image_notNoise, gradi_rotazione)
    
    # compreso tra -13 e -15
    elif (diff_Y_angoli <= -13 and diff_Y_angoli >= -15) :
        gradi_rotazione = -3
        # print(f'{stringa_stampa} {gradi_rotazione}°')
        return rotate(image_notNoise, gradi_rotazione)
    
    # compreso tra -16 e -20
    elif (diff_Y_angoli <= -16 and diff_Y_angoli >= -20) :
        gradi_rotazione = 4
        # print(f'{stringa_stampa} {gradi_rotazione}°')
        return rotate(image_notNoise, gradi_rotazione)

    return image_notNoise


def aggiustaContrasto(image) :
    stringa_stampa = 'Incremento contrasto:'

    # Valore contrasto 
    img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    contrast = img_grey.std()
    # print("Contrasto originale:",contrast)

    # Contrasto tra 0 e 20
    if (contrast >= 0 and contrast <=20) :
        valore_imcremento_contrasto = 2
        # print(f'{stringa_stampa} {valore_imcremento_contrasto} %')
        return cv2.convertScaleAbs(image, alpha=valore_imcremento_contrasto)

    # Contrasto tra 21 e 40
    if (contrast >= 21 and contrast <=40) :
        valore_imcremento_contrasto = 1.2
        # print(f'{stringa_stampa} {valore_imcremento_contrasto}%')
        return cv2.convertScaleAbs(image, alpha=valore_imcremento_contrasto)

    return image





# Tienilo qui IMPORTANTE
# estrai le boundingbox e le salva
# for idx,box in enumerate(boxes) :

#     # Trasforma arrai in INT
#     box = box.astype('int64')

#     img_crop = image[box[0][1]:box[2][1], box[0][0]:box[2][0] ]
    
#     pathFile = f'cropped_noise2/img_{idx+1}.png'

#     cv2.imwrite(pathFile, img_crop)