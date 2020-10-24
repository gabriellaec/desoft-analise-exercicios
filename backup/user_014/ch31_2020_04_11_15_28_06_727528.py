def eh_primo(n):
    n = int(input('Digite um número: ')
    numero_primo = True
    while numero_primo:
        if n != 2 and n % 2 == 0:
            numero_primo = False
            return False
