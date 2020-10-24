def calcula_fibonacci(n):
    if n==0:
        return []
    if n==1:
        return [1]
    if n>=2:
        while i<n:
            f=[1,1] 
            i=2
            while i<len(f):
                f.append(f[i-1]+f[i-2])
                i+=1
    return f    

