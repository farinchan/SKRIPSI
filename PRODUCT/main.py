import numpy as np
import cv2
from deepface import DeepFace
import matplotlib

webcam = cv2.VideoCapture(0)    

while True:
    success, img= webcam.read()
    
    try:
        prediction = DeepFace.analyze(img, actions = ['emotion'])
        print(prediction[0]['dominant_emotion'])
        shape = prediction[0]['region']
        print("gegelupada : ",shape)
        img = cv2.rectangle(img,(shape['x'],shape['y']),(shape['x']+shape['w'],shape['y']+shape['h']),(255,0,0),2)
    except:
        pass

    cv2.imshow("Hasil", img)
    
    interupt = cv2.waitKey(10)
    if interupt & 0xFF == 27:
        break
    
webcam.release()
cv2.destroyAllWindows()