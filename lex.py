import re

s = input("Enter filename : ")
f = open(s, 'r')
text = f.read()

simbolos = ['!', '@', '#', '$', '%', '&', '^', '*']
oparadores = ['+', '-', '*', '/', '=', '+=', '-=', '==', '<', '>', '<=', '>=']

PalavrasReservadas = ['auto','break', 'case', 'char', 'const', 'continue', 'default', 'do', 
			'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 
			'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 
			'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
delimitadores = [' ', '	', '.', ',', '\n', ';', '(', ')', '<', '>', '{', '}', '[', ']']


in_PalavrasReservadas = []
in_spl_Simbolos= []
in_oparadores = []
in_delimitadores = []
in_identificadores = []
in_constantes = []

tokens = []
isString = False
isWord = False
isCmt = 0
token = ''

for i in text:
	if i == '/':
		isCmt = isCmt+1

	elif isCmt == 2:
		if i == '\n':
			token = ''
			isCmt = 0
	
	elif i == '"' or i == "'":
		if isString:
			tokens.append(token)
			token = ''
		isString = not isString

	elif isString:
		token = token+i
    
	elif i in simbolos:
		tokens.append(i)
           
	elif i.isalnum() and not isWord:
		isWord = True
		token = i
    
	elif (i in delimitadores) or (i in oparadores):
		if token:
			tokens.append(token)
			token = ''
        
		if not (i==' ' or i=='\n' or i=='	'):
			tokens.append(i)

	elif isWord:
		token = token+i


for token in tokens:
	if token in simbolos:
		in_spl_Simbolos.append(token)

	elif token in oparadores:
		in_oparadores.append(token)

	elif token in PalavrasReservadas:
		in_PalavrasReservadas.append(token)
				
	elif re.search("^[_a-zA-Z][_a-zA-Z0-9]*$",token):
		in_identificadores.append(token)
		
	elif token in delimitadores:
		in_delimitadores.append(token)
		
	else:
		in_constantes.append(token)
	
						
print("NUMERO DE TOKENS  = ", len(tokens))   
print("\nNUMERO DE PALAVRAS RESERVADAS  = ",len(in_PalavrasReservadas))
print(in_PalavrasReservadas);
print("\nNNUMERO DE SIMBOLOS ESPECIAIS = ",len(in_spl_Simbolos))
print(in_spl_Simbolos);
print("\nNUMERO DE OPERADORES = ",len(in_oparadores))
print(in_oparadores);
print("\nNUMERO DE IDENTIFICADORES  = ",len(in_identificadores))
print(in_identificadores);
print("\nNUMERO DE TOKENS  = ",len(in_constantes))
print(in_constantes);
print("\nNUMERO DE DELIMITADORES = ",len(in_delimitadores))
print(in_delimitadores);
f.close()   
