def sushu(n):
    for i in range(2,n):
        if n % i == 0:
            return 0        #非素数返回零，不影响累加
            break
    else:    #为了防止break跳过else段，else与for对齐
        return n            #素数返回它本身，计入累加
 
sum = 2
 
for i in range(3,100):
    a = sushu(i)
    sum += a
 
print(sum)