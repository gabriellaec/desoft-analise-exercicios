preço_do_produto = [256, 145, 12, 889, 10]
quantidade_de_produto = [3, 1, 5, 0, 9]

def calcula_total_da_nota(preco, quantidade):
    valores = [0]*len(preco)
    soma_valores = 0 
    i = 0
    while i < len(preco):
        valores[i] = preco[i]*quantidade[i]
        soma_valores += valores[i]
        i += 1
    return soma_valores

valor_total = calcula_total_da_nota(preço_do_produto, quantidade_de_produto)

print('O valor total da compra é de R$ {0:.2f}'.format(valor_total))