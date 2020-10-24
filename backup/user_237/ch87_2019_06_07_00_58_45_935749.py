a = []
with open ("churras.txt", "r") as arquivo: 
    conteudo = arquivo.read()
    lista = conteudo.split() and conteudo.split('\n')
    gasto = 0
    for n in lista: 
        a.append(n.split(','))
    for item in a:
        gasto += int(item[1])*float(item[2])
print(gasto)
        