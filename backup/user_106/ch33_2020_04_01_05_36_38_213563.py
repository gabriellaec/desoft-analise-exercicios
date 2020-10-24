def primos_entre(a,b):
    lista=[]
    def lista_primos():
        i=0
        o=0
        def eh_primo(x):
            if x==0:
                return False
            elif x==1:
                return False
            elif x==2:
                return True
            elif x%2==0:
                return False
            else:
                i=3
                while i<x:
                    if x%i==0:
                        return False
                    i+=2
                return True
        while True:
            while o>=a and o<=b:
                if eh_primo(o):
                    lista.append(o)
                    o+=1
                o+=1
            o+=1
            if o>b:
                break
        return lista
    return len(lista)
print(primos_entre(7,15))