from LR0_item import LRitem
from State import State
class LR0():
    
    def __init__(self, enhancedGrammar):
        self.enhancedGrammar = enhancedGrammar
    
    def goTo(self, s, symbol):
        result = list()
        for item in s.getItems(): 
            if len(item.getBeta())==0: 
                continue

            if (item.getBeta()[0]==symbol):
                result.append(item.constructNewDotShift())
        return s.closure(result, self.enhancedGrammar)

    def canonicalCollection(self, enhancedGrammar):
        states = list()
        statesCopy=list()
        # s0 = closure({[S'->.S]})

        # build s0 "manually" 
        s0 =State(list())
        Sprime = enhancedGrammar.startingSymbol
        Sproductions = enhancedGrammar.getProductions().get(Sprime)
        
        for production in Sproductions:
            s0.addItem(LRitem(Sprime, list(), production))
        s0.setItems(s0.closure(s0.getItems(), enhancedGrammar))
        states.append(s0)
        # for each state s in states
        changed = True
        while changed:
            changed = False
            statesCopy = states.copy()
            for s in states:
                # for each grammar symbol X
                for X in enhancedGrammar.getGrammarSymbols():
                    # if goto(s, X) is not empty and not in states
                    gotoResult = self.goTo(s, X)
                    if len(gotoResult)!=0 and State(gotoResult) not in statesCopy:
                        # add goto(s, X) to states
                        newState = State(gotoResult)
                        statesCopy.append(newState)
                        changed = True
                    
            states = statesCopy.copy()
        return states

    def printStates(self, states):
        i = 0
        for s in states: 
            stringo = "s"+str(i)+": "
            for item in s.getItems():
                stringo += str(item) + ", "
            print(stringo[:-2])
            i+=1