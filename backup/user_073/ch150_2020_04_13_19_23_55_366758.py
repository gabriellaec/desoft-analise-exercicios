n=1
def calcula_pi(n):
    i=0
    s=0
    while i-1<n:
        s+=6/(i**2)
        i+=1
    π=s**0.5
    return π
