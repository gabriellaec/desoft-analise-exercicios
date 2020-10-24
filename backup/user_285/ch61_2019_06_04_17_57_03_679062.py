def eh_palindromo(palavra):
    for i in range(len(palavra)):
        if palavra[ : :-1] == palavra[ : :1]:
            return True
    return False