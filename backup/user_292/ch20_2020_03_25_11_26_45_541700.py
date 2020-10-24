d=int(input('qual a distacia deseja percorrer?'))
if d<200:
    p=d*0.5
elif d>200:
    p=200*5+(d-200)*0.45
print(p)