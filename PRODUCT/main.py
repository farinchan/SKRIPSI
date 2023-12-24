import numpy as np
import cv2
from deepface import DeepFace
import json
import matplotlib

test =  input("Jumlah orang yang ingin di input (1 - 10) : ")
for i in range(int(test)):
    print(i)
     
person1 = []

webcam = cv2.VideoCapture(0)    

while True:
    success, img= webcam.read()
    
    
    try:
        # output = DeepFace.verify("./face/inan.JPG",img)
        # print(output)
        prediction = DeepFace.analyze(img, actions = ['emotion'])
        person1.append(prediction[0])
        print(prediction[0])
        shape = prediction[0]['region']
        print("gegelupada : ",shape)
        img = cv2.rectangle(img,(shape['x'],shape['y']),(shape['x']+shape['w'],shape['y']+shape['h']),(255,0,0),2)
    except:
        pass
    
        # Serializing json
    json_object = json.dumps({
        "person1" : person1
    })
    
    # Writing to sample.json
    with open("db.json", "w") as outfile:
        outfile.write(json_object)
    
    cv2.imshow("Hasil", img)
    
    interupt = cv2.waitKey(10)
    if interupt & 0xFF == 27:
        break
    
webcam.release()
cv2.destroyAllWindows()