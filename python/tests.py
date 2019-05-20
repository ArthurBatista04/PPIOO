from expressionTree import *
def testLexer():
    try:
        assert(lexer("(10 / 3 + 23) * (1 - 4)") == ["(","10","/","3","+","23",")","*","(","1","-","4",")"])
        assert(lexer("-714*4+(4+1)/21") == ["-714","*","4","+","(","4","+","1",")","/","21"])
        assert(lexer("41--12") == ["41","-","-12"])
        assert(lexer("(71     -    12)+41  *2") == ["(","71","-","12",")","+","41","*","2"])
        print("LEXER SEM ERRO")
    except:
        raise Exception('ERROR NO TESTE LEXER')

def testParser():
    try:
        assert(['10', '3', '/', '23', '+', '1', '4', '-', '*'] == parser(["(","10","/","3","+","23",")","*","(","1","-","4",")"]))
        assert(['-714', '4', '*', '4', '1', '+', '21', '/', '+'] == parser(["-714","*","4","+","(","4","+","1",")","/","21"]))
        assert(['41', '-12', '-'] == parser(["41","-","-12"]))
        assert(['71', '12', '-', '41', '2', '*', '+'] == parser(["(","71","-","12",")","+","41","*","2"]))
        print("PARSER SEM ERRO")
    except:
        raise Exception('ERROR NO PARSER')

def testResults():
    operator = ["+","-","*","/"]
    try:
        root = createTree(['10', '3', '/', '23', '+', '1', '4', '-', '*']) # (10 / 3 + 23) * (1 - 4)
        evalStep(root)
        assert(toString(root) == "(3 + 23) * (1 - 4)")
        evalStep(root)
        assert(toString(root) == "26 * (1 - 4)")
        evalStep(root)
        assert(toString(root) == "26 * -3")
        evalStep(root)
        assert(root.key == "-78") #Result

        root = createTree(['-714', '4', '*', '4', '1', '+', '21', '/', '+']) # -714*4+(4+1)/21
        evalStep(root)
        assert(toString(root) == "-2856 + (4 + 1) / 21")
        evalStep(root)
        assert(toString(root) == "-2856 + 5 / 21")
        evalStep(root)
        assert(toString(root) == "-2856 + 0")
        evalStep(root)
        assert(root.key == "-2856")

        root = createTree(['41', '-12', '-']) #41--12
        evalStep(root)
        assert(root.key == "53")

        root = createTree(['71', '12', '-', '41', '2', '*', '+']) #(71     -    12)+41  *2
        evalStep(root)
        assert(toString(root) == "59 + 41 * 2")
        evalStep(root)
        assert(toString(root) == "59 + 82")
        evalStep(root)
        assert(root.key == "141")

        print("RESULTADOS CORRETOS")
    except:
        raise Exception('ERROR NO RESULTADO FINAL')
   

def main():
    testLexer()
    testParser()
    testResults()

if __name__ == "__main__":
    main()