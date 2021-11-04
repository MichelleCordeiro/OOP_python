def conta_dig_pares(x):
    '''
    Retorna dígitos pares do número
    inteiro x.
    '''

    cont = 0

    while x > 0:
        if x % 2 == 0:
            cont += 1

        x = x // 10

    return cont

num = int(input('Insira um número inteiro: '))
print(f'Número tem {conta_dig_pares(num)} dígitos pares')