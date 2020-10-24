with open ('churras.txt','r') as arquivo:
    linhas = arquivo.readlines()
    lista = []
    for linha in linhas:
        valores = linha.split(',')
        lista.append(float(valores[1])*float(valores[2]))
print(sum(lista))
        