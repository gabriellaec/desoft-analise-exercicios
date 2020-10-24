def remove_vogais(word):
    palavra=" " 
    for e in range (len(word)):
        if word [e]!="a" and  word [e]!="e" and  word [e]!="i" and  word [e]!="o" and  word [e]!="u":
            palavra=word[e]
        return palavra
    
