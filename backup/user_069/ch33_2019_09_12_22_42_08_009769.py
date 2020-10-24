100primeiros = [0]*100
while len(100primeiros) < 99:
	100primeiros[i + 1] = 100primeiros[i]*(1/2)
    s += i
print(s)    