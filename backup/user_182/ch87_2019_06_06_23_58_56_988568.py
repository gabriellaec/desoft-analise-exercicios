with open("churras.txt", "r", encoding="utf8") as arquivo:
    conteudo = arquivo.read()

linhas=str.splitlines(conteudo)
linhaf=[]
lista=[]
valoresdecadalinha=[]
i=0
s=0
conteudodoarquivo = ""
for o in range(len(linhas)):
    linha = linhas[o]
    linhaf=linha.split(",")
    lista.append(linhaf)
for a in range(len(lista)):
    u=lista[a]
    am=float(u[1])
    av=float(u[2])
    s+=am*av 
print(s)