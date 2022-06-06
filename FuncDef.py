import math as gfg

# Declaring a function
def FuncDef():
    print("Function Works!")
    print(gfg.factorial(10))

# Function with yield keyword case
def FuncYield():
    s = 0

    for i in range(10):
        s+=i
        # This keyword yields everytime loop runs
        yield s

if '__main__' == __name__:
    FuncDef()
    for i in FuncYield():
        print(i)