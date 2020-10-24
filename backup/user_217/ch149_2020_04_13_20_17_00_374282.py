faixa_salarial=float(input('Qual é seu salario? :'))
n_dependente=float(input('Qual é o numero de dependentes?: '))

def inss(faixa_salarial,n_dependente):
    if faixa_salarial <= 1045:
        inss = 0.075*faixa_salarial
    if faixa_salarial > 1045 and faixa_salarial <= 2089.6:
        inss = 0.09*faixa_salarial
    if faixa_salarial > 2089.6 and faixa_salarial <= 3134.4:
        inss = 0.12*faixa_salarial
    if faixa_salarial > 3134.4 and faixa_salarial<= 6101.06:
        inss = 0.14*faixa_salarial
    if faixa_salarial > 6101.06:
        inss = 671.12
    return (faixa_salarial - inss - (n_dependente*189.59))

base_de_calculo = inss(faixa_salarial,n_dependente)

def irrf(base_de_calculo):
    if base_de_calculo <= 1903.98:
        aliquota  = 0
        n_dependente = 0
    if base_de_calculo > 1903.98 and base_de_calculo <= 2826.65:
        aliquota = 0.075
        n_dependente = 142.8
    if base_de_calculo > 2826.65 and base_de_calculo <= 3751.05:
        aliquota = 0.15
        n_dependente = 354.8
    if base_de_calculo > 3751.05 and base_de_calculo <= 4664.68:
        aliquota = 0.225
        n_dependente = 636.13
    if base_de_calculo > 4664.68:
        aliquota = 0.275
        n_dependente = 869.36
    
    return base_de_calculo*aliquota-n_dependente


