# Verificando onde cada pessoa pode comprar bebida alcóolica

def verifica_idade(idade):
    if idade >= 21:
        return 'Liberade EUA e BRASIL'
    else:
        if idade >= 18:
            return 'Liberado BRASIL'
        else:
            return 'Não está liberado'

print(verifica_idade(12))
print(verifica_idade(19))
print(verifica_idade(25))