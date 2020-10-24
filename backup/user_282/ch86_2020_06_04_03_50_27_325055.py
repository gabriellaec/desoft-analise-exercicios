with open('dados.csv', 'r') as conteudo:
    csv = conteudo.read()

    with open('dados.tlv', 'w') as tlv:
        tlv.write(csv(sep='\t', index=False))