#### Simple Perceptron

import numpy as np

def NOT(x):
    w = 0.5
    θ = 0.25
    t = x * w
    if t <= θ:
        return 1
    elif t > θ:
        return 0

print(NOT(0))     # 1
print(NOT(1))     # 0

def NAND(x1,x2):
    w1 = -0.5
    w2 = -0.5
    θ  = -0.75
    t  = x1*w1 + x2*w2
    if t <= θ:
        return 0
    elif t > θ:
        return 1

print(NAND(0,0))     # 1
print(NAND(0,1))     # 1
print(NAND(1,0))     # 1
print(NAND(1,1))     # 0

def XOR(x1,x2):
    α1 = NAND(x1,x2)
    α2 = OR(x1,x2)
    β  = AND(α1,α2)
    return β

print(XOR(0,0))     # 0
print(XOR(0,1))     # 1
print(XOR(1,0))     # 1
print(XOR(1,1))     # 0