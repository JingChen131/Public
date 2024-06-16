x=str(input())
x=set(x)#先变成集合去重
sum=0
for i in x:
    i=int(i)
    sum+=i
print(sum)