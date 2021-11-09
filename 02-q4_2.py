'''
Implemente uma função que receba como parâmetro um número inteiro. A função deve calcular quantos dos dígitos dos números são pares. Implemente um programa que leia do usuário um número inteiro, realize uma chamada à função e imprima o resultado calculado.
'''

#  USANDO LISTA E STR

def qt_pares(num):
    num_pares = []
    cont_pares = 0
    for i in range(0, len(str(num))):
        num_temp = int(num % 10)
        if num_temp % 2 == 0:
            cont_pares += 1
            num_pares.append(num_temp)
        num = int(num / 10)
    
    num_pares.reverse()
    print('Números pares =', num_pares)
    return cont_pares

#num = 5247968134
num = int(input('Digite um numero inteiro: '))
print('Total de numeros pares =', qt_pares(num))