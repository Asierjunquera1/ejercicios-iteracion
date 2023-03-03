def mcd2(a, b):
    a = abs(a)
    b = abs(b)
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
