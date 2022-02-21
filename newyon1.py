from math import sin
from math import cos
e = 2.71828182846
from datetime import date, datetime, timedelta
def final_answer(x):
    now = datetime.now()
    the_date = now.day * 10000 + now.hour * 100 + now.minute
    # print(the_date)
    x=float(x)
    x = str(round(x, 6)) + "00000" + str(the_date)
    return x
def newtonRaphson(f,g,x0, e=10**-10, N=21):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break

        x1 = x0 - f(x0) / g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
        return float(x1)
    else:
        print('\nNot Convergent.')

def roots(f,g,factor,eps=10**-10):
    flag=0
    #f=function
    #eps=epsilon
    #factor=array of the segments
    #g=the derivative function
    root=[]

    for i in range(len(factor)-1):
        a=factor[i]
        b=factor[i+1]

        x=f(a)
        y=f(b)
        if -eps<x<eps:
            root.append(float(a))
            continue

        if x*y<0:
            root.append(newtonRaphson(f,g,(a+b)/2))
            continue

        elif g(a)*g(b)<0 :

            res=newtonRaphson(f,g,(a+b)/2)


            if res:
                for i in root:
                    a=round(i,7)
                    b=round(res,7)
                    if a==b:
                        flag=1
                if flag:
                    continue

                if -eps<f(res)<eps:
                    root.append(res)
            else:
                continue


    return root

p = lambda x: sin(x**2+5*x+6)/(2*e**(-x))
Dp = lambda x: 1/2* e**x*((5 + 2**x)*cos(6 + 5*x + x**2) + sin(6 + 5*x + x**2))
approx = roots(p, Dp, [-3,-2.6,-2.2,-1.8,-1.4,-1,-0.6,-0.2,0.2,0.6,1])
for i in approx:
    print(final_answer(i))
print(approx)