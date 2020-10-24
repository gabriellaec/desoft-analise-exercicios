def esconde_senha(string):
    escondida=''
    contador=0
    for i in string:
        contador+=1
    escondida= contador*'*'
    return escondida