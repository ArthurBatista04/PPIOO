class Tree(object):

    def lexer(self,expression):
        expression = expression.replace("(","( ")
        expression = expression.replace(")"," )")
        expressionToken = expression.split()        
        return expressionToken
    
    
    def greaterPrecedence(self,operator1,operator2,operators): #verifica se o operator1 tem maior precedência se comparado ao 2
        if operator2 not in operators: #Verifica se o topo da pilha é uma operacao e nao "(" ou ")"
            return False
        elif operator2 == "/" or operator2 == "*": #Se o topo da fila contem operatores de de multiplicacao ou divisao, certamente terá maior precedência
            return True
        elif operator1 == "/" or operator1 == "*":   
            return False    
        return True # Ambos os operadores têm mesma precedência
    


    def paser(self,token):
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
                        if self.greaterPrecedence(element,topOfStack,operators):
                            queue.append(stack.pop()) #adicionamos o operator com maior precedencia da pilha à fila
                        else:
                            break    
                    stack.append(element) #adicionamos o operator novo à pilha    
                elif element == "(":
                    stack.append(element)
                elif element == ")":
                    while stack[-1] != "(": #verificamos se o topo da pilha contem "(" se não adicionamos os operadores à fila
                        queue.append(stack.pop())
                    stack.pop()        
                else:
                    raise ValueError(element,' é um valor inválido!')                                       
        while stack: #Se existirem operadores ainda na pilha, mova-os à fila
            queue.append(stack.pop()) 
              
        return queue

    def evalStep(self,rpn):
        operators = ["+","-","*","/"]
        stack = []
        while rpn:
            element = rpn.pop(0)
            if element in operators:
                operand = stack.pop()
                operand2 = stack.pop()
                exec('result = '+"str("+operand+element+operand2+")", locals(), globals())
                stack.append(result)
            else:
                stack.append(element)    
        return stack.pop()
def main():
    expression = input()
    while expression:
        postFixExpression = []
        tree = Tree()
        token = tree.lexer(expression)
        rpn = tree.paser(token)
        print(tree.evalStep(rpn))
        # tree.postFix(rpnTree,postFixExpression)
        # print(postFixExpression)

        expression = input()

if __name__ == "__main__":
    main()