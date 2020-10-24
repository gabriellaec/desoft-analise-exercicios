with open ("churras.txt","r") as arquivo:
    conteudo = arquivo.readlines()
    i = 0
    s = 0
    while i< len(lista):
        lista = conteudo.split(",")
        s += float(lista[i][2]) * lista[i][1]
        i +=1
print (s)