def conta_ocorrencia(palavra):
    with open(palavra, 'r') as arquivo:
        conteudo = arquivo.read()
        if 'banana' in palavra:
            return len(palavra)