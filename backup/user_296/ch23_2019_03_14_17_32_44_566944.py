def verifica_idade(a):
    if a>= 21:
        return "liberado EUA e BRASIL"
    elif 18 <= a < 21:
        return "Liberado BRASIL"
    else:
        return "Não está liberado"
idade = int(input())
print(verifica_idade(idade))   