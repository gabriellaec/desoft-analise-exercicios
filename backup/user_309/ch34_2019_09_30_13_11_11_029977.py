deposito = float(input('Digite o deposito inicial: '))
taxa_juros = float(input('Digite a taxa de juros: '))
mes = 1
ganho = 0
while mes <= 24:
    ganho = ganho + (deposito * (taxa_juros/100))
    print("Ganho do mes {0} foi {1:.2f}".format(mes,ganho))
    mes += 1
print("Ganho final foi: {0:.2f}".format(deposito - ganho))
