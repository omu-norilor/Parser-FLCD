from LR0_canonical_collection import CanonicalCollection

class LRTableEntry():
    def __init__(self, targetStates, actionType, reductionIndex):
        self.targetStates = targetStates
        self.actionType = actionType
        self.reductionIndex = reductionIndex

    def __str__(self):
        return str(self.targetStates) + " " + self.actionType + " " + str(self.reductionIndex)


# table entry = (target states, action type, reduction index)
# table entry in table = (state, table entry)

class LRTable():
    def __init__(self,  canonicalCollection):
        self.table=dict()
        self.generateTable(canonicalCollection)
        self.enhancedGrammar = canonicalCollection.enhancedGrammar
        self.startingState = canonicalCollection.startingState
        
    def __getitem__(self, state):
        return self.table[state]
    
    def __str__(self):
        string = ""
        for key in self.table.keys():
            string += str(key) + " " + str(self.table[key]) + "\n"
        return string
    
    def getTable(self):
        return self.table
    

    def getStartingState(self):
        return self.startingState
    
    
    def getEnhancedGrammar(self):
        return self.enhancedGrammar
    

    def generateTable(self, canonicalCollection):
        print(canonicalCollection.enhancedGrammar.startingSymbol)
        nrOfErrors = 0
        for state in canonicalCollection.states:
            lRitem = state.items[0]
            action = ""
            reductionIndex = -1

            if len(lRitem.beta)!=0:
                action = "SHIFT"
            
            elif lRitem.lhs == canonicalCollection.enhancedGrammar.startingSymbol and len(lRitem.beta)==0 and len(state.getItems()) == 1:
                action = "ACCEPT"
            
            elif len(state.getItems()) == 1 and len(lRitem.beta)==0:
                action = "REDUCE"
                reductionIndex = canonicalCollection.enhancedGrammar.getProductionIndex(lRitem.lhs, lRitem.alfa)
            
            else: #if not shift or accept or reduce, then it is an error (DUUH)
                action = "ERROR"
                nrOfErrors+=1
            

            lrTableEntry = LRTableEntry(canonicalCollection.stateTransitions.get(state), action, reductionIndex)
            self.table[state] = lrTableEntry
        
        print("Number of conflicts:" + str(nrOfErrors))
    
