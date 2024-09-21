# Author: Alec Begay
# My first Python lab in CIS129 course
# This code is an implenmentation of the fibonacci sequence in Python
a, b = 0, 1
print("Initial values: a =", a, "b =", b)
while a < 100:
    print("Inside loop: a =", a)
    print(a); a, b = b, a + b
    print("After iteration: a =", a, "b =", b)
