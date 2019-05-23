use std::collections::VecDeque;
use std::io::{self, BufRead};
use std::convert::AsRef;

#[derive(Debug,PartialEq,Clone)]
//Estrutura de nó para a árvore de expressões
struct node {
	key: String,
	left : Option<Box<node>>,
	right : Option<Box<node>>,
}

//A função lexer transforma a expressão de entrada em um vetor de tokens
fn lexer(expression: &String) -> VecDeque<String>{
	let mut expression_token: VecDeque<String> = VecDeque::new();
	let mut aux: Vec<char> = Vec::new();
	let special_characters = vec!['*','/','+','-','(',')']; //caracteres especiais
	let special_characters_verificate = vec!['*','/','+','-','('];
	let mut count = 0;

	//coloca cada elemento (números e caracteres especiais) em uma posição do vetor
	for element in expression.chars() {
		if element.is_digit(10) || special_characters.contains(&element) {
			aux.push(element);    
		}
	}

	//tratamento para o caso de a expressão começar com um número negativo
	if aux[count] == '-'{ 
		let mut negative_number: String = "-".to_string();
		count = count + 1;
		// enquanto tiver algarismos, constrói o número negativo
		while aux[count].is_digit(10) { 
			negative_number.push(aux[count]);
			count = count + 1;
			if count == aux.len() {
				break;
			}
		}
		//adiciona ao vetor de tokens o número negativo inicial
		expression_token.push_back(negative_number);
	}

	//constrói o restante do vetor de tokens
	while count < aux.len() { 
		let mut num: String = "".to_string();
		//forma os valores numéricos positivos
		while aux[count].is_digit(10) {
			num.push(aux[count]);
			count = count + 1;
			if count == aux.len() {
				break;
			}
		}
		//se um número foi formado, adiciona no vetor
		if num != "".to_string() { 
			expression_token.push_back(num);
		}else{
			//tratamento dos números negativos
			if aux[count] == '-' && aux[count + 1].is_digit(10) && special_characters_verificate.contains(&aux[count-1]) { 
				let mut negative_number: String = "-".to_string();
				count = count + 1;
				//forma os valores numéricos negativos
				while aux[count].is_digit(10) { 
					negative_number.push(aux[count]);
					count = count + 1;
					if count == aux.len() {
						break;
					}
				}
				//se um número foi formado, adiciona no vetor
				expression_token.push_back(negative_number);
			// caso seja um caracter especial, adiciona no vetor
			}else{ 
				expression_token.push_back(aux[count].to_string());
				count = count + 1;
			}
		}
	}
	return expression_token
}   

//esta função verifica a precedência de operadores
fn greater_or_equal_precedence(operator1: &String, operator2: &String, operators: &Vec<String>) -> bool {
	//retorna falso se o topo da pilha for '('
	if !operators.contains(&operator2) { 
		return false
	//retorna verdadeiro se o topo da pilha tiver maior precedência
	} else if operator2 == &'/'.to_string() || operator2 == &'*'.to_string() { 
		return true 
	//retorna flaso se o elemento da fila tiver maior precedência
	} else if operator1 == &'/'.to_string() || operator1 == &'*'.to_string() { 
		return false
	}
	//retorna verdadeiro se ambos tiverem a mesma precedência
	return true 
}

//esta função transforma o vetor de tokens em um vetor com a reverse polish notation
fn parser(tokens: &mut VecDeque<String>) -> VecDeque<String> {
	let mut stack: VecDeque<String> = VecDeque::new(); //pilha de operadores
	let mut queue: VecDeque<String> = VecDeque::new(); //fila de saída
	let operators = vec![String::from("*"),String::from("/"),String::from("+"),String::from("-")]; // contém os operadores
	let mut element: String;
	//percorre todo o vetor de tokens
	while !tokens.is_empty() { 
		//primeiro elemento do vetor de tokens
		element = tokens.pop_front().unwrap();
		//se o primeiro elemento é um número, adiciona na fila de saída
		if element.parse::<i64>().is_ok() { 
			queue.push_back(element);
		//se o elemento for um operator, verifica as precedências
		}else if operators.contains(&element) {
				//enquanto houver elementos no topo da pilha, verifica pecedência
				while !stack.is_empty() { 
					let top_of_stack = &stack[stack.len()-1];
					//se o elemento do topo da tiver maior precedência, adiciona-o na fila de saída
					if greater_or_equal_precedence(&element, &top_of_stack, &operators) {
						queue.push_back(stack.pop_back().unwrap()); 
					} else {
						break;
					}
				}
				stack.push_back(element);
		//coloca o '(' na pilha  
		} else if element == '('.to_string() {
				stack.push_back(element);
		//se for um ')', adicionamos os operadores à fila até encontrar o '('
		} else if element == ')'.to_string() { 
				while stack[stack.len()-1] != '('.to_string(){ 
					queue.push_back(stack.pop_back().unwrap());
				}
				stack.pop_back();
		// se for um caracter inválido
		} else { 
				panic!("Caracter inválido: {}", element);
		}
	}
	while !stack.is_empty() { // enquanto existirem operadores na pilha
		queue.push_back(stack.pop_back().unwrap()); // adicionamos os operadores no topo no final da final
	}

	return queue;
}

