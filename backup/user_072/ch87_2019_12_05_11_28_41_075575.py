#soma = 0
#Abrindo o arquivo e lendo as informações contidas nele
with open('churras.txt', encoding="utf8") as churras: 
    leitura = churras.readlines() #Leitura de cada linha
    soma = 0 #Valor dos custos

    for linha in leitura:
        itens = linha.split(",")
        quantidade = float(itens[1])
        preco = float(itens[2])
        valor = quantidade * preco
        soma += valor
        
    print(soma) #Exibindo valor total dos custos