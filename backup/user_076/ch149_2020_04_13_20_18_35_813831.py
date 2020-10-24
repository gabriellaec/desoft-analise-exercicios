salário = float(input("Digite o valor do salário bruto: "))
dependentes = int(input("Digite o número de dependentes: "))

def IRRF (s,d):

    #Cálculo do INSS (n) com base no salário:

    if s<=1045.00:
        n = 0.075*s
    elif s<=2089.60:
        n = 0.09*s
    elif s<=3134.40:
        n = 0.12*s
    elif s<=6101.06:
        n = 0.14*s
    else:
        n = 671.12
    
    #Cálculo da base de cálculo:

    base = s - n - d*189.59
    
    #Cálculo da alíquota e dedução:
    
    if s<= 1903.98:
        alíquota = 0 
        dedução = 0
    elif s<= 2826.65:
        alíquota = 0.075 
        dedução = 142.80
    if s<= 3751.05:
        alíquota = 0.15
        dedução = 354.80
    if s<= 4664.68:
        alíquota = 0.225
        dedução = 636.13
    else:
        alíquota = 0.275
        dedução = 869.36
    
    #Cálculo do IRRF:

    imposto = base * alíquota - dedução

    return imposto

print (IRRF(salário,dependentes))