def classifica_triangulo(ladoA, ladoB, ladoC):
    if ladoA==ladoB==ladoC:
        return 'equilátero'
     elif ladoA!=ladoB!=ladoC:
        return 'escaleno'
    else:
        return 'isóceles'
    
    