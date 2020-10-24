def conta_bigramas(q): 
    rep = {}
    for item in q: 
        if (item in rep): 
            rep[item] += 1
        else: 
            rep[item] = 1
    rep.items() 
    print (rep)
if __name__ == "__main__":  
    b='banana nanica'
    conta_bigramas(q) 