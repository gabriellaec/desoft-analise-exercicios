def agrupa_por_idade (x):
    Criança=[]
    Adolescente=[]
    Adulto=[]
    Idoso=[]
    x1={"Criança":Criança,"Adolescente":Adolescente, "Adulto": Adulto, "Idoso": Idoso}
    for y in x:
        a=x[b]
        if a <=11:
            c="Criança"
            Criança.append(b)
            x1[c]=Criança
        elif a>11 and a<=17:
            c="Adolescente"
            Adolescente.append(b)
            x1[c]=Adolescente
        elif a>17 and a<=59:
            c="Adulto"
            Adulto.append(b)
            x1[c]=Adulto
        else:
            c="Idoso"
            Idoso.append(b)
            x1[c]=Idoso
        return x1
i={"João":10,"Maria":8, "Miguel":20, "Helena":67, "Alice":50}
print(agrupa_por_idade(i))