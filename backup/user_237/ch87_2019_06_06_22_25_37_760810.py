with open ("churras.txt", "r") as arquivo: 
    conteudo = arquivo.read()
    string = conteudo.strip()
    lista = string.split(",")
    quantidade = lista[1::3]    
    preco = lista[2::3]
    soma = 0
    for n,m in quantidade,preco:
        soma += int(quantidade[n]) * float(preco[m])
    print(soma)
        