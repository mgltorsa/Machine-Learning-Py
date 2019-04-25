from numpy import *


class MachineLearning:
    
        # private Dictionary<int,Category> categories;
        # private int[][] dataInputTraining;
        # private int[] dataOutputTraining;


    def __init__(self):
        
        self.categories = {}
        self.dataInputTraining=[]
        self.dataOutputTraining=[]
        
        
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
        # a = keys = moment.Keys()
        for  a in moment:
            lis=moment.get(a)
            if (lis!=None):
                ca = Category(a,(len(lis)/ len(inputL),lis) )
                # self.categories.setdefault(a,ca)
                            
        # self.dataInputTraining = inputL
        # self.dataOutputTraining = outputL