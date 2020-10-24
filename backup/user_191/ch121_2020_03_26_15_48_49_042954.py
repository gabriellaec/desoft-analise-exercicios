a=[1,2,3,4,5]
b=[1,2,8,9,0] 
i=0
o=0
while o<len(b):
    while i<len(a):
        if a[i]==b[o]:
            del a[i]
            i+=1
        else:
            i+=1
    i=0
    o=o+1
print(a)