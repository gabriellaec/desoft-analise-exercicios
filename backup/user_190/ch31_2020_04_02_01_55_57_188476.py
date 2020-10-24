n2=3
n1=int(input('qual o numero?: '))
if n%2==0:
    return False
while n2<=n1:
    if n1%n2==0:
        return False
    else:
        n2+=2
        return True