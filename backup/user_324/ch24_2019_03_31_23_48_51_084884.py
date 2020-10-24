def classifica_triangulo(ladoA, ladoB, ladoC):
    if ladoA==ladoB==ladoC:
        return 'equilátero'
    elif ladoA!=ladoB!=ladoC and ladoA+ladoB>ladoC or ladoA+ladoC>ladoB or ladoC+ladoC>ladoA:
        return 'escaleno'
    else:
        return 'isóceles'
    
    