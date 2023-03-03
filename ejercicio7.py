def convertir_a_base(n, B):
    digitos = []
    while n > 0:
        resto = n % B
        digitos.append(resto)
        n //= B
    if B > 36:
        for i in range(len(digitos)):
            if i % 3 == 0 and i > 0:
                digitos[i] = str(digitos[i]) + '.'
            else:
                digitos[i] = str(digitos[i])
    digitos.reverse()
    return ''.join(digitos)
