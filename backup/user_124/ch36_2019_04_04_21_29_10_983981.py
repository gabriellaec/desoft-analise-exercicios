def eh_primo(n):
    conta = 2
    n = conta + 1
    while conta < n:
        if n % 2 == 0:
            n % conta == 0 or n % conta == 2
            return False
        while n % 2 != 0:
            n % conta !=0
            conta += 1
            return True