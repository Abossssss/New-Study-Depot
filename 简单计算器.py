flag=True

while flag:
    try :       
        a=eval (input('请输入第一组数字：'))
    except SyntaxError:
        print('您没有输入任何数字')
        continue
    except NameError:
        print('请不要输入数字以外的内容')
        continue    
    b=input ('请输入运算符号：')
    if b not in ["+","-","*","/"]:
        print("请输入正确的运算符号！")
        continue
    try:    
        c=eval (input('请输入第二组数字：'))
    except SyntaxError:
        print('您没有输入任何数字')
        continue
    except NameError:
        print('请不要输入数字以外的内容')
        continue    
    if b=='+':
        print(a+c)
    
    if b=='-':
        print(a-c)
    if b=='*':
        print(a*c)
    if b=='/':
        print(a/c)
    flag=False