//recebe a expressão em reverse polish notation e monta a arvore, retornando o nó raiz 
fn create_tree(rpn: &mut VecDeque<String>) -> node{
	let mut stack: VecDeque<node> = VecDeque::new();
	let operators = vec![String::from("*"),String::from("/"),String::from("+"),String::from("-")];
	let mut element;
	let mut newnode;
	//percorre o vetor com a rpn
	while ! rpn.is_empty(){
		element = rpn.pop_front();
		newnode = node {key : element.clone().unwrap(), left : None, right: None};
		//se for um operador, coloca ele e seus filhos na arvore
		if operators.contains(&element.unwrap()){
			newnode.right = Some(Box::new(stack.pop_back().unwrap()));
			newnode.left = Some(Box::new(stack.pop_back().unwrap()));
		}
		stack.push_back(newnode);
	}
	//retorna o topo da pilha
	stack.pop_back().unwrap()
}

//percorre recursivamente a arvore e imprime na tela a expressão
fn to_string(root: &node) {
	let maior_precedencia = vec![String::from("*"),String::from("/")];
	let menor_precedencia = vec![String::from("+"),String::from("-")];
    match root {
        node {
            left: None,
            right: None,
            ..
        } => {
			print!("{}",root.key);
        }
        node {
            left: Some(left),
            right: Some(right),
            ..
        } => {
			if maior_precedencia.contains(&root.key) && menor_precedencia.contains(&Some(left).unwrap().key) && menor_precedencia.contains(&Some(right).unwrap().key){
				print!("(");
				to_string(&left);
				print!(")");
				print!(" {} ", root.key);
				print!("(");
				to_string(&right);
				print!(")");
			} else if maior_precedencia.contains(&root.key) && menor_precedencia.contains(&Some(left).unwrap().key){
				print!("(");
				to_string(&left);
				print!(")");
				print!(" {} ", root.key);
				to_string(&right);
			} else if maior_precedencia.contains(&root.key) && menor_precedencia.contains(&Some(right).unwrap().key){
				to_string(&left);
				print!(" {} ", root.key);
				print!("(");
				to_string(&right);
				print!(")");
			} else {
				to_string(&left);
				print!(" {} ", root.key);
				to_string(&right);
			}
        }
		_ => {}
    }
}

//recebe a arvore e realiza uma operação 
fn eval_step(root: &mut node) {
	let maior_precedencia = vec![String::from("*"),String::from("/")];
	let menor_precedencia = vec![String::from("+"),String::from("-")];
		match root {
			node {
				left: Some(left),
				right: Some(right),
				key,
				..
			} => {
				//se os dois filhos forem números, ele realiza a operação 
				if left.key.parse::<i64>().is_ok() && right.key.parse::<i64>().is_ok(){
					root.key = execute_operation(&mut left.key,&mut right.key, key.to_string());
					root.left = None;
					root.right = None;
				//caso contrário, ele verifica se o filho da esquerda é um operador, se for, ele chama a função recursivamente passando-o
				} else if maior_precedencia.contains(&left.key) || menor_precedencia.contains(&left.key){
					eval_step(left);
				} else {
					eval_step(right);
				}
			}
			_ => {}
		}
}

//recebe a raiz da arvore e resolve a expressão
fn resolve_expression( root: &mut node){
	//se o filho da esquerda e direita fore none, significa que todas as operações foram realizadas 
	while root.right != None && root.left != None {
		to_string(&root);
		println!();
		eval_step(root);
	}
	print!("{}",root.key);
	println!();
}

