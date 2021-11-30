'''Prática 1.2: Pessoas e Vacinação
Implemente a classe Pessoa, a ser utilizada no contexto da vacinação contra a COVID19.

Para isto, a classe deve ter como atributos:

O nome da pessoa (com getter/setter)
A idade da pessoa (com getter/setter)
A quantidade de doses_vac de vacinas` que a pessoa tomou (apenas getter)
O tipo_vac de vacina que a pessoa tomou (apenas getter)
A classe deve possuir os seguintes métodos

__init__: deve receber o nome e idade como parâmetros
__str__: deve retornar uma string com os dados da pessoa no formato nome - idade (X doses tipo Y), onde Y é um caractere identificando o tipo de vacina que a pessoa tomou
toma_vacina: faz a pessoa tomar a vacina, de acordo com um tipo passado como parâmetro. O método deve incrementar a quantidade de doses tomada pela pessoa, de acordo com a seguinte lógica:
Caso a pessoa não tenha tomado nenhuma vacina, o atributo tipo_vac deve receber o valor do parâmetro
Caso a pessoa já tenha tomado alguma vacina, a dose só deve ser incrementada se o parâmetro for do mesmo tipo de tipo_vac. Se não for, a mensagem "Paciente já vacinado com outro tipo de vacina" deve ser impressa
Utilize o código a seguir como ponto de partida. O código de teste para a sua classe é dado e não deve ser modificado.


Saída esperada do programa:

Inicialização:
mario, 33 anos (0 doses)
roberta, 21 anos (0 doses)
vilma, 57 anos (0 doses)

Vacinação:
#aplicando vacina tipo C em mario
#aplicando vacina do mesmo tipo em mario
mario, 33 anos (2 doses tipo C)

#aplicando vacina tipo A em vilma
#vilma tem uma dose do tipo A e por isso não pode tomar C
Paciente já vacinado com outro tipo de vacina
vilma, 57 anos (1 doses tipo A)

#aplicando vacina tipo B em francisca
#aplicando vacina do mesmo tipo em francisca
francisca, 48 anos (2 doses tipo B)
'''

class Pessoa:
    '''Representa uma pessoa a ser vacinada.'''    
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__doses_vac = 0
        self.__tipo_vac = ''
    
    @property
    def nome(self):
        '''Retorna o nome'''
        return self.__nome
    
    @property
    def idade(self):
        '''Retorna a idade'''
        return self.__idade
    
    @property
    def doses_vac(self):
        '''Retorna a qtdade de dases'''
        return self.__doses_vac
    
    @property
    def tipo_vac(self):
        '''Retorna o tipo da vacina'''
        return self.__tipo_vac
    
    @nome.setter
    def nome(self, novo_nome):
        '''Muda o nome'''
        self.__nome = novo_nome
    
    @idade.setter
    def idade(self, nova_idade):
        '''Muda a idade'''
        self.__idade = nova_idade
    
    def toma_vacina(self, tipo_vac):
        if self.__doses_vac == 0:
            self.__tipo_vac = tipo_vac
            self.__doses_vac += 1
        elif self.__tipo_vac == tipo_vac:
            self.__doses_vac += 1
        else:
            print("Paciente já vacinado com outro tipo de vacina")
    
    def __str__(self):
        if self.__doses_vac == 0:
            return '{}, {} anos ({} doses)'.format(self.__nome, self.__idade, self.__doses_vac)
        else:
            return '{}, {} anos ({} doses tipo {})'.format(self.__nome, self.__idade, self.__doses_vac, self.__tipo_vac)

if __name__ == "__main__":
    print('Inicialização:')
    p1 = Pessoa('mario', 33)
    p2 = Pessoa('roberta', 21)
    p3 = Pessoa('vilma', 57)
    print(p1)
    print(p2)
    print(p3)

    print('\nVacinação:')
    p1.toma_vacina('C')
    p1.toma_vacina('C')
    print(p1)

    p3.toma_vacina('A')
    p3.toma_vacina('C')
    print(p3)
    
    p2.nome = 'francisca'
    p2.idade = 48
    p2.toma_vacina('B')
    p2.toma_vacina('B')
    print(p2)