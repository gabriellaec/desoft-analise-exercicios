def eh_palindromo(palavra):
    resposta=False
    for e in palavra:
        if palavra == palavra[ : :-1]:
        	resposta=True
    return resposta
print(eh_palindromo('roma é amor'))
print(eh_palindromo('abcd'))