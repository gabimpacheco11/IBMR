# importando as bibliotecas
import cv2 
import numpy as np
#from IPython.display import Image
import matplotlib.pyplot as plt
import matplotlib

# leitura da imagem
img = cv2.imread('imagem.jpg')

# Apresentacao da imagem na tela
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#plt.show()

#Dimensão das imagens
plt.rcParams['figure.figsize'] =(224,224)

# Classificador construido para detectar faces
face_cascade = cv2.CascadeClassifier('app/haarcascade_frontalface_default.xml')

# Transformando a imagem em escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Processo para detectar as faces na imagem
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

count = 0
for(x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y), (x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    count += 1

    cv2.imwrite('aragorn.png',img)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()