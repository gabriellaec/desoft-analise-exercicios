lista_mes = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
num_mes = [1,2,3,4,5,6,7,8,9,10,11,12]

pergunta_mes = input('Digite o mes: ')

i = 0
while i < len(num_mes):
    lista_mes[i] = str(pergunta_mes)
    num_mes[i] = lista_mes[i]
    i += 1
    
print(num_mes[i])
