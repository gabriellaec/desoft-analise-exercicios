def calcula_tempo(atletas):
    
    tempo = {}
    
    for e in atletas:
        
        y = (200*atletas[e])**(1/2)
        
        tempo[e] = (y/atletas[e])
        
    return tempo