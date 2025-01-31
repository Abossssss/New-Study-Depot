a=eval(input('请输入边长(cm)'))
b=eval(input('请输入边长(cm)'))
c=eval(input('请输入边长(cm)'))

if a+b>c and a+c>b and b+c>a :
    print('可以组成三角形')
    if  a==b or b==c or a==c:
        if a==b==c:
            print('可以组成等边三角形')
        else :
            print('可以组成等腰三角形')
    else:
        print('可以组成普通三角形')
else:
     print('不能组成三角形')