with open ("churras.txt", "r") as arquivo: 
    conteudo = arquivo.read()
    string = conteudo.strip()
    lista = string.split(",")
    quantidade = int(lista[1::3])
    preco = float(lista[2::3])
    soma = 0
    for n in len(quantidade):
        soma += quantidade[n-1] * preco[n-1]
    print(soma)
        