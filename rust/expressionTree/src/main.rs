use std::collections::VecDeque;
use std::io::{self, BufRead};

fn lexer(expression: &String) -> VecDeque<String>{
	let mut expression_token: VecDeque<String> = VecDeque::new();
	let mut aux: Vec<char> = Vec::new();
	let special_characters = vec!['*','/','+','-','(',')'];
	let mut count = 0;
	let mut num: String = "".to_string();
	for element in expression.chars() { //retira os espaços da string expression
		if element.is_digit(10) || special_characters.contains(&element) {
			aux.push(element);    
		}
	}

	if aux[0] == '-' && aux[1].is_digit(10) { //tratamento para o caso de começar com um número negativo
		let mut negative_number: String = "-".to_string();
		negative_number.push(aux[1]);
		expression_token.push_back(negative_number);
		count = count + 2;
	}

	while count < aux.len() { //como no laço anterior ele vai salvar o numero como [1,1,1, ... ], esse laço vai "juntar" esse número como [111, .... ] 
		while aux[count].is_digit(10) {
			num.push(aux[count]);
			count = count + 1;
			if count == aux.len() {
				break;
			}
		}
		if num != "".to_string() {
			expression_token.push_back(num);
			num = "".to_string();
		}else{
			if aux[count] == '-' && aux[count + 1].is_digit(10) && special_characters.contains(&aux[count-1]) { //tratamento dos números negativos
				let mut negative_number: String = "-".to_string();
				negative_number.push(aux[count+1]);
				expression_token.push_back(negative_number);
				count = count + 1;
			}  
			expression_token.push_back(aux[count].to_string());
			count = count + 1;
		}
	}
	return expression_token
}   

fn greater_or_equal_precedence(operator1: &String, operator2: &String, operators: &Vec<String>) -> bool {
	if !operators.contains(&operator2) {
		println!("operador");
		return false
	} else if operator2 == &'/'.to_string() || operator2 == &'*'.to_string() {
		return true 
	} else if operator1 == &'/'.to_string() || operator1 == &'*'.to_string() {
		return false
	} 
	return true
}

fn parser(tokens: &mut VecDeque<String>) -> VecDeque<String> {
	let mut stack: VecDeque<String> = VecDeque::new();
	let mut queue: VecDeque<String> = VecDeque::new();
	let operators = vec![String::from("*"),String::from("/"),String::from("+"),String::from("-")];
	let mut element: String;
	while !tokens.is_empty() {
		element = tokens.pop_front().unwrap();
		if element.parse::<f64>().is_ok() {
			queue.push_back(element);
		} else if operators.contains(&element) {
				while !stack.is_empty() {
					let top_of_stack = &stack[stack.len()-1];
					if greater_or_equal_precedence(&element, &top_of_stack, &operators) {
						queue.push_back(stack.pop_back().unwrap());
					} else {
						break;
					}
				}
				stack.push_back(element);
		} else if element == '('.to_string() {
				stack.push_back(element);
		} else if element == ')'.to_string() {
				while stack[stack.len()-1] != '('.to_string(){
					queue.push_back(stack.pop_back().unwrap());
				}
				stack.pop_back();
		} else {
				panic!("Caracter inválido: {}", element);
		}
	}
	while !stack.is_empty() {
		queue.push_back(stack.pop_back().unwrap());
	}
	return queue;
}


fn main() {
		let mut expression: String = String::new();
		let mut token: VecDeque<String> = VecDeque::new();

		let stdin = io::stdin();
		stdin.lock().read_line(&mut expression).expect("FOI");
		while expression.len() > 0 {
				expression = expression.trim().to_string();
				token = lexer(&expression);
				for i in &token {
							print!("{} ", i);
				} 
				println!();
				println!();
				let rpn = parser(&mut token);

				for i in rpn {
					print!("{} ", i);
				} 
				expression.clear();
				token.clear();
				stdin.lock().read_line(&mut expression).expect("FOI");
						
		}
    
}
