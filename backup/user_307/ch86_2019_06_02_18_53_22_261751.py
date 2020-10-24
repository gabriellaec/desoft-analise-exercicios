with open('data.csv','r') as arquivo:
    cont = arquivo.read()
    nome = arquivo.name()
    str(nome)
    nome.replace('csv','tlv')
