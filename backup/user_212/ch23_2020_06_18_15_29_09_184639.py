velo = float(input("Qual a velocidade do carro?"))

if velo > 80:
    km = velo-80
    multa = km*5
    retorno = "{2:.f}".format(multa)
elif velo <= 80:
    retorno = 'Não foi multado'
    
print(retorno)
                   