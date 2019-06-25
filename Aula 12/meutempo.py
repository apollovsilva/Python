import numpy as np

class  MeuTempo : 
    # Métodos previamente definidos aqui ... 
    def  __init__ ( self ,  hrs = 0 ,  mins = 0 ,  segs = 0 ): 
        """ Criar um novo objeto MeuTempo inicializado para hrs, min, segs. 
           Os valores de mins e segs podem estar fora do intervalo de 0-59, 
           mas o objecto MeuTempo resultante será normalizado.  """ 
        # Calcular total de segundos para representar 
        self.totalsegs =  hrs * 3600  +  mins * 60  +  segs 
        self.horas =  self.totalsegs  //  3600         # Divisão em h, m, s 
        restosegs =  self.totalsegs  %  3600 
        self.minutos  =  restosegs  //  60 
        self.segundos  =  restosegs  %  60
        if self.horas >=24:
            self.horas = self.horas%24

            
    def  to_seconds (self): 
        "" "Retorna o número de segundos representados por esta instância " "" 
        return  self.totalsegs

    
    def  __add__ (self, other): 
        """ Retorna a soma do tempo atual e outro, para utilizar com o simbolo + """
        return  MeuTempo(0, 0, self.to_seconds() + other.to_seconds())

    
    def  __sub__ (self, other): 
        """ Retorna a soma do tempo atual e outro, para utilizar com o simbolo - """
        return  MeuTempo(0, 0, np.abs(self.to_seconds() - other.to_seconds()))
    
    
    def __str__(self):
        """Retorna uma representação do objeto como string, legível para humanos."""
        return '%.2d:%.2d:%.2d'%(self.horas, self.minutos, self.segundos)


a=MeuTempo(1,40,30)
b=MeuTempo(12,55,15)

print(a,b)
print(a + b)
print(a - b)
print(a,b)
