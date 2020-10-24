def palindromo(palavra):
    palavra=str(input("Digite a palavra: "))
    if palavra[ : :-1]==palavra[ : :1]:
        return True
    return False