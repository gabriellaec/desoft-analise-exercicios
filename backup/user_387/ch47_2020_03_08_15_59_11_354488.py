b = []
pos = 0



def estritamente_crescente(a):

    pos = 0

    for num in reversed(a):

        b.insert(0 , num)
        pos = a.index(num) - 1

        while pos > 0:



            if num <= a[pos]:
                b.remove(num)
                pos = pos - 1

                

            else:
                
                pos = pos - 1
    

    c = list(dict.fromkeys(b))
    return(c)