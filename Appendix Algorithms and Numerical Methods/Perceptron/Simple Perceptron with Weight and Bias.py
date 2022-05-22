#### Simple Perceptron with Weight and Bias



def OR(x1,x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.25
    t = np.sum(w*x) + b
    if t <= 0:
        return 0
    else:
        return 1

print(OR(0,0))     # 0
print(OR(0,1))     # 1
print(OR(1,0))     # 1
print(OR(1,1))     # 1

def NAND(x1,x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.75
    t = np.sum(w*x) + b
    if t <= 0:
        return 0
    else:
        return 1

print(NAND(0,0))    # 1
print(NAND(0,1))    # 1
print(NAND(1,0))    # 1
print(NAND(1,1))    # 0

## XOR: A simple 2-layered perceptron
def XOR(x1,x2):
    α1 = NAND(x1,x2)
    α2 = OR(x1,x2)
    β  = AND(α1,α2)
    return β

print(XOR(0,0))     # 0
print(XOR(0,1))     # 1
print(XOR(1,0))     # 1
print(XOR(1,1))     # 0