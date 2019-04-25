from numpy import zeros

class MachineLearning:
    
        # private Dictionary<int,Category> categories;
        # private int[][] dataInputTraining;
        # private int[] dataOutputTraining;


    def __init__(self):
        
        self.categories = {}
        self.dataInputTraining=[]
        self.dataOutputTraining=[]
        
        
    def Decide(self,inputL):    
        ret =zeros(len(inputL))
        for i in range(len(inputL)):    
             ret[i] = self.DecideV(inputL[i])
        return ret
        
    def DecideV(self,input):
        ret = -1
        pro = -1
        for  a in (self.categories).keys():
            tmp=self.categories[a]
            prop = tmp.propiedades
            plus = tmp.plus
            sum = tmp.Proba
            for  i in range(prop):
                    
               if (input[i] != 0):                  
                   sum *= plus[i] * input[i]
                                   
            if(sum > pro ): ret=a 
            if(sum > pro): pro=sum 
                
        return ret
        
    def Learn(self,inputL,outputL):
        moment = {}
        for i in range(len(inputL)):      
            tmp = inputL[i]
            clas = outputL[i]
            lis= moment.get(clas)
            nExist=lis==None
            if (nExist):                
                lis = []                
            lis.append(tmp)
            if (nExist):
                moment.setdefault(clas,lis)                      
        keys = moment.keys()
        for  a in keys:
            lis=moment.get(a)
            if (lis!=None):
                ca = Category(a,(len(lis)/ len(inputL)),lis)
                (self.categories).setdefault(a,ca)
                            
        self.dataInputTraining = inputL
        self.dataOutputTraining = outputL
        
class Category:

    def __init__(self, name, pr, values):
        self.Proba = pr
        self.name = name
        self.values = values
        self.propiedades = len(values[0])
        self.plus = zeros(self.propiedades)
        self.CalculateAverage()

    def CalculateAverage(self):
        total=0
        for i in range(self.propiedades):

            sum = 0
            for j in range(len(self.values)):

                sum += self.values[j][i]
                total+=self.values[j][i]

            self.plus[i] = sum

        for i in range(self.propiedades):

            self.plus[i] = self.plus[i]/total


m=MachineLearning() 
t=[[1,3,4,5],[1,1,1,1],[2,4,5,2],[12,41,34,12],[22,11,12,33],[123,123,421,422]]
o=[3,3,3,2,2,2]
m.Learn(t,o)
rs=m.Decide(t)
for i in rs:
    print(i)