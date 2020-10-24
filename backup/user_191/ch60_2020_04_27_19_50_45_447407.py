def eh_palindromo(n):
    for i in n:
        for u in n[::-1]:
            if i==u:
                return True
            else:
                return False