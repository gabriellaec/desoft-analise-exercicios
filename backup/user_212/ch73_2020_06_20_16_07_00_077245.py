def remove_vogais (string):
    nova = []
    vogais = ['a', 'e', 'i', 'o', 'u']
    
    for l in string:
        if l not in vogais: 
            nova.append(l)
            
    string_final = ''.join(nova)
    
    return string_final