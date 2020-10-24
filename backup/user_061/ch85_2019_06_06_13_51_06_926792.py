with open("macacos-me-mordam.txt", "r", encoding="utf8") as file:
    conteudo = file.read()
contador = 0
conteudo  = conteudo.upper()
palavra = "BANANA"
for palavras in conteudo.split():
    if palavra == palavras:
        contador += 1
print(contador)