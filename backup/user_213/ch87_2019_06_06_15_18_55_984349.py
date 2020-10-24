valores={'valor': 0}
with open('churras.txt','r') as arquivo:
    conteudo = arquivo.read()
    itens = arquivo.readlines()
    for item in itens:
        nome,quantidade,valor = item.split(',')
        valor = float(valor)
        valores['valor'] += valor
    print (valores['valor'])
    