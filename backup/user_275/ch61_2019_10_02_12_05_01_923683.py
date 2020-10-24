def eh_palindromo(palavra):
    inicio=palavra[0:len(palavra)]
    final=palavra[ : :-1]
    if inicio == final:
        return "eh palidromio"
    else:
        return "nao eh um palidormio"