class Tree(object):
    def __init__(self):
        nodes = None

    def lexer(self,expression):
        expressionToken = []
        expression = expression.replace(" ","") # Remoção dos espaços
        expressionToken.extend(expression)
        return expressionToken
    
    
    def greaterPrecedence(self,operator1,operator2): #verifica se o operator1 tem maior precedência se comparado ao 2
        if operator1 =="+" and operator2 == "*": return False
        elif operator1 =="+" and operator2 == "/": return False 
        elif operator1 =="-" and operator2 == "*": return False
        elif operator1 =="-" and operator2 == "/": return False    
        return True #Neste caso, comparamos (+ com -) ou (* com /)
    
    def paser(self,token):
        queue = []
        stack = []
        while not token:
            element = token.pop(0)
            try:
                element = int(element) #verificamos se o elemento é um número
                queue.append(element)
            except:
                operators = ["+","-","*","/"]
                if element in operators: #verificamos se o elemento é um operador
                    inversedSize = reversed(range(len(stack)-1)) 
                    for i in inversedSize: #percorremos o vetor de trás p/ frente (pilha)
                        if self.greaterPrecedence(stack[i],element):
                            queue.append(stack[i]) #adicionamos o operator com maior precedencia da pilha à fila
                            stack.remove(stack[i])
                            stack.append(element) #adicionamos o operator novo à fila
                        break    
                elif element == "(":
                    pass
                else element == ")"
                    pass

class node(object):
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None
    
    def lexer(self):
        



def main():
    expression = "(2 + 5) - (3 + 7)"
    


# if __name__ == "__main__":
#     main()