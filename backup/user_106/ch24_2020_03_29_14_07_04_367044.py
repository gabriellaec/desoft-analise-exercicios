salário = float(input("Digite seu salário:"))
pc_aumento = 0.15
if salário > 1250:
    pc_aumento = 0.10
aumento = salário * pc_aumento
print("Seu aumento será de: R$ {0:.2f}".format())


def calcula_aumento(s):
    if s>1250.00:
        x=s*1.10
        return x
    else:
        x=s*1.15
        return x