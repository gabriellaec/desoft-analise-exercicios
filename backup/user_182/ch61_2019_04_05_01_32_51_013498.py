string = input('fala ai: ')
def eh_palindromo(string):
    return (string==string[ : :-1])
print(eh_palindromo(string))