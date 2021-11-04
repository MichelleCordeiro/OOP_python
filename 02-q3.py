n = int(input('Insira a quantidade de números: '))

for i in range(n):
    x = int(input('Insira um número: '))

    if x != 0 and x != 1:
        print('Sequência não está no padrão')
        break
else: # for pythonico: só vai para o else se terminou sem break
    print('Sequência está no padrão')