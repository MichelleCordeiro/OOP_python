'''
Saída esperada para o código acima:

Passou um segundo de 31/12/2013, 23:59:59 para 01/01/2014, 00:00:00
Passou um segundo de 07/02/2013, 13:55:40 para 07/02/2013, 13:55:41
'''


from _17_relogio import Relogio
from _17_calendario import Calendario

class CalendarioRelogio(Relogio, Calendario):
    def __init__(self, dia, mes, ano, horas, minutos, segundos):
        #super().__init__(dia, mes, ano, horas, minutos, segundos)
        Relogio.__init__(self, horas, minutos, segundos)
        Calendario.__init__(self, dia, mes, ano)
        #Calendario.__init__(self, dia, mes, ano)
        
        #super().set_data(dia, mes, ano)
        #super().set_hora(horas, minutos, segundos)
        #Calendario.set_data(self, dia, mes, ano)
        #Relogio.set_hora(self, horas, minutos, segundos)
        
    def marca_segundo(self):
        """
        Avança um segundo no relógio.
        """
        #Checa se após add 1seg a hora "zerou/o dia virou" p implentar mais um dia
        hora_original = self._horas
        Relogio.marca_segundo(self)
        if hora_original > self._horas:   # 23 > 00
            self.avanca_dia()
            
    def __str__(self):
        return Calendario.__str__(self) + ", " + Relogio.__str__(self)
            

if __name__ == "__main__":
    cr = CalendarioRelogio(31, 12, 2013, 23, 59, 59)
    #print(CalendarioRelogio.mro())
    print("Passou um segundo de", cr, end=" ")
    cr.marca_segundo()
    print("para", cr)
    
    cr = CalendarioRelogio(7, 2, 2013, 13, 55, 40)
    print("Passou um segundo de", cr, end=" ")
    cr.marca_segundo()
    print("para", cr)