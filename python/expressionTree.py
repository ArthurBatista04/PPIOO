def lexer(expression):
    expressionToken = expression.replace("(","( ") #incluimos um espaco entre ( e numero
    expressionToken = expressionToken.replace(")"," )")#incluimos um espaco entre num e )
    expressionToken = expressionToken.split() #separmos os elementos da expressão por espaço
    return expressionToken


def greaterPrecedence(operator1,operator2,operators): #verifica se o operator1 tem maior precedência se comparado ao 2
    if operator2 not in operators: #Verifica se o topo da pilha é uma operacao e nao "(" ou ")"
        return False
    elif operator2 == "/" or operator2 == "*": #Se o topo da fila contem operatores de de multiplicacao ou divisao, certamente terá maior precedência
        return True
    elif operator1 == "/" or operator1 == "*":   
        return False    
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
    while stack: #Se existirem operadores ainda na pilha, mova-os à fila
        queue.append(stack.pop()) 
            
    return queue

def evalStep(rpn,expression):
    operators = ["+","-","*","/"]
    stack = []
    print(expression)
    while rpn:
        element = rpn.pop(0)
        if element in operators: #se houver um operador, fazemos a operacao deste com os dois operandos no topo da pilha
            operand = stack.pop()
            operand2 = stack.pop()
            exec('result = '+"int("+operand2+element+operand+")", locals(), globals()) #salva na variável result a operacao
            stack.append(str(result))
            expression = toString(element,operand,operand2,str(result),expression)
            print(expression)
        else:
            stack.append(element)    

def toString(operator,operand,operand2,result,expression):
    subExpression = operand2+" "+operator+" "+operand 
    expression = expression.replace(subExpression, result) #substituimos o os dois operandos e a operacao pelo seu resultado
    if "("+result+")" in expression: 
        expression = expression.replace("("+result+")",result)#se existir apenas o resultado entre parenteses, retiramo-nos
    return expression

def main():
    expression = input()
    while expression:
        token = lexer(expression)
        rpn = paser(token)
        evalStep(rpn,expression)
        print("\n")
        expression = input()

if __name__ == "__main__":
    main()