valores={'valor': 0}
with open('churras.txt','r') as arquivo:
    itens = arquivo.readlines()
    for item in itens:
        nome,quantidade,valor = item.split(',')
        valor = float(valor)
        valores['valor'] += valor
    