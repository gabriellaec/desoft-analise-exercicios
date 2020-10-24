# Exercício 8 - Servidor
# Aplicando funções de MRU

def calcula_posicao(tempo,espaço_inicial,velocidade):
    calcula_posicao=espaço_inicial+(velocidade*tempo)
    return calcula_posicao

a=10 # tempo decorrido
b=5 # espaço inicial
c=2 # velocidade 
d=calcula_posicao(a,b,c)

print('A posição do móvel decorridos {0} s, espaço inicial {1} m e velocidade {2} m/s é {3} m'.format(a,b,c,d))