//recebe o operador e os operandos e realiza a operação
fn execute_operation(operator1: &mut String,operator2: &mut String,operation: String) -> String{
	let result;
	match operation.as_ref() {
		"+" => {
			result = operator1.parse::<i64>().unwrap() + operator2.parse::<i64>().unwrap();
			result.to_string()
		}
		"-" => {
			result = operator1.parse::<i64>().unwrap() - operator2.parse::<i64>().unwrap();
			result.to_string()
		}
		"*" => {
			result = operator1.parse::<i64>().unwrap() * operator2.parse::<i64>().unwrap();
			result.to_string()
		}
		"/" => {
			result = operator1.parse::<i64>().unwrap() / operator2.parse::<i64>().unwrap();
			result.to_string()
		}
		_ => {
			panic!("Error".to_string());
		}
	}
}


fn main() {
		let mut expression: String = String::new(); //expressão de entrada
		let mut token: VecDeque<String> = VecDeque::new(); //vetor de tokens
		let mut root; //raiz da arvore a ser construida
		let stdin = io::stdin();
		stdin.lock().read_line(&mut expression).expect("Não foi possível ler a expressão.");
		
		//enquanto há expressões, realiza os passos para resolvê-las
		while expression.len() > 0 && expression != "\n".to_string() { // enquanto tiver input
				expression = expression.trim().to_string(); // transformar input em string
				token = lexer(&expression); //constroi os tokens
				let mut rpn = parser(&mut token); //constroi a reverse polish notation
				root = create_tree(&mut rpn); // raiz da ávore
				resolve_expression(&mut root); //resolve a expressão
				expression.clear(); //limpa a expressão para uma proxima entrada
				println!();
				stdin.lock().read_line(&mut expression).expect("Não foi possível ler a expressão.");	
		 }
    
}


	fn to_s(vec_aux: Vec<&str>) -> Vec<String> {
		let mut vec_ans: Vec<String> = vec![];
		for i in vec_aux{
			vec_ans.push(i.to_string());
		}
		vec_ans
	}
    #[test]
    fn lexer_test() {
        assert_eq!(lexer(&String::from("(10 / 3 + 23) * (1 - 4)")), vec!["(","10","/","3","+","23",")","*","(","1","-","4",")"]);
        assert_eq!(lexer(&String::from("-714*4+(4+1)/21")),vec!("-714","*","4","+","(","4","+","1",")","/","21"));
        assert_eq!(lexer(&String::from("41--12")),vec!("41","-","-12"));
        assert_eq!(lexer(&String::from("(71     -    12)+41  *2")),vec!("(","71","-","12",")","+","41","*","2"));
    }
	#[test]
    fn parser_test(){
		assert_eq!(parser(&mut VecDeque::from(to_s(vec!["(","10","/","3","+","23",")","*","(","1","-","4",")"]))),to_s(vec!["10", "3", "/", "23", "+", "1", "4", "-", "*"]));
        assert_eq!(parser(&mut VecDeque::from(to_s(vec!["-714","*","4","+","(","4","+","1",")","/","21"]))),to_s(vec!["-714", "4", "*", "4", "1", "+", "21", "/","+"]));
        assert_eq!(parser(&mut VecDeque::from(to_s(vec!["41","-","-12"]))), to_s(vec!["41", "-12", "-"]));
        assert_eq!(parser(&mut VecDeque::from(to_s(vec!["(","71","-","12",")","+","41","*","2"]))), to_s(vec!["71", "12", "-", "41", "2", "*", "+"]));
     }
	 #[test]
	 fn result_test(){
		lexer(&String::from("(10 / 3 + 23) * (1 - 4)"));
		let mut rpn = parser(&mut VecDeque::from(to_s(vec!["(","10","/","3","+","23",")","*","(","1","-","4",")"])));
		let mut root = create_tree(&mut rpn);
		while root.right != None && root.left != None {
			eval_step(&mut root);
		}
		assert_eq!(root.key, "-78".to_string());

		lexer(&String::from("-714*4+(4+1)/21"));
		rpn = parser(&mut VecDeque::from(to_s(vec!["-714","*","4","+","(","4","+","1",")","/","21"])));
		root = create_tree(&mut rpn);
		while root.right != None && root.left != None {
			eval_step(&mut root);
		}
		assert_eq!(root.key, "-2856".to_string());

		lexer(&String::from("41--12"));
		rpn = parser(&mut VecDeque::from(to_s(vec!["41","-","-12"])));
		root = create_tree(&mut rpn);
		while root.right != None && root.left != None {
			eval_step(&mut root);
		}
		assert_eq!(root.key, "53".to_string());

		lexer(&String::from("(71     -    12)+41  *2"));
		rpn = parser(&mut VecDeque::from(to_s(vec!["(","71","-","12",")","+","41","*","2"])));
		root = create_tree(&mut rpn);
		while root.right != None && root.left != None {
			eval_step(&mut root);
		}
		assert_eq!(root.key, "141".to_string());
	 }