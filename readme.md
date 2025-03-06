Criando e ativando variaveis de ambiente

python -m venv venv
venv\Scripts\activate

============================================================================================

# Detecção de Rostos com OpenCV

Este projeto utiliza a biblioteca **OpenCV** para detectar rostos em uma imagem e exibi-los com um retângulo ao redor. O código também salva a imagem processada.

## Explicação do Código

### 1. Importação das bibliotecas
```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
```
- `cv2`: Biblioteca OpenCV para processamento de imagens.
- `numpy`: Biblioteca para manipulação de arrays.
- `matplotlib.pyplot`: Usada para exibição da imagem.

### 2. Leitura da Imagem
```python
img = cv2.imread('imagem.jpg')
```
Carrega a imagem chamada **"imagem.jpg"**.

### 3. Exibição da Imagem
```python
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
```
- O OpenCV carrega imagens no formato **BGR**, enquanto o Matplotlib usa **RGB**.
- A função `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` faz essa conversão antes de exibir a imagem.

### 4. Ajuste do Tamanho da Figura
```python
plt.rcParams['figure.figsize'] =(224,224)
```
Define o tamanho da imagem exibida para **224x224** pixels.

### 5. Carregamento do Classificador de Rostos
```python
face_cascade = cv2.CascadeClassifier('app/haarcascade_frontalface_default.xml')
```
- Usa o modelo **Haar Cascade** treinado para detectar rostos.
- O arquivo `'haarcascade_frontalface_default.xml'` contém as regras para identificar faces.

### 6. Conversão para Escala de Cinza
```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
A detecção de rostos funciona melhor em imagens monocromáticas, pois reduz a complexidade.

### 7. Detecção de Rostos
```python
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)
```
- `scaleFactor=1.1`: Reduz o tamanho da imagem em **10%** a cada escala, ajudando a detectar rostos de diferentes tamanhos.
- `minNeighbors=5`: Evita falsos positivos ao exigir pelo menos **5 vizinhos** para validar uma detecção.
- `minSize=(30, 30)`: Define o tamanho mínimo do rosto detectado.

### 8. Desenhando Retângulos nos Rostos Detectados
```python
count = 0
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
```
- Percorre cada rosto detectado e desenha um **retângulo azul (255,0,0)** ao redor.
- `(x, y)`: Coordenadas do canto superior esquerdo do rosto.
- `(x + w, y + h)`: Coordenadas do canto inferior direito.
- `2`: Espessura da linha do retângulo.

### 9. Recorte das Regiões do Rosto
```python
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
```
- `roi_gray`: Recorta a região do rosto na imagem em escala de cinza.
- `roi_color`: Recorta a região do rosto na imagem colorida.

### 10. Salvando a Imagem Processada
```python
    cv2.imwrite('aragorn.png', img)
```
Salva a imagem com os rostos detectados e os retângulos desenhados com o nome **"aragorn.png"**.

### 11. Exibição da Imagem Processada
```python
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
```
- Converte a imagem para **RGB** novamente.
- Exibe a imagem processada com os rostos detectados.

## Resultado Esperado
A imagem carregada terá um retângulo azul ao redor de cada rosto detectado e será salva como **"aragorn.png"**.

## Observação
Caso a imagem não contenha rostos ou o classificador não esteja bem treinado para a imagem fornecida, pode ser necessário ajustar os parâmetros `scaleFactor` e `minNeighbors` para melhorar a detecção.

