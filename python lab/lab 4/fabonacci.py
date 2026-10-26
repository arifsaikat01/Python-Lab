N = int(input("Enter N: "))

a, b = 0, 1

while a < N:
    print(a)
    a, b = b, a + b