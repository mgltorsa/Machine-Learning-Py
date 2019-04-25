""" 
La controladora se encarga de 
cargar las imagenes (las shapes de los digitos),
entrenar el bayes y mostrar resultados.

Nota: es preferible que cada una de las funcionalidades
anteriormente mencionadas se haga en metodos
y dentro de una clase para reducir tiempos de carga.

@Author Miguel Torres

"""

from naive.bayes import MachineLearning
import pathlib
from sklearn.datasets import load_digits
import pylab as pl
import sklearn

class Controller:

    def __init__(self):
        self.bayes = MachineLearning()
        self.inputs = []
        self.outputs= []
        
    def __loadDefault(self):
        self.digits = load_digits()
        self.targets = self.digits.target

    def __listFilter(self,number1, targets):
        indices_list = []
        for i in range(0, len(targets)):
            if targets[i] == number1:
                indices_list.append(i)
        return indices_list

    def loadInfo(self):
        self.__loadDefault(); 
        self.inputs = self.digits.images
     
            

    def loadInfoNumber(self,number : int):
        self.__resetInfo()
        self.__loadDefault()
        array = self.__listFilter(number,self.targets)
        """Filtra todos los index de los target == number"""
        for index in array:
            self.inputs.append(self.digits.images[index])
            


    def __resetInfo(self):
        self.inputs=[]
        pass
    
    def getAllStatisticalResults(self):
        pass

    def getStatisticalResults(self,number : int):
        pass


    def trainNaive(self):

        #TODO: Pasar self.inputs (Matrix) a una arreglo
        inputs = []
        outputs = []
        self.bayes.Learn(inputs,outputs)


c = Controller()

c.loadInfo()





