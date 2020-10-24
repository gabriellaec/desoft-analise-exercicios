def soma_valores(numeros):
   if len(numeros) == 1:
        return numeros[0]
   else:
        return numeros[0] + soma_valores(numeros[1:])