salario=float(input("Informe seu salário:"))
dependente=int(input("quantos dependem de você?"))
def inss(salario,dependente):
    if salario<=1045:
        contri=salario*7.5/100
        return contri
    else:
        if 1045.01<=salario<=2089.60:
            contri=salario*9/100
            return contri
        else:
            if 2089.01<=salario<=3134.40:
                contri=salario*12/100
                return contri
            else:
                if 3134.41<=salario<=6101.06:
                    contri=salario*14/100
                    return contri
                else:
                    contri=671.12
                    return contri
def base_calculo:
    base_de_calculo=salario-contri-(dependente*189.59)
    if base_de_calculo<=1903.98:
        ali=0
        dedu=0
    else:
        if 1903.99<=base_de_calculo<=2826.65:
            ali=7.5/100
            dedu=142.80
        else:
            if 2826.66<=base_de_calculo<=3751.05:
                ali=15/100
                dedu=354.80
            else:
                if 3751.06<=base_de_calculo<=4664.68:
                    ali=22.5/100
                    dedu=636.13
                else:
                    ali=27.5/100
                    dedu=869.36

    
def irrf_:
    irrf=base_de_calculo*ali-dedu
    
        
        