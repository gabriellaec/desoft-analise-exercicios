def eh_palindromo(palavra):
    s=palavra[::-1]
    t=palavra
    if s==t:
        return True
    else:
        return False