i=0
while i<len(lista):
    lista[i] = input("Digite uma palavra:")
    palavra = lista[i]
    primeira_letra = palavra[1]
    if primeira_letra == "a" or primeira_letra == "A":
        palavras_com_a_no_cmc.append(lista[i])
    i=i+1
print(palavras_com_a_no_cmc)
