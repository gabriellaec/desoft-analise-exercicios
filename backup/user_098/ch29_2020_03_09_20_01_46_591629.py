inicial = float(input('Valor Inicial: '))
taxa_juros = float(input('Taxa: '))

i=0
total=0
mes=inicial

while i < 24:
    mes=mes*((taxa_juros/100)+1)
    total=total+mes
    i=i+1
    print(mes)
else:
    print(total)