def agrupa_por_idade(dicionario):
criança = []
adolescente = []
adulto = []
idoso = []
dicionario1 = {"criança": criança, "adolescente": adolescente, "adulto": adulto, "idoso": idoso }
for i, x in dicionario.items():
    if x <= 11:
        criança.append (i)
    elif x > 11 and x < 18:
        adolescente.append(i)
    elif x > 17 and x < 60:
        adulto.append(i)
    else:
        idoso.append(i)
return dicionario1
        