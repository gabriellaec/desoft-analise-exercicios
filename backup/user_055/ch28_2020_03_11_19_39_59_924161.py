potencia = int(0)
expressao = float(1/(2**potencia)) 
while expressao > 1/(2**99):
    potencia += 1
    expressao = expressao*100