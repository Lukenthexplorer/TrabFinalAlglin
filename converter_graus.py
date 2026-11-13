"""
Converte cifras (nomes de acordes) para graus simplificados.

Regras:
1. "..." é removido.
2. Baixo da barra é ignorado: "D/F#" -> D.
3. Extensões são ignoradas; só sobra a qualidade:
   maior (I), menor (i) ou diminuto (i°).
   - menor: sufixo começa com "m" (mas não "maj")
   - diminuto: "°", "dim" ou "m7b5"
   - todo o resto (7, maj7, 7M, sus, add9, 5, 6...) = maior
4. Grau relativo à tonalidade MAIOR de referência
   (música em lá menor usa dó maior como referência: Am = vi).
"""
import re, sys, runpy

GRAUS = ["I", "bII", "II", "bIII", "III", "IV", "#IV", "V", "bVI", "VI", "bVII", "VII"]
NOTAS = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}

def nota(txt):
    n = NOTAS[txt[0]]
    for c in txt[1:]:
        n += 1 if c == "#" else -1
    return n % 12

def qualidade(sufixo):
    if "°" in sufixo or "dim" in sufixo or "m7b5" in sufixo:
        return "dim"
    if sufixo.startswith("m") and not sufixo.startswith("maj"):
        return "min"
    return "maj"

def para_grau(acorde, tom):
    acorde = acorde.replace("*", "").split("/")[0]
    m = re.match(r"([A-G][#b]?)(.*)", acorde)
    raiz, suf = m.group(1), m.group(2)
    g = GRAUS[(nota(raiz) - nota(tom)) % 12]
    q = qualidade(suf)
    if q == "min":
        return g.lower()
    if q == "dim":
        return g.lower() + "°"
    return g

if __name__ == "__main__":
    entrada, tons_arq, saida = sys.argv[1], sys.argv[2], sys.argv[3]
    musicas = {k: v for k, v in runpy.run_path(entrada).items() if isinstance(v, list)}
    tons = runpy.run_path(tons_arq)["TONALIDADES"]
    with open(saida, "w") as f:
        f.write("# Gerado por converter_graus.py a partir de " + entrada + "\n\n")
        for nome, seq in musicas.items():
            graus = [para_grau(a, tons[nome]) for a in seq if a != "..."]
            f.write(f"# tom de referência: {tons[nome]} maior\n{nome} = {graus!r}\n\n")
