i=0
with open ('macacos-me-mordam.txt') as arq:
    texto=arq.readlines()
    for row in texto:
        if row[0]=='B' or row[0]=='b':
            if row[1]=='a' or row[1]=='A':
                if row[2]=='n' or row[2]=='N':
                    if row[3]=='A' or row[3]=='a':
                        if row[4]=='n' or row[4]=='N':
                            if row[5]=='A' or row[5]=='a':
                                i+=1
                                
print(i)
            