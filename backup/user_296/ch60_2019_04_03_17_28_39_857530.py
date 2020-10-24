def asteriscos(a):
    i = 0
    for n in a:
        if n == "*":
            i+=1
    return i
n = str(input())
print(asteriscos(n))
        