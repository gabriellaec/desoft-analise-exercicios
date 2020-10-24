def idade(n):
    if n < 18:
        return jovem
    if n >= 18 and n < 60:
        return adulto
    if n >= 60:
        return adulto
print(idade(n))