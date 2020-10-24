nome_mes = input("Qual o nome do mês? ")
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
i = 0
while i<len(meses):
    if nome_mes == meses[i]:
        print(meses[i])
    else:
        break
    
      