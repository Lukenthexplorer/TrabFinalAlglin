from dados.dados_graus import DADOS

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


# print(estados)
# print(len(estados))
print(indice)