import cmath

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
d = (b**2) - (4*a*c)
if d>0:
    print("这个方程有两个不相等的解")
    jie1 = (-b-cmath.sqrt(d))/(2*a)
    jie2 = (-b+cmath.sqrt(d))/(2*a)
    print("x1=", jie1, "\t", "x2=", jie2)
elif d==0:
    print("此方程只有一个解")
    z = (-(b/2*a))
    print("x=", z)
elif d<0:
    print("此方程无解")