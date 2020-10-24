
def apaga_repetidos(string):
    
    resultado = str()
    ocorrencias = set()
    
    for letra in string:
        
        if letra not in ocorrencias:
            ocorrencias.add(letra)
            resultado += letra
            continue
        
        resultado += '*'
    
    return resultado
                
