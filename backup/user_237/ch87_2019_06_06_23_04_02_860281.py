with open ("churras.txt", "r") as arquivo: 
    conteudo = arquivo.readlines()
    quantidade = conteudo[1::3]
    preco = conteudo[2::3]
    soma = 0
    len_listas = len(quantidade)
    for e in range(1,len_listas):
        soma += int(quantidade[e-1]) * float(preco[e-1][:5])
    print(soma)
        