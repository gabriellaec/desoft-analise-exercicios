lista_mes = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
num_mes = [1,2,3,4,5,6,7,8,9,10,11,12]

pergunta_mes = input('Digite o mes: ')

a = str(pergunta_mes)
posicao = lista_mes.index(a)

print(num_mes[posicao])
