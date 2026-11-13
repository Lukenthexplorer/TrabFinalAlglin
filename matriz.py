from dados.dados_graus import DADOS
import numpy as np


# 1 - Montar os dados
estados = set()
for artista in DADOS:
  for musica in DADOS[artista]:
    sequencia = DADOS[artista][musica]
    for grau in sequencia:
      estados.add(grau)

estados = sorted(estados)


# 2 - Indice
indice = {}
for i, grau in enumerate(estados):
  indice[grau] = i

# 3 - Matrizes de zeros
n = len(estados)
contagem = {}
for artista in DADOS:
  contagem[artista] = np.zeros((n, n))

# 4 - Contar as transicoes
for artista in DADOS:
  for musica in DADOS[artista]:
    seq = DADOS[artista][musica]
    for k in range(len(seq) - 1):
      origem = seq[k]
      destino = seq[k + 1]
      contagem[artista][indice[destino], indice[origem]] += 1

print(contagem["bring_me_the_horizon"].sum())

