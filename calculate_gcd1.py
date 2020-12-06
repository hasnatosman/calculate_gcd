def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


a = 60
b = 48
x = hcf(a, b)
print('The result is : ', x)
