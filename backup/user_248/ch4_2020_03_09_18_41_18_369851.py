def classifica_idade(jaca):
    if jaca<=11:
        idade=("criança")
    elif jaca>=12 and jaca<=17:
        idade="adolescente"
    else:
        idade="adulto"
    return idade
fx=classifica_idade(11)
print(fx)