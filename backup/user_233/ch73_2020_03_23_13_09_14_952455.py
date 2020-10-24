vogais = ['a', 'e', 'i', 'o', 'u']

def remove_vogais(string):
    
    sem_vogais = str()
    
    for c in string:
        if c in vogais: continue
        sem_vogais += c
   	
    return sem_vogais