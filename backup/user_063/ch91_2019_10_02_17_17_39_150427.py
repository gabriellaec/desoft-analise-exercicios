arquivo = open('palavras.txt', 'r')
contador = 0
linha = arquivo.readlines()
j = 0
for i in linha:
    essalinha = i.split()
    while j < len(essalinha):
        if essalinha[j].startswith("a") == True or essalinha[j].startswith("A") == True:
            contador += 1
            j += 1
        else:
            j += 1
print (contador)