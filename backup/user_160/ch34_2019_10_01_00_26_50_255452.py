depositoinicial = float(input("Qual o deposito inicial?"))
taxadejuros = float(input("Qual a tx de juros?"))
i = 1
while i <= 24:
    valmes = depositoinicial*(1+taxadejuros)**i
    print(valmes)
    i+=1
print(valmes-depositoinicial)
    