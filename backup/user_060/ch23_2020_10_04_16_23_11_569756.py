velocidade = float(input("qual a velocidade?"))
if velocidade <= 80:
    return "não foi multado"
else:
    multa = (velocidade - 80)*5
    return multa
                         