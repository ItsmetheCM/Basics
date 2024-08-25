# import pandas as pd
#
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
# df = pd.read_csv(url, header = None)
import math


# # Swap variables
v1 ="first string"
v2 = "second string"
vs = v1
v1=v2
v2=vs
print(v1)
print(v2)

# # If else

a = 4
b = 5
if a == b:
    print("both are equal")
else:
    if a < b:
        print("b is greater")
    else:
        print("a is greater")
print("out of the block")


a = int(input())
b = int(input())
intDiv = (a//b)
fltDiv = (a/b)
print("The result of the integer division", a, "//", b, "=", intDiv)
print("The result of the float division", a, "/", b, "=", fltDiv)


n = int(input())
if n <= 20:
    for i in range(1, n):
        n = i*i
        print(n)

