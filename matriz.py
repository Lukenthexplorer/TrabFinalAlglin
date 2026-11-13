import matplotlib.pyplot as plt
import numpy as np
from dados.dados_graus import DADOS

# 1 - Montar os estados com todos os dados
estados = set()
for artista in DADOS:
  for musica in DADOS[artista]:
    for grau in DADOS[artista][musica]:
      estados.add(grau)

estados = sorted(estados)

# 2 - Índice
indice = {grau: i for i, grau in enumerate(estados)}

# 3 - Matrizes de zeros
n = len(estados)
contagem = {artista: np.zeros((n, n)) for artista in DADOS}

# 4 - Contar as transições com todos os dados
for artista in DADOS:
  for musica in DADOS[artista]:
    seq = DADOS[artista][musica]
    for k in range(len(seq) - 1):
      origem = seq[k]
      destino = seq[k + 1]
      contagem[artista][indice[destino], indice[origem]] += 1

# 5 - Suavização de Laplace e distribuição estacionária para CADA artista
distribuicoes = {}

for artista in DADOS:
  suavizada = contagem[artista] + 1
  P = suavizada / suavizada.sum(axis=0, keepdims=True)

  autovalores, autovetores = np.linalg.eig(P)
  posicao = np.argmin(np.abs(autovalores - 1))
  v = np.abs(np.real(autovetores[:, posicao]))
  distribuicoes[artista] = v / v.sum()

# 6 - Plotagem
posicoes = np.arange(len(estados))
largura = 0.4

plt.figure(figsize=(12, 5))
plt.bar(
    posicoes - largura / 2,
    distribuicoes["john_mayer"],
    largura,
    label="John Mayer",
)
plt.bar(
    posicoes + largura / 2,
    distribuicoes["bring_me_the_horizon"],
    largura,
    label="BMTH",
)

plt.xticks(posicoes, estados, rotation=45)
plt.xlabel("Grau do acorde")
plt.ylabel("Probabilidade estacionária")
plt.title("Distribuições estacionárias")
plt.legend()
plt.tight_layout()
plt.savefig("figuras/distribuicoes_estacionarias.png", dpi=300)
plt.close()
plt.show()