'''
Implemente um programa que leia do usuário um número N de números inteiros que fazem parte de uma sequência. O programa deve imprimir uma mensagem informando se a sequência é composta apenas de números 0s ou 1s, com a mensagem "sequência no padrão" ou com a mensagem "sequência não está no padrão", caso algum dos números digitados não seja 0 nem 1.
'''

# USANDO LISTA

N = 5
seq = []
cont_diferente = 0

for i in range(0,N):
    seq.append(int(input('Informe um número inteiro: ')))
    
    if seq[i] != 0 and seq[i] != 1 :
        cont_diferente += 1
    
print('Sequencia digitada =', seq)

if cont_diferente == 0 :
    print('sequência no padrão')
else:
    print('A sequência não está no padrão')