'''
## Exercício de Fixação 1

Considerando as classes `Pessoa`, `Aluno`, e `Professor`
dos exemplos desta aula, implemente um método de classe que receba
como parâmetro uma lista de pessoas. O método deve calcular
a média de idade das pessoas na lista.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'Pessoa{self.nome, self.idade}'

    def compara_idades(self, p2):
        '''Retorna verdadeiro se self for mais novo que p2.'''
        return self.idade <= p2.idade
    
    def cumprimenta(self, p):
        '''Cumprimenta um objeto p do tipo Pessoa'''
        print(f'Olá {p.nome}, tudo bem?')
        
    def media_idades(self, pesos):
        '''Calcula a media das idades das pessoas da lista'''
        soma = self.idade
        for p in pesos:
            soma += p.idade
        return soma / (len(pesos)+1)

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        Pessoa.__init__(self, nome, idade)
        self.matricula = matricula

    def __repr__(self):
        return f'Aluno{self.nome, self.idade, self.matricula}'

class Professor(Pessoa):
    def __init__(self, nome, idade, departamento):
        super().__init__(nome, idade)
        self.departamento = departamento

    def __repr__(self):
        return f'Professor{self.nome, self.idade, self.departamento}'
    
if __name__ == "__main__":
    p = Pessoa('joao', 3)
    a = Aluno('hugo', 20, 111)
    prof = Professor('santos', 40, 'ECT')

    p1 = Pessoa('maria', 28)
    print(p1.compara_idades(prof))   # método "compara_idades" funciona com qualquer objeto que tenha o atributo "idade"
    
    for pess in [p, a, prof]:
        print(pess)    # executa o __repr__ de cada objeto na lista
    
    p1 = Pessoa('joao', 6)
    p2 = Pessoa('ze', 3)
    p3 = Pessoa('pedro', 2)
    p4 = Pessoa('xuxa', 1)
    lista = [p2, p3, p4]
    print(p1.media_idades(lista))

    print(p.media_idades([a, prof]))