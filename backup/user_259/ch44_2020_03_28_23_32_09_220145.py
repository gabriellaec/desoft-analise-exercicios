nome_mes = input("Qual o nome do mês? ")
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
i = 0
while i<len(meses):
    if nome_mes == meses[i]:
        print(meses[i])
        break
    else:
        i+=1
    
      