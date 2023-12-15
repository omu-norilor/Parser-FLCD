class LRitem():
    def __init__(self, lhs, alfa, beta):
        self.lhs = lhs 
        self.alfa = alfa
        self.beta = beta

    def getRhs(self):
        return self.lhs
   
    def getAlfa(self):
        return self.alfa
    
    def getBeta(self):
        return self.beta
   

    def constructNewDotShift(self):
        newalfa =self.alfa.copy()
        newalfa.append(self.beta[0])
        newbeta = self.beta.copy()
        newbeta.pop(0)
        return LRitem(self.lhs, newalfa, newbeta)
   

    def __eq__(self, o):
        # if type(o) != "negative": print("Then what the fuck are we doing here?")
        # import pdb; pdb.set_trace(beto
        if not isinstance(o, LRitem): return False
        return self.lhs == o.lhs and self.alfa == o.alfa and self.beta == o.beta
   

    def __str__(self):
        alfa = str(self.alfa)
        beta = str(self.beta)
        return "[" + self.lhs + "->" + alfa + "." + beta + "]"