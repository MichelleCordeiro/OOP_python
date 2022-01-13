'''
Exercício de Fixação - Relógio Calendário
Considere duas classes com funcionalidades e interfaces bem definidas:

Relogio: armazena horas, minutos e segundos e avança um segundo quando o método adequado é chamado
Calendario: armazena o dia, mês e ano atual e avança um dia quando o método adequado é chamado
A partir destas duas classes, implemente uma nova classe RelogioCalendario utilizando herança múltipla.

Saída esperada para o código acima:

23:59:59
00:00:00
'''

class Relogio():

    def __init__(self, horas, minutos, segundos):
        self.set_hora(horas, minutos, segundos)

    def set_hora(self, horas, minutos, segundos):
        """
        Atributo horas deve ser um valor inteiro entre 0 e 23
        Atributo minutos deve ser um valor inteiro entre 0 e 59
        Atributo segundos deve ser um valor inteiro entre 0 e 59
        """
        if 0 <= segundos <= 59:
            self.__segundos = segundos
        else:
            print("Segundo inválido")
         
        if 0 <= minutos <= 59:
            self.__minutos = minutos
        else:
            print("Minuto inválido")
        
        if 0 <= horas <= 23:
            self._horas = horas
        else:
            print("Hora inválidos")
        

    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self._horas,
                                                self.__minutos,
                                                self.__segundos)

    def marca_segundo(self):
        """
        Avança um segundo no relógio.
        """
        if self.__segundos == 59:
            self.__segundos = 0
            
            if self.__minutos == 59:
                self.__minutos = 0
                
                if self._horas == 23:
                    self._horas = 0
                else:
                    self._horas += 1
            else:
                self.__minutos += 1
        else:     
            self.__segundos += 1


if __name__ == "__main__":
    r = Relogio(23,59,59)
    print(r)
    r.marca_segundo()
    print(r, "\n")
    
    r = Relogio(13,59,59)
    print(r)
    r.marca_segundo()
    print(r, "\n")
    
    r = Relogio(13,39,59)
    print(r)
    r.marca_segundo()
    print(r, "\n")
    
    r = Relogio(13,39,44)
    print(r)
    r.marca_segundo()
    print(r, "\n")