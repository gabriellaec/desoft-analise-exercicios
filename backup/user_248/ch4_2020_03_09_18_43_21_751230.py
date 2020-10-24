def classifica_idade(jaca):
    if int(jaca)<=11:
        idade=("criança")
    elif jaca>=12 and jaca<=17:
        idade=("adolescente")
    else:
        idade=("adulto")
    return idade
fx=classifica_idade(16)
print(fx)