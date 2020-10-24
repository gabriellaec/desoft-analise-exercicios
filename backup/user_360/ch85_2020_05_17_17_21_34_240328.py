def conta_palavra(tst):
    with open(tst, 'r') as arq:
        cont = arq.read()
        words = cont.split()
        i = 0
        for x in words:
            if x.lower() == 'banana':
                i +=1
            if x.lower() == 'banana.':
                i+=1
            
        return i
print(conta_palavra('macacos-me-mordam.txt'))
