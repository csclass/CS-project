#!/usr/bin/python3
#System of linear equations solver
class x:#for the representation of a polynomial
    def __init__(self,coefficients):
        self.coefficients=coefficients

        #also store it in a dictionary, so we can look up the coefficients for each x^n term
        self.dic=dict()
        for i in range(len(self.coefficients)):
            self.dic["x"+str(i)]=coefficients[i]
    def __str__(self):
        p=str()
        if len(self.coefficients)==1:#check for the constant polynomial
            return self.coefficients[0]
        elif len(self.coefficients)>1:#x's are involved
            p+=str(self.coefficients[0])#add the constant to output
            for i in range(1,len(self.coefficients)):#then for each extra coefficient, add x^i
                if i==1:
                    p+="+"+str(self.coefficients[i])+"x"#we don't need to print x^1 when x works
                elif self.coefficients[i] != 0:
                    p+="+"+str(self.coefficients[i])+"x^"+str(i)# add all x^n's into our output string
        return p
def get(): #gets user input and creates a polynomial
        pass
def solve(l):#input needs to be a list of n class x objects
        for i in l:# checks if everythng is of class x
                if not isinstance(i,x):
                        print('Equations must be polynomial objects')
                        return None
        print("Solving {"+str(x1)+" , "+str(x2)+"} for (x,y)...")
        print(x2)
x1=x([1,2,0,5,10])
x2=x([1,50])
#x2=5
solve([x1,x2])
