def dayUP(df):
    dayup=1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup=dayup*(1-0.01)
        else:
            dayup =dayup * (1+df)
    return dayup
dayfactor =0.01
while dayUP(dayfactor)<37.78:
    dayfactor += 0.001
print("工作日的努力参数是:{:.3f}".format(dayfactor))
#十进制：一般表示
#二进制：0b 或 0B 开头
#八进制：0o 或 0O 开头
#十六进制：0x 或 0X 开头