distancia = int(input("distancia desejada: "))
if distancia <= 200:
    x = distancia * 50
    s = str(x)
    s = s[:-2] + "." + s[-2:]
    print(s)
if distancia > 200:
    x = 200 * 50 + (distancia - 200) * 45
    s = str(x)
    s = s[:-2] + "." + s[-2:]
    print(s)