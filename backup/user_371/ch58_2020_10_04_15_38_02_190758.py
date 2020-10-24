def conta_a (palavra):
    numero_a=0
    i=0
    while len(palavra)>i:
        if palavra[i]=="a":
            numero_a+=1
            i+=1
        else:
            i+=1
    return numero_a  