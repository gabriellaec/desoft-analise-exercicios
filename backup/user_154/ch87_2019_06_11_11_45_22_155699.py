with open("churras.txt", "r") as file:
    custo = 0
    
    for linha in file.readlines():
        splt = line.split(",")
        custo = custo + (int(splt[1])*float(splt(2))
    
    print(custo)