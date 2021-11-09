'''
Implemente um programa que leia do usuário um total N de números reais e imprima na tela qual foi o maior número digitado.
'''

N = float(input('Digite um numero: '))    #o usuario define qdo parar as entradas
maior = N

while N != -99999:         # MEU ERRO ESTAVA AQUI, A CONDIÇÃO DE PARADA ERA O ZERO
    print('Até agora o maior numero é:', maior)
    N = float(input('Digite outro numero(para sair digite -99999): '))
    if maior < N:
      maior = N
      
print('O maior numero é:', maior)