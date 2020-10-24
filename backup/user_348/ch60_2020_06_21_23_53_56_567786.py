def eh_palindromo (string):
        # Verifica se a string é igual a ela ao contrário
        if string == string[::-1]:
            return True
        else:
            return False