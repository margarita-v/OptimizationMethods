from math import sqrt
    
k1 = (3 - sqrt(5))/2
k2 = (sqrt(5) - 1)/2
    
def U1(a, b):
    return k1*(b - a) + a

def U2(a, b):
    return k2*(b - a) + a

def solve(a, b, eps, func):
    u1 = U1(a, b)
    u2 = U2(a, b)
    
    while abs(b - a) > eps:
        if func(u1) <= func(u2):
            b = u2
            u2 = u1
            u1 = U1(a, b)
        else:
            a = u1
            u1 = U1(a, b)
            u2 = U2(a, b)
    return (a + b) / 2
