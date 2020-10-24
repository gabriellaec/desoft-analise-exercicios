with open('palavras.txt','r') as plvs:
    data = plvs.read()

i=0
c=[]
a=["A","a"]
es=[" ","", ","]
if data[0] in a:
    c.append(data[0])
while i<len(data):
    if data[i] in a and data[i-1] in es:
        c.append (data[i])
    i+=1
    
print (len(c))