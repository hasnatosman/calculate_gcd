def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


print('result: ', gcd(100, 47))
