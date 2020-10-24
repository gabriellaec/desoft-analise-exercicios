print("Vamos calcular o seu imposto de renda que sera retido na fonte...")
sb = int(input("Coloque aqui o seu salario bruto... "))
ndp = int(input("Coloque aqui o seu numero de dependentes... "))
if sb < 1045:
    al = 0.075
    cinss = sb * al
elif sb > 1045 and sb <= 2089.60:
    al = 0.09
    cinss = sb * al
elif sb > 2089.60 and sb <= 3134.40:
    al = 0.12
    cinss = sb * al
elif sb > 3134.40 and sb <= 6101.06:
    al = 0.14
    cinss = sb - al
else:
    al = 671.12
    cinss = sb - 671.12
# calculando a base de calculo...
bc = sb - cinss - (ndp *189.59)
# calculando a aliquota...
if bc <= 1903.98:
    al = 0
    dd = 0
elif bc > 1903.98 and bc <= 2826.65:
    dd = 142.8
    al = 0.075
elif bc > 2826.65 and bc <= 3751.05:
    dd = 358.8
    al = 0.15
elif bc > 3751.05 and bc <= 4664.68:
    dd = 636.13
    al = 0.225
else:
    dd = 869.36
    al = 0.275
# calcular o irff:
irff = (bc * al) - dd

