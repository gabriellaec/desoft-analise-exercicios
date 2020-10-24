def classifica_idade(anos):  
    x = anos
    if x<12:
        return "crianca"
    if 11<x<18:
        return "adolescente"
    if x>17:
        return "adulto"
 