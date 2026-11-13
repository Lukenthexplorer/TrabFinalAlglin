from dados.dados_graus import DADOS
import numpy as np

TESTE = {
    "john_mayer": [
        "john_mayer_room_for_squares_st_patricks_day",
        "john_mayer_heavier_things_come_back_to_bed",
        "john_mayer_continuum_gravity",
    ],
    "bring_me_the_horizon": [
        "bringmethehorizon_sleepwalking",
        "bringmethehorizon_throne",
        "bringmethehorizon_drown",
    ],
}

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
    if musica in TESTE[artista]:
      continue
    seq = DADOS[artista][musica]
    for k in range(len(seq) - 1):
      origem = seq[k]
      destino = seq[k + 1]
      contagem[artista][indice[destino], indice[origem]] += 1

# O BMTH tem 1.513 acordes em 20 músicas, e 1.513 − 20 = 1.493. Ou seja, cada música perde uma transição.
# print(contagem["bring_me_the_horizon"].sum())


print(contagem["john_mayer"].sum())
print(contagem["bring_me_the_horizon"].sum())
