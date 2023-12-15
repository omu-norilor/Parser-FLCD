from grammar import Grammar
from LR0_item import LRitem
from LR0_parser import LR0
import random
def GrammarPrints(grammar):
    print("\nGrammar from file: ", grammar.filename)
    print("\nProductions:")
    grammar.printProductions()
    print("\nNon-terminals:")
    grammar.printNonTerminals()
    print("\nTerminals:")
    grammar.printTerminals()
    print("\nIs CFG?")
    if grammar.isCFG: print("Yes it is!\n")
    else: print("Nope, it's not.\n")

def testGrammar():
    # read choices from user
    choice = input("Enter \n- 1 for g1.txt, \n- 2 for g2.txt: ")
    annoyance= ["You're annoying me. ", "You're really annoying me. ", "You're really really annoying me. ", "Please stop. ", "I'm going to stop responding if you don't stop. ", "You wanted it"]
    while choice != "1" and choice != "2":
        rand = random.randint(0, len(annoyance)-1)
        print(annoyance[rand])
        if rand == len(annoyance)-1: return
        choice = input("Enter 1 for g1.txt, 2 for g2.txt: ")

    if choice == "1":
        filename = "rules\\g1.txt" # Syntax.in from course
        grammar = Grammar(filename)
        GrammarPrints(grammar)

    if choice == "2":
        filename = "rules\\g2.txt" # Syntax.in from GitHub 1b
        grammar = Grammar(filename)
        GrammarPrints(grammar)
    
    print("That's all folks!")

def testParser():
    # read choices from user
    choice = input("Enter \n- 1 for g1.txt, \n- 2 for g2.txt: ")
    annoyance= ["You're annoying me. ", "You're really annoying me. ", "You're really really annoying me. ", "Please stop. ", "I'm going to stop responding if you don't stop. ", "You wanted it"]
    while choice != "1" and choice != "2":
        rand = random.randint(0, len(annoyance)-1)
        print(annoyance[rand])
        if rand == len(annoyance)-1: return
        choice = input("Enter 1 for g1.txt, 2 for g2.txt: ")

    if choice == "1":
        filename = "rules\\g1.txt" # Syntax.in from course
        grammar = Grammar(filename)
        lr0 = LR0(grammar)
        states = lr0.canonicalCollection(grammar)
        lr0.printStates(states)

    if choice == "2":
        filename = "rules\\g2.txt" # Syntax.in from GitHub 1b
        grammar = Grammar(filename)
        lr0 = LR0(grammar)
        states = lr0.canonicalCollection(grammar)
        lr0.printStates(states)
    
    print("That's all folks!")


if __name__ == "__main__":
    testParser()
    # testGrammar()