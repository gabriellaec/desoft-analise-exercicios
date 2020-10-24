velo = float(input("Qual a velocidade do carro?"))

if velo > 80:
    km = velo-80
    multa = km*5
    retorno = round(multa, 2)
elif velo <= 80:
    retorno = 'Não foi multado'
    
print(retorno)
                   