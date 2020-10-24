contador = 0
passador = 0
def quantos_uns(numero):
    palavra =str(numero)
    while contador <= len(palavra):
        passador += 1
        if palavra[passador] == "1":
        	contador += 1
    return contador
        
    