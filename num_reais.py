"""
Implemente a classe `Complexo` para representar um número complexo.
Um número complexo é um número $Z = a + bi$, no qual $a$ é a sua parte real, $b$ é a sua parte imaginária e $i$ é $\sqrt{-1}$.

Sua classe deve oferecer os seguintes métodos:
  - `__init__`: inicializa um objeto da classe recebendo como parâmetro a sua parte real e imaginária
  - `reset`: atribui 0.0 à parte real e à parte imaginaria.
  - `__str__`: converte o número complexo em uma string no formato $a + bi$
  - `soma`: retorna um número complexo dado pela soma do próprio objeto com outro. A soma de um número complexo $Z_1 = a_1 + b_1i$ com outro $Z_2 = a_2 + b_2i$ é igual ao número complexo $Z_3 = (a_1 + a_2) + (b_1 + b_2)i$.
  - `modulo`: retorna o módulo do número complexo, dado por $\sqrt{a^2 + b^2}$
"""


import math

class Complexo:
    def __init__(self, real, imag):
        '''Inicialização a parte real e imaginária c1 e c2'''
        self.real = real
        self.imag = imag
    
    def reset(self):
        self.real = 0.0
        self.imag = 0.0
        
    def __str__(self):
        '''Retorna uma representação em formato de string da classe Complexo'''
        return('{} + {}i'.format(self.real, self.imag))
        
    def soma(self, c):
        c_real = (c1.real+c2.real)
        c_imag = (c1.imag+c2.imag)
        return Complexo(c_real, c_imag)
    
    def modulo(self):
        somas = pow(self.real, 2) + pow(self.imag, 2)
        return(math.sqrt(somas))

if __name__ == '__main__':

    c1 = Complexo(2, 3)
    c2 = Complexo(10, 7)
    print(c1)
    print(c2)

    c3 = c1.soma(c2)
    print(c3)
    print(c3.modulo())

    c3.reset()
    print(c3)