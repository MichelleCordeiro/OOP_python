'''
Implemente um programa que leia três números inteiros denotando os lados de um triangulo. Três números formam um triângulo se cada um deles for menor do que a soma dos outros dois. O programa deve informar se eles formam um triângulo e em caso positivo, qual é o triângulo formado (equilátero, isósceles ou escaleno).
'''


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