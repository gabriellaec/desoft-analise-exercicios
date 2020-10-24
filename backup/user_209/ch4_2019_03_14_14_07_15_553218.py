def classifica_idade (n):
    a = " "
    if n >= 0 and n<= 11:
        a = "crianca"
    elif n >=12 and n<=17:
        a = "adolescente"
    elif n >= 18 :
        a = "adulto"
    else:
        a = "nao existe idade negativa"
        return a