x = int(input('insira o 1o. lado: '))
y = int(input('insira o 1o. lado: '))
z = int(input('insira o 1o. lado: '))

if (x < y + z) and (y < x + z) and (z < x + y):
    print('Lados formam um triângulo')
    if x == y == z:
        print('O triângulo é equilátero')
    elif x != y != z:
        print('O triângulo é escaleno')
    else:
        print('O triângulo é isósceles')
else:
    print('Lados não formam um triângulo')