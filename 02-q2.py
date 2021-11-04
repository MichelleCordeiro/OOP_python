n = int(input('Insira a quantidade de números: '))
maior = float(input('Insira um número: ')) # primeiro nr. é lido fora do laço

for i in range(1, n): # laço lê n-1 números
    x = float(input('Insira um número: '))

    if x > maior:
        maior = x

print(f'Maior número: {maior}')