from numpy import zeros
from numpy import *
class MachingLearn:
    
        # private Dictionary<int,Category> categories;
        # private int[][] dataInputTraining;
        # private int[] dataOutputTraining;


        def __init__():
        
            categories = {}
        
        
        def Decide(self,input,ret):
        
            res = True
            ret =zeros(input.Length)
            for i in range(input.Length):
            
                res = res and DecideV(input[i],ret[i])
               
            
            return res
        
        def DecideV(self,input, ret):
            ret = -1
            pro = Double.MinValue
            for  a in self.keys:
                tmp=self.categories[a]
                prop = tmp.Propiedades
                plus = tmp.Plus
                sum = tmp.Proba
                for  i in range(prop):
                    
                   if (input[i] != 0):
                  
                       sum *= plus[i] * input[i]
                                   
                if(sum > pro ): ret=a 
                if(sum > pro): pro=sum 
                
            return ret
        
        def Learn(self,inputL,outputL):
        
            moment = {}
            for i in range(input.Length):
            
                tmp = inputL[i]
                clas = outputL[i]
                lis= moment.get(clas)
                nExist=lis==None
                if (nExist):                
                  lis = {}                
                lis.append(tmp)
                if (nExist):
                    moment.setdefault(clas,lis)              
            
            keys = moment.Keys()
            for  a in keys:
                lis=moment.get(a)
                if (lis!=None):
                    ca = new Category(a,(len(lis)/ len(inputL),lis)
                    categories.Add(a, ca);
            
            self.dataInputTraining = inputL
            self.dataOutputTraining = outputL



class Category:
    def Category(self, name, pr, values):
        self.Proba = pr
        self.name = name
        self.values = values
        self.propiedades = values[0].Length
        self.plus = zeros(values[0].Length)
        self.CalculateAverage()

    def CalculateAverage(self):
        total=0
        for i in range(self.values[0].Length):

            sum = 0
            for j in range(self.values.Length):

                sum += self.values[j][i]
                total+=self.values[j][i]

            self.plus[i] = sum

        for i in range(self.propiedades):

            self.plus[i] = self.plus[i]/total
