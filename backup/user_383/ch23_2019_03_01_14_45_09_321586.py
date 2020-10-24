def verifica_idade(idade):
    if idade>=21:
        return('Você é liberado no Brasil e nos EUA para comprar bebida alcóolica')
    elif idade>=18 and idade<21:
        return('Você é liberado apenas no Brasil para comprar bebida alcóolica')
    else:
        return('Você não está liberado para para comprar bebida em nenhum local')
