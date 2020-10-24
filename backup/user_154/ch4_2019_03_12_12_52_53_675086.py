def classifica_idade(idade):
    if (idade < 1):
        return "Idade Invalida"
    if (idade < 12):
        return "criança"
    if (idade < 18):
        return "adolescente"
    return "adulto"