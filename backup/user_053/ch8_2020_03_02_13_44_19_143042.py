# Exercício 8 - Servidor
# Aplicando funções de MRU

def calcula_posição(tempo,espaço_inicial,velocidade):
    calcula_posição=espaço_inicial+(velocidade*tempo)
    return calcula_posição

a=10 # tempo decorrido
b=5 # espaço inicial
c=2 # velocidade 
d=calcula_posição(a,b,c)

print('A posição do móvel decorridos {0} s, espaço inicial {1} m e velocidade {2} m/s é {3} m'.format(a,b,c,d))