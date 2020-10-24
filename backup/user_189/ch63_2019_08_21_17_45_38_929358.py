
def encontraarroba(str):
    for p in range(len(str)):
        if str[p]=="@":
            print(p)
    
str="abcde@jmghjut"
print(encontraarroba(str))  