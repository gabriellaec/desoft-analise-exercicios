def separa_trios(s):
    z=[]
    y=[]
    l=[]
    for i in range(len(s)):
        z.append(s[0:3])
        y.append(s[3:6])
        l.append(s[6:len(s)])
        return[z,y,l]

s = ['enrico','murilo','lucca','thiago','gustavo','silvana','victor']
print(separa_trios(s))
    
