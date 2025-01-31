a = eval(input('请输入您的身高(m)):'))
b = eval(input('请输入您的体重(kg):'))
BMI = a + b**2
if BMI<=18.4:
    print('您的体质偏瘦')
elif BMI<=23.9:
    print('您的体质正常')
elif BMI<=27.9:
    print('您的体质过重')
elif BMI<=32.0:
    print('您的体质肥胖')
else:
    print('您已经重度肥胖')