depositoinicial=float(input('deposito inicial: '))
taxadejuros=float(input('taxa de juros: '))
mes=1
ganho=0
ganhototal=0

valor=depositoinicial
while mes<=12:
    ganho=valor*(taxadejuros/100)
    valor+=+ganho
    print('o valor do mes {0} é R${1:.2f}'.format(mes, valor))
    mes+=1
    ganhototal+=ganho
print('o total ganho com juros é  R${0:.2f}'.format(ganhototal))
