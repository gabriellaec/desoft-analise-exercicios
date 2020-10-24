# Cria uma lista com o nome todos os meses
lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
# Cria uma variável com a resposta do usuário
mes = int(input('Qual o mes:'))
# Determina uma variável com o índice que será acessado (subtrai 1 pois o python começa a contar a partir do 0 e os meses começam no 1)
i = mes - 1
# Verifica o elemento da lista 
mes = lista_meses[i]
print(mes)


