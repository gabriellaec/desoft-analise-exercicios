def primeiras_ocorrencias(palavra):
    return {letra:palavra.index(letra) for letra in palavra}