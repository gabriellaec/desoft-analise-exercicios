nome=input('Qual o nome do mês? ')
meses=[Janeiro, Fevereiro, Março, Abril, Maio, Junho, Julho, Agosto, Setembro, Outubro, Novembro, Dezembro]
i=0
while i<len(meses):
    if meses[i]==nome:
        ind=i
    i+=1
print (ind+1)