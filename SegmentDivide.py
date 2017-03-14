# -*- coding: utf-8 -*-

def solve(a, b, eps, func):

    while abs(b - a) >= eps:
        delta = (b - a) / 4
        u1 = (b + a - delta) / 2
        u2 = (b + a + delta) / 2
        
        if func(u1) <= func(u2):
            b = u2
        else:
            a = u1

    return (a + b) / 2
