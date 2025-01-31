
import random

a=random.randint(0,101)
flag = True

while flag:
    try:
        b=eval(input('请输入你猜想得到的数字:'))
    except SyntaxError:
        print('您没有输入任何数字')
        continue
    except NameError:
        print('请不要输入数字以外的内容')
        continue
    if b != a:
        if b>a:
             print('你的猜测偏大')
        else :
            print('你的猜测偏小')
    else :
        print ('你真牛逼，猜对了！')
        flag = False

       