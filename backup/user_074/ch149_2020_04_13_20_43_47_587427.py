salbruto=input(('insira o salário bruto:'))
    dependentes=input(('insira o numero de dependentes:'))
def calcula_imposto_renda(salbruto, dependentes):
    if salbruto<1045.00:
        alicota=0.075
    if salbruto>=1045.00 and salbruto<2089.60:
        alicota=0.09
    if salbruto>=2089.60 and salbruto<3134.40:
        alicota=0.12
    if salbruto>=3134.40 and salbruto<6101.06:
        alicota=0.14
    else:
        alicota=671.12
    con_inss=salbruto*alicota
    print(con_inss)
    basecal = salbruto-con_inss-(dependentes*189.59)
    print(basecal)
    if basecal<1903.98:
        deducao=0
        alicota=0
    if basecal>=1903.98 and basecal< 2826.65:
        alicota=0.075
        deducao=142.80
    if basecal>=2826.65 and basecal<3751.05:
        alicota=0.15
        deducao=354.80
    if basecal>=3751.05 and basecal<4664.68:
        alicota=0.225
        deducao=636.13   
    else:
        alicota=0.275
        deducao=869,36
    imposto_renda = (basecal*alicota)-deducao 
    print(imposto_renda)
    return imposto_renda
