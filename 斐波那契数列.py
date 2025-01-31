#每一项等于前两项之和
list=[]
n=eval(input("请输入要生成的项数："))
a,b=0,1
for i in range(n):
    list.append(a)
    a,b=b,a+b
print(list) 