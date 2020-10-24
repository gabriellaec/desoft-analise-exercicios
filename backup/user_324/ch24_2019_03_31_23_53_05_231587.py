def classifica_triangulo(ladoA, ladoB, ladoC):
    if ladoA+ladoB>ladoC or ladoA+ladoC>ladoB or ladoB+ladoC>ladoA:
    	if ladoA==ladoB==ladoC:
        	return 'equilátero'
    	elif ladoA!=ladoB!=ladoC:
        	return 'escaleno'
    	elif ladoA!=ladoB==ladoC or ladoA==ladoB!=ladoC or ladoA==ladoC!=ladoB:
        	return 'isóceles'

    