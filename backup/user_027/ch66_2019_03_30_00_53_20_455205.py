def capitaliza(x):
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if x[0] not in ALFABETO:
   	    comeco = ALFABETO[alfabeto.find(x[0])]
        final = x[1:]
    return final