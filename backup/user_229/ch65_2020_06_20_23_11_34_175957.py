def capitaliza(string):
    nova_palavra = string
    maiuscula = string.upper()
    resposta = nova_palavra.replace('{}'.format(string[0]), '{}'.format(maiuscula[0]))
     
    return resposta