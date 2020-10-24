with open ('churras.txt','r') as arquivo:
    linhas = arquivo.readlines
    lista = []
    for linha in linhas:
        valores = linha.split(',')
        lista.append(valores[1]*valores[2])
print(sum(lista))
        