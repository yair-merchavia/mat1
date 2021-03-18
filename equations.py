
def exponent(x:float)-> float:
    x=float(x)
    e = 0
    j = 1 
    x1 = x
    for i in range(50):
        if i == 0 :
            e = +1
        else:
            e += x1/j
            i1 = i+1
            j = j*(i1)
            x1 = x*x1
    #e=float('%0.6f' % e)
    return float(e)

def Abs(x:float)-> float:
    x=float(x)
    if x>=0:
        return x
    else:
        return float(x*-1)

def Ln(x:float)-> float:
    x=float(x)
    if x>0:
        yn =x-1
        yn1 = yn
        yn1 += 2*((x-exponent(yn))/(x+exponent(yn)))  
        while Abs(yn-yn1)>0.0001:
           yn=yn1
           yn1 += 2*((x-exponent(yn))/(x+exponent(yn)))      
    else:
        yn1=0
    #yn1=float('%0.6f' % yn1)    
    return float(yn1)


def XtimesY(x:float,y:float) -> float:
    x=float(x)
    y=float(y)
    if x>0:
        x_y=exponent(y*Ln(x))
        x_y=float('%0.6f' % x_y)
    else:
        x_y=0
    return float(x_y)


def sqrt(x:float,y:float) -> float:
    x=float(x)
    y=float(y)
    if x!=0:
        x=1/x
    else:
        x=0
    x_y=exponent(x*Ln(y))
    #x_y=float('%0.6f' % x_y)
    return float(x_y)

def calculate(x:float) -> float:
    x=float(x)
    p=exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
    p=float('%0.5f' % p)
    return float(p)

