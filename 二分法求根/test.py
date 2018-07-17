#已知 f(x)=X^2+3X-10,用二分法求根

l = float(input("请输入对称轴："))

middlel = (-100+0)/2
middler = (0+100)/2
def funl(left,right,middle):
    while right-left>0.00000000000000000001:
        if middle*middle+3*middle-10 == 0:
            break
        if ((middle*middle+3*middle-10)*(left*left+3*left-10))<0:
            right = middle
            middle = (left+right)/2
        else:
            left = middle
            middle = (left+right)/2
    return middle
def funr(left,right,middle):
    while right-left>0.00000000000000000001:
        if middle*middle+3*middle-10 == 0:
            break
        if ((middle*middle+3*middle-10)*(left*left+3*left-10))<0:
            right = middle
            middle = (left+right)/2
        else:
            left = middle
            middle = (left+right)/2
    return middle
print("左边的根：" + str(funl(-100,l,middlel)))
print("右边的根：" + str(funr( l,100,middler)))