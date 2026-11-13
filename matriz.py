from dados.dados_graus import DADOS
import numpy as np

estados = set()

for artista in DADOS:
  for musica in DADOS[artista]:
    sequencia = DADOS[artista][musica]
    for grau in sequencia:
      estados.add(grau)

estados = sorted(estados)

indice = {}
for i, grau in enumerate(estados):
  indice[grau] = i

n = len(estados)
contagem = {}
for artista in DADOS:
  contagem[artista] = np.zeros((n, n))

print(contagem["john_mayer"].shape)

# print(estados)
# # print(len(estados))
# print(indice)
