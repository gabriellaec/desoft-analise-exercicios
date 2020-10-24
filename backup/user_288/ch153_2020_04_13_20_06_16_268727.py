def agrupa_por_idade (lista):
    idades = {}

    for e in lista: 
        nome = input('Quais são os nomes?')
    
    for e in lista.values():
        idade = input('Quais as idades?')
        
    if idade <= 11:
        crianca = idade[e]
    elif idade >= 12 and idade <= 17:
        adolescente = idade[e]
    elif idade >= 18 and idade <= 59:
        adulto = idade[e]
    else:
        idoso = idade [e]
    return idades
    
