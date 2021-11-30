'''
Implemente uma função que receba como parâmetro um número inteiro. A função deve calcular quantos dos dígitos dos números são pares. Implemente um programa que leia do usuário um número inteiro, realize uma chamada à função e imprima o resultado calculado.
'''

# SEM USAR LISTA E STR

def qt_pares(num):
    cont_pares = 0
    
    while num > 0:
        #print(num)
        
        if num % 2 == 0:
            cont_pares += 1
        num = int(num // 10)
        #print(num)
    return cont_pares
    
#num = 5247968134
num = int(input('Digite um numero inteiro: '))
print('Total de numeros pares =', qt_pares(num))
#print(f'Número tem {cont_pares(num)} dígitos pares')