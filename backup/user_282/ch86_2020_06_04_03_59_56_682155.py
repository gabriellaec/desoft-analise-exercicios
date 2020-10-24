with open('dados.csv', 'r') as conteudo:
    x = conteudo.read()
    csv = x.split('\t')


with open('dados.tlv', 'w') as tlv:
    tlv.write(csv)