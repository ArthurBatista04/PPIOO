class node(object):
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None
    

def lexer(expression):
    #Adicionamos um espaco entre os caracters não numerais
    cont = 0
    specialCaracters = ["+","-","*","/","(",")"]
    expressionToken = expression.replace("("," ( ")
    expressionToken = expressionToken.replace(")"," ) ")
    expressionToken = expressionToken.replace("+"," + ")
    expressionToken = expressionToken.replace("*"," * ")
    expressionToken = expressionToken.replace("/"," / ")
    expressionToken = expressionToken.replace("-"," - ")
    expressionToken = expressionToken.split() #separmos os elementos da expressão por espaço
    while cont<len(expressionToken): #diferenciamos os numeros negativos das operações de subtração
        if expressionToken[cont] == "-":
            if cont!=0:
                if expressionToken[cont+1].isdigit() and expressionToken[cont-1] in specialCaracters:
                    expressionToken[cont+1] = "-"+expressionToken[cont+1] 
                    del expressionToken[cont]
            else:
                expressionToken[cont+1] = "-"+expressionToken[cont+1]
                del expressionToken[cont]        
        cont+=1
    return expressionToken


def greaterPrecedence(operator1,operator2,operators): #verifica se o operator1 tem maior precedência se comparado ao 2
    if operator2 not in operators:return False #Verifica se o topo da pilha é uma operacao e nao "(" ou ")"
    elif operator2 == "/" or operator2 == "*": return True #Se o topo da fila contem operatores de de multiplicacao ou divisao, certamente terá maior precedência
    elif operator1 == "/" or operator1 == "*":return False    
    return True # Ambos os operadores têm mesma precedência



def paser(token):
    queue = []
    stack = []
    operators = ["+","-","*","/"]
    while token:
        element = token.pop(0)
        try:
            int(element) #verificamos se o elemento é um número
            queue.append(element)
        except:
            if element in operators: #verificamos se o elemento é um operador e se a pilha contem elementos
                while stack:
                    topOfStack = stack[-1]
                    if greaterPrecedence(element,topOfStack,operators):
                        queue.append(stack.pop()) #adicionamos o operator com maior precedencia da pilha à fila
                    else:
                        break    
                stack.append(element) #adicionamos o operator novo à pilha    
            elif element == "(":
                stack.append(element)
            elif element == ")":
                try:
                    while stack[-1] != "(": #verificamos se o topo da pilha contem "(" se não adicionamos os operadores à fila
                        queue.append(stack.pop())
                    stack.pop()
                except:
                    raise ValueError("Erro nos parenteses, verifica se para cada ')' há um '(' correspondente!")     
            else:
                raise ValueError(element,' é um valor inválido!')                                                  
    while stack: #Se existirem operadores ainda na pilha, movam-nos à fila
        queue.append(stack.pop()) 
    root = createTree(queue)      
    return root

def createTree(rpn):
    stack = []
    operators = ["+","-","*","/"]
    for element in rpn:
        newNode = node(element)
        if element in operators: #Quando encontrar um operator, os dois elementos no topo da pilha são seus filhos
            newNode.right = stack.pop()
            newNode.left = stack.pop()
        stack.append(newNode)
    return stack.pop() #retorna a raiz da árvore

def executeOperation(leftOperator,operation,rightOperator):
    if operation == "+": return(str(int(int(leftOperator) + int(rightOperator))))
    elif operation == "-": return(str(int(int(leftOperator) - int(rightOperator))))
    elif operation == "/": return(str(int(int(leftOperator) / int(rightOperator))))
    else: return(str(int(int(leftOperator) * int(rightOperator))))


def evalStep(root):
    operators = ["+","-","*","/"]
    while root.key in operators: 
        leftKey = root.left.key
        rightKey = root.right.key
        if leftKey not in operators and rightKey not in operators: #encontramos um nó operador que tem dois numeros como filhos
            root.key = executeOperation(leftKey,root.key,rightKey) #o novo valor do nó será o operação do operador com seus operandos
            root.left = None
            root.right = None
        elif leftKey in operators:#verificamos se o elemento da esquerda é um operador
            root = root.left
        else:
            root = root.right       

def resolveExpression(root):
    while root.right != None and root.right!= None: #Enquanto a arvore toda não for resolvida
        toString(root)
        print()
        evalStep(root)
    print(root.key)    

def toString(root): #Chamada in-order, esquerda, raiz e direita
    maiorPrecedencia = ["*","/"]
    menorPrecedencia = ["+","-"]
    if root != None:
        if root.key in maiorPrecedencia and root.left.key in menorPrecedencia and root.right.key in menorPrecedencia: #caso tenha um operador de multiplicacao ou divisao e seus ambos seus filhos são adicoes ou subitracao 
            print("( ", end = "")
            toString(root.left)
            print(")", end = " ")
            
            print(root.key, end = " ")
            
            print("( ",end = "")
            toString(root.right)
            print(")",end = " ")

        elif root.key in maiorPrecedencia and root.left.key in menorPrecedencia: #caso tenha um operador de mul ou div e seu filho esquerdo for uma operacao de add ou sub
            print("( ", end = "")
            toString(root.left)
            print(")", end = " ")
            
            print(root.key, end = " ")
            
            toString(root.right) 
            
        elif root.key in maiorPrecedencia and root.right.key in menorPrecedencia: #caso tenha um operador de mul ou div e seu filho direito for uma operacao de add ou sub
            toString(root.left)
            
            print(root.key, end = " ")
            
            print("( ",end = "")
            toString(root.right)
            print(")",end = " ")

        else: #Nao há parenteses 
            toString(root.left)
            print(root.key, end = " ")
            toString(root.right)

def main():
    expression = input()
    while expression:
        token = lexer(expression)
        root = paser(token)
        resolveExpression(root)
        print()
        expression = input()

if __name__ == "__main__":
    main()