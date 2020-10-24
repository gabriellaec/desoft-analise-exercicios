def nomeMes(mes):
    i=0
    lista = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    while i < len(lista):
        if mes == lista[i]:
            resposta=i+1
        i+=1
    return resposta
mes=str(input('nome do mês: '))
print(nomeMes(mes))

     