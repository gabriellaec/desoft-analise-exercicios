def verifica_palindromo(palavra):
    a=False
    s=palavra[::-1]
    if s == palavra:
        a=True
    return a 
