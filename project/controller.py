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
        self.trainingPercentage=0.4
        self.testPercentage=0.6

    def setTrainingPercentage(self,percentage):
        self.trainingPercentage=percentage
    
    def setTestPercentage(self, percentage):
        self.testPercentage=0.6
        
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
        self.filteredArray = []
        for i in range(len(self.targets)):
            self.filteredArray.append(i);
    
    def getAllStatisticalResults(self):
        results = self.decide()
        cases = int(self.trainingPercentage*len(self.inputs))
        #Dictionary with numbers [accerts, fails]
        numbers={
                    0:[0,0],
                    1:[0,0],
                    2:[0,0],
                    3:[0,0],
                    4:[0,0],
                    5:[0,0],
                    6:[0,0],
                    7:[0,0],
                    8:[0,0],
                    9:[0,0],
                 }
                
        for i in range(len(results)):
            if int(results[i]) == self.targets[cases+i]:
                numbers[self.targets[cases+i]][0]+=1

            else:
                numbers[self.targets[cases+i]][1]+=1   

        message ="number - hit - fails - hitRate - failsRate \n"
        total_tested = len(self.inputs)-cases
        print("total tested : %s " % (total_tested) )
        
        print("for training: %s and for test %s" % (self.trainingPercentage,1-self.trainingPercentage) )

        for key in numbers:
            hits = numbers[key][0]
            fails = numbers[key][1]
            hitsRate = hits / (hits+fails)
            failsRate = fails / (hits+fails)
            message += "%s        %s      %s     %.3f     %.3f \n" % (key,hits,fails,hitsRate,failsRate )

        return message
        

    def getStatisticalResults(self,number : int):
        filteredArray = self.__listFilter(number,self.targets)


        return None

    def decide(self):
        inputsL = []      
        cases = int(self.trainingPercentage*len(self.inputs))
        for i in range(cases,len(self.inputs)):
            image_arr = []
            for row in self.inputs[i]:
                image_arr.extend(row)
            inputsL.append(image_arr)
        
        results = self.bayes.Decide(inputsL)
        return results

    def trainNaive(self):

        #TODO: Pasar self.inputs (Matrix) a una arreglo
        inputs = self.getTrainingData()
        outputs = self.getTrainingTargets()

        self.bayes.Learn(inputs,outputs)

    def getTrainingTargets(self):
        cases = int(self.trainingPercentage*len(self.filteredArray))
        trainingTargets=[]
        for i in range(cases):
            indexOfTarget = self.filteredArray[i];
            trainingTargets.append(self.targets[indexOfTarget])     
        return trainingTargets
    
    def getTrainingData(self):
        cases = int(self.trainingPercentage*len(self.inputs))
        trainingData=[]
        for i in range(cases):
            formatted_image = []
            for row in self.inputs[i]:
                formatted_image.extend(row)

            """ print test
            if i==7:
                print("formatted")
                print(formatted_image)
                print("image")
                print(str(self.inputs[i]))  
                print("with target: %s" % (self.targets[self.filteredArray[i]]))  """        
            trainingData.append(formatted_image)
        return trainingData




c = Controller()

c.loadInfo()
c.trainNaive()
results = c.getAllStatisticalResults()

print("results")
print(results)





