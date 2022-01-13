'''
POO 2021.1 - Prova 2
Um sistema envolvendo diferentes tipos de polígonos possui modelagem como descrita a seguir.

Implemente o sistema e entregue também o diagrama de classes do sistema.

Classe Abstrata Poligono¶
Representa um polígono qualquer.

Atributos:

centro: tupla de 2 números reais contendo as coordenadas do centro do polígono
lados: tupla de tamanho  𝑛≥3  contendo os tamanhos dos lados de um polígono
num_lados: deve fornecer o número de lados do polígono a partir do tamanho da tupla lados
Métodos:

distancia: método de classe que retorna a distância entre dois polígonos passados por parâmetro. Sendo  𝑃1  e  𝑃2  dois polígonos, a distância entre eles é dada por  𝑑(𝑃1,𝑃2)=(𝑥𝑐1−𝑥𝑐2)2+(𝑦𝑐1−𝑦𝑐2)2⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯√ , onde  𝑥𝑐𝑖  e  𝑦𝑐𝑖  são as coordenadas do centro do polígono  𝑃𝑖 .
perimetro: método abstrato que calcula o perímetro de um polígono. Deve ter implementação dada pelo somatório de todos os lados.
area: método abstrato que calcula a área de um polígono (sem implementação)
__repr__: método abstrato para retornar uma string representando o polígono (sem implementação)
eh_regular: método que retorna verdadeiro se o polígono possuir todos os seus lados iguais (polígono regular) ou falso caso contrário
__init__: deve receber como parâmetros as tuplas informando o centro do polígono e os tamanhos dos seus lados
Classe PoligonoRegular
Representa um polígono regular. Herda diretamente da classe base abstrata Poligono.

Métodos:

Reimplementação de perimetro: deve retornar este valor como sendo o produto entre qualquer dos seus lados e o seu número de lados
Implementação de __repr__: deve retornar a string "Poligono regular de n lados, lado igual a s"
Implementação de area: um polígono regular tem sua área dada por  𝑠2𝑛4tan(𝜋𝑛) , onde  𝑠  é o tamanho do seu lado,  𝑛  é o seu número de lados e o ângulo  𝜋𝑛  está em radianos. Utilize a função math.tan que recebe um ângulo em radianos e a constante math.pi.
__init__: deve checar se o polígono é regular e caso não seja, deve imprimir uma mensagem de erro
Classe TrianguloEquilatero
Representa um triângulo com três lados iguais. Herda diretamente da classe PoligonoRegular.

Métodos:

Implementação de __repr__: deve retornar a string "Triangulo equilatero com lado igual a s"
__init__: ao invés da tupla com os valores dos lados, recebe como parâmetro um número real com o valor do lado do triângulo equilátero.
Classe Quadrado
Representa um quadrado. Herda diretamente da classe PoligonoRegular.

Métodos:

Implementação de __repr__: deve retornar a string "Quadrado com lado igual a s"
__init__: ao invés da tupla com os valores dos lados, recebe como parâmetro um número real com o valor do lado do quadrado.


Saída esperada:

Triangulo equilatero com lado igual a 2
    >Perimetro: 6
    >Area: 1.7320508075688779
Triangulo equilatero com lado igual a 3
    >Perimetro: 9
    >Area: 3.8971143170299753
Quadrado com lado igual a 4
    >Perimetro: 16
    >Area: 16.000000000000004
Poligono regular de 5 lados, lado igual a 7
    >Perimetro: 35
    >Area: 84.30339262885938
Distancia entre o quadrado e o pentagono: 28.284271247461902
Lados informados nao formam um poligono regular
'''

from abc import ABC, abstractmethod
from math import dist, tan, pi

class Poligono(ABC):
    '''
    Representa um polígono qualquer.
    '''

    def __init__(self, centro, lados):
        '''
        Parâmetros
        ----------
        centro : tupla
        Informacao do centro do poligono
        lados : tupla
        Tamanho dos lados do poligono
        num_lados : int
        Fornece o numero de lados a partir do tamanho da tupla lados 

        Retorno
        -------
        Poligono
        Poligono inicializado.
        '''

        self.centro = (centro)
        self.lados = lados
        self.num_lados = len(lados)
    
    @abstractmethod
    def __repr__(self):
        '''
        Retorno
        -------
        String
        Retornar uma string representando o polígono.
        '''
        pass

    def eh_regular(self):
        '''
        Retorno
        -------
        Bool
        Retorna verdadeiro se o polígono possuir todos os seus lados iguais ou falso caso contrário
        '''
        #for lado in self.lados:
        i = 0
        while i < len(self.lados)-1:
            if self.lados[i] != self.lados[i+1]:
                return False
            i += 1
        return True
    
    @abstractmethod
    def perimetro(self):
        '''    
        Retorno
        -------
        Float
        Calcula o perímetro de um polígono pelo somatorio de seus lados
        '''
        for lado in self.lados:
            per += lado
        return per
    
    @abstractmethod
    def area(self):
        '''
        Retorno
        -------
        Float
        Calcula a área de um polígono
        '''
        pass

    def distancia(self, outro):
        '''
        Parâmetros
        ----------
        outro: Poligono
        Poligono a ser usado para calcular a distancia de outro poligono

        Retorno
        -------
        Float
        Calcula a distancia entre dois polígonos
        '''
        return dist(self.centro, outro.centro)


