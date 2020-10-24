with open ("churras.txt", "r") as arquivo: 
    conteudo = arquivo.readlines()
    texto = conteudo
    quantidade = []
    preco = []
    for s in texto:
        s.replace("\n","")
		s.split(",")
    for m in texto:     
    quantidade.append(m[1])
    preco.append(m[2])
    soma = 0
    len_listas = len(quantidade)
    for e in range(1,len_listas):
        soma += int(quantidade[e-1]) * float(preco[e-1])
    print(soma)
        