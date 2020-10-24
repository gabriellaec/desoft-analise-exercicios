with open('churras.txt','r',encoding='utf8') as arquivo: 
    lista_linhas = arquivo.readlines()

listona = []
soma= 0 
for linha in lista_linhas:
    j = linha.replace(" ", "")
    k = j.replace(","," ")
    c = k.split()
    listona.append(c)

print(listona)
  
for listinha in listona:
    quantidade = int(listinha[1])
    preco = float(listinha[2])

    soma += quantidade*preco
print(soma)
        