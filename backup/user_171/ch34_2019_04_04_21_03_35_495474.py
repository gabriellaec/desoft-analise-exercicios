depositoinicial=float(input('deposito inicial: '))
taxadejuros=float(input('taxa de juros: '))
mes=1
valor=depositoinicial
while mes<=12:
    deposito=depositoinicial
    ganho=valor*(taxadejuros/100)
    valor+=deposito+ganho
    print('o valor do mes {0} é R${1}'.format(mes, valor))
    mes+=1
print('o total ganho com juros é  R${0}'.format(ganho))