class PoligonoRegular(Poligono):
    '''
    Representa um polígono regular.
    '''

    def __init__(self, centro, lados):
        '''
        Parâmetros
        ----------
        centro : tupla
        Informacao do centro do poligono
        lados : tupla
        Tamanho dos lados do poligono
        num_lados : int
        Fornece o numero de lados a partir do tamanho da tupla lados 

        Retorno
        -------
        PoligonoRegular
        PoligonoRegular inicializado.
        '''

        super().__init__(centro, lados)

        if not self.eh_regular():
            print('Nao eh um poligono regular')
    
    def __repr__(self):
        '''
        Retorno
        -------
        String
        Retorna uma string.
        '''
        #return f'Poligono regular de {self.lados} lados, lado igual a {self.num_lados}'
        return f'Poligono regular de {self.num_lados} lados, lado igual a {self.lados[0]}'

    def perimetro(self):
        '''    
        Retorno
        -------
        Float
        Calcula o perímetro de um polígono regular multiplicando seu nº de lados
        pelo tamanho de um dos lados.
        '''
        return self.num_lados * self.lados[0]
    
    def area(self):
        '''
        Retorno
        -------
        Float
        Calcula a área de um polígono regular por 
        (lados**2 * nº de lados) / (4 * tan(pi/nº de lados)radianos))
        '''
        return (self.lados[0] ** 2 * self.num_lados) / (4 * tan(pi / self.num_lados))


class Quadrado(PoligonoRegular):
    '''
    Representa um quadrado.
    '''

    def __init__(self, centro, lados):
        '''
        Parâmetros
        ----------
        lados : float
        Tamanho dos lados do quadrado

        Retorno
        -------
        Quadrado
        Quadrado inicializado.
        '''

        #super().__init__(centro, lados)
        #self.lados = lados
        self.centro = (centro)
        self.lados = (lados, lados, lados, lados)
        self.num_lados = 4
    
    def __repr__(self):
        '''
        Retorno
        -------
        String
        Retorna uma string.
        '''
        return f'Quadrado com lado igual a {self.lados[0]}'


class TrianguloEquilatero(PoligonoRegular):
    '''
    Representa um triângulo com três lados iguais.
    '''

    def __init__(self, centro, lados):
        '''
        Parâmetros
        ----------
        lados : float
        Tamanho dos lados do triangulo equilatero.

        Retorno
        -------
        TrianguloEquilatero
        TrianguloEquilatero inicializado.
        '''

        #super().__init__(centro, lados)
        self.centro = centro
        self.lados = (lados, lados, lados)
        self.num_lados = 3
    
    def __repr__(self):
        '''
        Retorno
        -------
        String
        Retorna uma string.
        '''
        return f'Triangulo equilatero com lado igual a {self.lados[0]}'


if __name__ == "__main__":
    
    t1 = TrianguloEquilatero((5.0, 5.0), 2)
    print(t1)
    print(">Perimetro: {}".format(t1.perimetro()))
    print(">Area: {}".format(t1.area()))
    
    t2 = TrianguloEquilatero((0.0, -2.0), 3)
    print(t2)
    print(">Perimetro: {}".format(t2.perimetro()))
    print(">Area: {}".format(t2.area()))
    
    q1 = Quadrado((10.0, 10.0), 4)
    print(q1)
    print(">Perimetro: {}".format(q1.perimetro()))
    print(">Area: {}".format(q1.area()))
    
    p1 = PoligonoRegular((-10.0, -10.0), (7,7,7,7,7))
    print(p1)
    print(">Perimetro: {}".format(p1.perimetro()))
    print(">Area: {}".format(p1.area()))
    print("Distancia entre o quadrado e o pentagono: {}".format(Poligono.distancia(q1, p1)))

    perr = PoligonoRegular((5.0, 5.0), (6, 6, 6, 5, 6, 6))