def change(n,m):
    result = n = (n/m)
    return result

n = 10

try:
    print(change(n,0))
except ZeroDivisionError as ze:
    print(ze)
    print(change(n,1))