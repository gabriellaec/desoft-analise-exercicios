with open ("churras.txt", "r") as arquivo: 
    conteudo = arquivo.read()
  	texto = conteudo.strip("\n")
    lista = texto.split(",")
    quantidade = lista[1::3]
    preco = lista[2::3]
    soma = 0
    len_listas = len(quantidade)
    for e in range(1,len_listas):
        soma += int(quantidade[e-1]) * float(preco[e-1])
    print(soma)
        