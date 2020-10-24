def classifica_idade(a):
    if a <= 11:
        recebe = "crianca" 
    if a>=12 and a<= 17:
        recebe = "adolescente"
    if a >= 18:
        recebe = "adulto"
    return recebe

    