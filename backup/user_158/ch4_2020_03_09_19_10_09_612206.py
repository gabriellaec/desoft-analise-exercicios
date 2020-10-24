def classifica_idade:
    if Idade <= 11:
       Idade = "crianca" 
    elif Idade <= 17 or Idade >= 12:
       Idade = "adolescente"
    else Idade <= 18:
        Idade = "adulto"
    return Idade
print(Idade)