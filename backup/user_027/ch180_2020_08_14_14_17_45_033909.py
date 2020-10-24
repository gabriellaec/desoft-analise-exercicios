def ocorrencias_letras(string:str) -> dict:
    return {letra:list(string).count(letra) for letra in set(string) }