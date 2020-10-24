l=[]
nums=int(input('Digite um número: '))
while nums>0:
    nums=int(input('Digite um número: '))
    l.append(nums)
if nums<=0:
    print(l[::-1])