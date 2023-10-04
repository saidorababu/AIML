
def checkAllTrue(clauses, symbols, values):
    for clause in clauses:
        flag = False
        for literal in clause:
            if((literal>0 and literal in values.keys() and values[literal] == True) or (literal<0 and -literal in values.keys() and values[-literal] == False)):
                flag = True
                break
        if(flag == False):
            return False
    return True

def anyClauseIsFalse(clauses, symbols, values):
    for clause in clauses:
        flag = False
        for symbol in clause:
            if((symbol>0 and symbol not in values) or (symbol<0 and -symbol not in values) or (symbol>0 and values[symbol] == True) or (symbol<0 and values[-symbol] == False)):
                flag = True
                break
        if(flag == False):
            return True
    return False

def findPureSymbol(clauses,symbols,values):
    (ansSymbol,ansValue) = (None,None)
    for symbol in symbols:
        isPure = True
        flag = None
        for clause in clauses:
            for literal in clause:
                if(literal == symbol):
                    if(flag == -1):
                        isPure = False
                        break
                    flag = 1
                elif(literal == -symbol):
                    if(flag == 1):
                        isPure = False
                        break
                    flag = -1
            if(isPure == False):
                break
        if(isPure):
            if(flag == 1):
                (ansSymbol,ansValue) = (symbol,True)
            elif(flag == -1):
                (ansSymbol,ansValue) = (symbol,False)
    return (ansSymbol,ansValue)

def findUnitClause(clauses,symbols,values):
    for clause in clauses:
        cnt = 0
        for literal in clause:
            if(literal not in values.keys()):
                cnt+=1
            elif((literal<0 and values[-literal] == False) or (literal>0 and values[literal] == False)):
                continue
            if(cnt>1):
                break
        if(cnt == 1):
            return literal
    return None


def dpll(clauses , symbols, values):
    #Early Termination
    #If anyone literal in all the clauses is true or not 
    if(checkAllTrue(clauses,symbols,values)):
        return True
    # for a,b in values.items():
    #     print(a," : ",b)
    # print()
    #If anyone clause is false 
    if(anyClauseIsFalse(clauses,symbols,values)):
        return False
    
    #If find the  Pure Symbol is there or not
    (symbol,value) = findPureSymbol(clauses,symbols,values)
    if value!=None:
        values[symbol] = value
        return dpll(clauses,symbols,values)
    
    literal = findUnitClause(clauses,symbols, values)
    if literal != None:
        if(literal<0):
            values[-literal] = False
        else:
            values[literal] = True
        return dpll(clauses,symbols,values)
    
    # choose a literal
    literalReq = None
    valueReq = None
    for clause in clauses:
        for literal in clause:
            if(literal<0):
                if(-literal not in values.keys()):
                    literalReq = -literal
                    valueReq = False
                    break
            else:
                if(literal not in values.keys()):
                    literalReq = literal
                    valueReq = True
                    break
    if(literalReq == None):return False
    values[literalReq] = valueReq
    route1 = dpll(clauses,symbols,values)
    values[literalReq] = not valueReq
    route2 = dpll(clauses,symbols,values)
    return route1 or route2

clauses = [[1,2,3],[1,-2,3],[-1,2,3],[-1,-2,3],[1,2,-3],[1,-2,-3]]
symbols = [1,2,3]
if __name__ == "__main__":
    values = {}
    ans = dpll(clauses,symbols,values);
    print(ans)
    if(ans):
        print("The Given sentence is Satisfiable!")
        print("Solution:")
        for a,b in values.items():
            print(a," : ",b)
    else:
        print("The Given Sentence is not satisfiable")


