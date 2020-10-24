#Abrindo o arquivo e lendo as informações contidas nele
with open('churras.txt', encoding="utf8") as churras: 
    leitura = churras.readlines()
	soma = 0
    for linha in leitura:
        itens = linha.split(",")
        quantidade = float(itens[1])
        preco = float(itens[2])
        valor = quantidade * preco
        soma += valor