#Temperature conversion.py
TempStr = input("请输入带有温度符号的温度值：")
if TempStr[-1] in ['F','f']:
    #缩进是Python语法要求
    C = (eval(TempStr[0:-1]) -32)/1.8 #右侧运算结果赋给变量C
    print("转换后的温度是{:.3f}c".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.3f}F".format(F))
else:
    print("输入格式错误")
#单行注释
'''多行注释'''