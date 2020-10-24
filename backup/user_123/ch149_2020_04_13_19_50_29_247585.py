def calculobase(salbruto):
    salbruto = float(input('Qual seu salário bruto?')
    dep = float(input("Quantos dependentes tem?"))
    if salbruto <= 1045 :
        base_de_calculo = salbruto - (salbruto*0.07) - (dep*189.59)
    elif 1045 < salbruto <= 2089.60 :
        base_de_calculo = salbruto - (salbruto*0.09) - (dep*189.59)
    elif 2089.61 < salbruto <= 3134.40 :
        base_de_calculo = salbruto - (salbruto*0.12) - (dep*189.59)
    elif 3134.40 < salbruto <= 6101.06:
        base_de_calculo = salbruto - (salbruto*0.14) - (dep*189.59)

def irff(base_de_calculo):
    if base_de_calculo <= 1903.98:
        irrf = 0
    elif 1903.98 < base_de_calculo <= 2826.65:
        irrf = (base_de_calculo*0.075)-142
    elif 2826.65 < base_de_calculo <= 3751.05:
        irrf = (base_de_calculo*0.15)-354.80
    elif 3751.05 < base_de_calculo <= 4664.68:
        irrf = (base_de_calculo*0.225)-636.13
    else:
        irrf = (base_de_calculo*0.275)-869.36
print (irrf)