'''
Prática 3b: Oficina de Carros
Defina a classe Carro, que deve conter a sua marca e modelo. Defina o seu método __str__.

Defina a classe Patio, que deve ter um nome e uma lista de carros. Os métodos adiciona_carro e imprime_carros devem ser implementados.

Por fim, implemente a classe Oficina, que é uma composição de três pátios: o primeiro para carros da marca 'bmw' ou 'audi', o segundo para 'citroen' ou 'renault' e o último para 'chevrolet' ou 'ford'. Os seus métodos devem ser os mesmos da classe Patio, com a diferença que o carro deve ser adicionado ao pátio apropriado (de acordo com sua marca).

Utilize o código base a seguir como ponto de partida.


Resultado esperado:

Carros do Patio alemão
    audi a3
    bmw m3
Carros do Patio francês
    citroen c4
    renault clio
Carros do Patio americano
    chevrolet malibu
    ford focus
'''

class Carro:
    '''Um carro'''
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
    def __str__(self):
        return f'{self._marca} {self._modelo}'
    
class Patio:
    '''Um patio com varios carros'''
    def __init__(self, nome, carro):
        self._nome = nome
        self._lista_carros = []
        
    def adiciona_carro(self, carro):
        self._lista_carros.append(carro)
        
    def imprime_carros(self):
        print(f'Carros do Patio {self._nom}\n    {carro}')  

class Oficina:
    '''Uma oficina com varios pátios'''
    def __init__(self):
        self._patio = [Patio("alemão",None), Patio("francês",None), Patio("americano",None)]
            
    def adiciona_carro(self, carro):
        if carro._marca == "audi" or carro._marca == "bmw":
            self._patio[0].adiciona_carro(carro)
        elif carro._marca == "citroen" or carro._marca == "renault":
            self._patio[1].adiciona_carro(carro)
        else:
            self._patio[2].adiciona_carro(carro)
        
    def imprime_carros(self):
        for p in self._patio:
            print(f'Carros do Patio {p._nome}')
            for car in p._lista_carros:
                print(f'    {car}')

if __name__ == "__main__":
    # cria instâncias da classe carro
    c1 = Carro('audi', 'a3')
    c2 = Carro('bmw', 'm3')
    c3 = Carro('citroen', 'c4')
    c4 = Carro('renault', 'clio')
    c5 = Carro('chevrolet', 'malibu')
    c6 = Carro('ford', 'focus')

    # cria uma instância de oficina
    # observe que pátios são criados pela oficina (composição)
    ofic = Oficina()
    # adiciona carros à oficina (aos seus pátios)
    ofic.adiciona_carro(c1)
    ofic.adiciona_carro(c2)
    ofic.adiciona_carro(c3)
    ofic.adiciona_carro(c4)
    ofic.adiciona_carro(c5)
    ofic.adiciona_carro(c6)

    # imprime os carros da oficina (imprime os carros de cada pátio)
    ofic.imprime_carros()