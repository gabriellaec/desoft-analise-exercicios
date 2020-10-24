a = int(input("ano"))

def eh_bissexto(n):
    if n % 4 == 0:
        return "True"
    else:
        return "False"

print(eh_bissexto(a))