def classifica_triangulo(ladoA, ladoB, ladoC):
    if ladoA+ladoB>ladoC and ladoA+ladoC>ladoB and ladoB+ladoC>ladoA:
    	if ladoA==ladoB==ladoC:
        	return 'equilátero'
    	elif ladoA!=ladoB!=ladoC:
        	return 'escaleno'
    	elif ladoA!=ladoB==ladoC or ladoA==ladoB!=ladoC or ladoA==ladoC!=ladoB:
        	return 'isóceles'

    