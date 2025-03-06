from sklearn.cluster import KMeans
import numpy as np

# Aqui criamos um array 2D (X) que contém 6 pontos no espaço bidimensional (x, y):
X = np.array([[1,2], [1,4], [1,0], [4,2], [4,4], [4,0]])

#Se fosse um grafico seria assim:
#    y
#    ↑
#  4 |  (1,4)       (4,4)
#  3 |
#  2 |  (1,2)       (4,2)
#  1 |
#  0 |  (1,0)       (4,0)
#    ------------------→ x

#Criamos um modelo KMeans configurado para 2 clusters (n_clusters=2).
# random_state=0 garante que o resultado seja sempre o mesmo (pois o algoritmo K-Means pode ser sensível à inicialização dos centróides).
#.fit(X) treina o modelo, agrupando os pontos de X em 2 clusters.
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

#kmeans.labels_ retorna um array onde cada número representa o cluster ao qual o ponto pertence.
print(kmeans.labels_)

# Aqui verificamos a qual cluster pertencem os novos pontos (0,0) e (4,4) com predict().
kmeans.predict([[0,0],[4,4]])

#kmeans.cluster_centers_ retorna as coordenadas dos centros dos clusters.
# Isso significa que os centróides dos clusters são aproximadamente:

#[[3.25 2.5 ]
# [1.   1.  ]]
print(kmeans.cluster_centers_)