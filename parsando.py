from grammar import Grammar

def main():
    filename = "rules\\grammar.txt" # Syntax.in from GitHub 1b
    grammar = Grammar(filename)
    grammar.printProductions()
    print()
    grammar.printProductionsNonTerminal("term")
    print()
    grammar.printNonTerminals()
    print()
    grammar.printTerminals()
    print()
    print(grammar.isCFG)
    #TODO: LR(0) Parser
    


if __name__ == "__main__":
    main()