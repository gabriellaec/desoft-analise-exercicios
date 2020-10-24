with open ("churras.txt", "r") as arquivo: 
    conteudo = arquivo.read()
    string = conteudo.strip()
    lista = string.split(",")
    quantidade = lista[1::3]    
    preco = lista[2::3]
    soma = 0
    len_listas = len(quantidade)
    for q,p in quantidade,preco:
        soma += int(q) * float(p)
    print(soma)
        