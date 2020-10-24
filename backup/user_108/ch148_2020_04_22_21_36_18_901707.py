def conta_letras(palavra):
    return {letra:palavra.count(letra) for letra in palavra}