a = int (input('Distância em km: '))
if a <= 200:
    def um(a):
        resultado = 0.5 * a
        return resultado
else: 
    def dois(a):
        resultado = 200*0.5 + (a-200)*0.45
        return resultado

print ('{0:.2f}' .format(resultado))
      