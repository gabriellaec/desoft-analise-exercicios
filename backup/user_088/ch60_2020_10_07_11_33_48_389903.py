def eh_palidromo(numero):
i = 0
f = len(numero)-1  # posição do último caracter da string
while f > i and numero[i] == numero[f]:
    f = f - 1
    i = i + 1
if numero[i] == numero[f]:
    print(numero, "é palíndromo")
else:
    print(numero, "não é palíndromo")
