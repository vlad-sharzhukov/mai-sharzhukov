a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
def motoblock (a, b, c):
    result = None
    if a == 0 and b==0 and c==0:
        print ("решений нет")
    elif a==0 and b!=0 and c!=0:
        result = -c/b
    else:
        d=b**2 - 4*a*c
        if d<0:
            print ("решениий нет")
        elif d==0:
            result = ((-b)/(2*a))
            return result
        elif d>0:
            x1 = (((-b)+((d)**(-1/2)))/(2*a))
            x2 = (((-b)-((d)**(-1/2)))/(2*a))
            return x1, x2 
print (motoblock (a, b, c))
