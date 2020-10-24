with open('palavras.txt','r') as pvs:
    data = pvs.read()

i=0
c=[]
a=["A","a"]
while i<len(data):
    if data[i] in a:
        c.append (data[i])
    i+=1
    
print (len(c))