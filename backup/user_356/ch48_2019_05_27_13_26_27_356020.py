lista_meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
mes=input('qual o mês?: ')
i=0
while i<len(lista_meses):
    if mes==lista_meses[i]:
        print(i+1)
        break
    if mes!=lista_meses[i]:
        i+=1