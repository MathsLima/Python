#Algoritimo para calculo de raizes atraves da formula de Bhaskara.

a = int(input('digite A:  '))

b = int(input('digite B:  '))

c= int(input('digite C:  '))

d = b**2 - 4*a*c

if(d > 0):
    print("x1 =", -b + {d}**(1/2)/(2*a))
    print("x2 =", -b + {d}**(1/2)/(2*a))
elif (d == 0):
    print("x1 = ", -b/(2*a))
else:
    print("Não tenho raizes")