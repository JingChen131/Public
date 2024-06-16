num=eval(input())
n=int(num/2)+1
#计算行数
m=1
for i in range(n):
  print((' '*((num-m)//2))+('*'*m)+(' '*((num-m)//2)))
  #((num-m)//2)是‘*’前后的空格数
  m+=2