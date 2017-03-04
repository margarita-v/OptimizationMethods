# -*- coding: utf-8 -*-

import sys

def func(x):
    return x*x

def solve(a, b, eps):
    if a > b:
        a, b = b, a

    while True:
        delta = (b - a) / 4
        u1 = (b + a - delta) / 2
        u2 = (b + a + delta) / 2
        
        if func(u1) <= func(u2):
            b = u2
        else:
            a = u1
            
        # условие прекращения цикла
        if not abs(b - a) >= eps:
            break
    return a
