'''
Implemente um programa que leia do usuário um número N de números inteiros que fazem parte de uma sequência. O programa deve imprimir uma mensagem informando se a sequência é composta apenas de números 0s ou 1s, com a mensagem "sequência no padrão" ou com a mensagem "sequência não está no padrão", caso algum dos números digitados não seja 0 nem 1.
'''

# # SEM USAR LISTA

N = int(input('Insira a quantidade de números: '))

for i in range(0,N):
    num = int(input('Insira um número: '))

    if num != 0 and num != 1:
        print('Sequência não está no padrão')
        break

print('Sequência está no padrão')