def classifica_idade(p):
        if p <= 11:
            resposta='crianca'
        elif p >= 18:
            resposta='adulto'
        else:
            resposta='adolescente'
        return resposta
print(classifica_idade(25))