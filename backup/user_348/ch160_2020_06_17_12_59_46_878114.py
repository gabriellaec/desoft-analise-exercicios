erro = 0
for x in range(0,91):
    funcao = 4 * x * (180-x)/(40500 - x * (180 - x))
    python = math.sin(math.radians(x))
    diferenca = abs(funcao - python)
    if diferenca > erro:
        print(x)
    
    