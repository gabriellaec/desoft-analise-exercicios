with open('churras.txt','r',encoding='utf8') as arquivo: 
    lista_linhas = arquivo.readlines()

soma= 0
for linha in lista_linhas:
    j = linha.replace(" ", "")
    k = j.replace(","," ")
    c = k.split()
    print(c)
    for elemento in c:
        quantidade = float(c[1])
        preco = float(c[2])
        total = quantidade * preco
        soma = soma + total
print(soma)