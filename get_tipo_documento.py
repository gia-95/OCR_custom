import cv2 
import matplotlib.pyplot as plt
import keras_ocr 


def get_rappporto_dimensione(image) :
    return image.shape[1] / image.shape[0]


def elabora_tipologia(image, detector, recognizer) :
    sanitaria_fronte =  ['regionale', 'servizi']
    sanitaria_retro = ['europea', 'assicurazione', 'malattia']
    identita_nuova_fronte = ['ministero', 'dell', 'dellinterno', 'interno']
    identita_nuova_retro = ['padre', 'madre', 'veci']
    patente_fronte  = ['patente', 'guida'] 
    patente_retro  = ['am', 'a1', 'a2'] 
    SOGLIA_PIXEL_Y = 300
    categoria = 'Non riconosciuta...'

    rapporto_h_w  = get_rappporto_dimensione(image)
    
    if (rapporto_h_w < 1.45) :
        categoria = 'Carta identita vecchia'
        return categoria

    
    # Resize (1400 x 900)
    image_resize = cv2.resize(image, (1400, 900), interpolation=cv2.INTER_CUBIC)

    boxes = detector.detect(images=[image_resize])[0]
    
    for idx, box in enumerate(boxes) :
        
        box = box.astype('int64')

        px_y = box[2][1]

        
        if (px_y > SOGLIA_PIXEL_Y) :
            continue
        
        label_cropped_img = image_resize[box[0][1]:box[2][1], box[0][0]:box[2][0] ]
        # plt.imshow(label_cropped_img)
        # plt.show()

        try :
            word_predicted = recognizer.recognize(label_cropped_img)
            # print(word_predicted)
        except :
            print("Errore recognizer parola.")
            continue

        if word_predicted in sanitaria_fronte : 
            categoria = 'Tessera sanitaria - fronte'
            break
        elif word_predicted in sanitaria_retro : 
            categoria = 'Tessera sanitaria - retro'
            break
        elif word_predicted in identita_nuova_fronte : 
            categoria = 'Carta di identità - fronte'
            break
        elif word_predicted in identita_nuova_retro : 
            categoria = 'Carta di identità - retro'
            break
        elif word_predicted in patente_fronte : 
            categoria = 'Patente - fronte'
            break
        elif word_predicted in patente_retro : 
            categoria = 'Patente - retro'
            break

    return categoria
