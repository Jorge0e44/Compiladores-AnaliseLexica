from os import altsep
import re

s = input("Enter filename : ")
f = open(s, 'r')
text = f.read()

simbolos = ['@', '#', '$', '&', '^']
operadores_logicos = ['&&','||','!']##AND ORD NOT
operadores_aritmeticos=['+','-','*','/','%']#VERIFICAR A DIVISÃO PQ TÁ BUGANDO
operadores_relacionais = [ '+=','!=','-=', '==', '<', '>', '<=', '>=','<>']#VERIFICAR QUANDO O USO FOR DO TIPO <STDIO.H> POIS O <> ELE IDENTIFICA SOMENTE COMO OPERADOR RELACIONAL
tipo_variaveis=['int','float','long','double','short','char','long','unsigned']
simb_atribuicao = ['=']
loops = ['for','while'] #verificar se o do entra nesse caso
condicionais = ['if','else']
digitos = ['0','1','2','3','4','5','6','7','8','9']
PalavrasReservadas = ['auto','break', 'case', 'const', 'continue', 'default', 'do', 
			'enum', 'extern', 'goto','define',
			  'register', 'return', 'signed', 'sizeof', 'static','include','main'
			'struct', 'switch', 'typedef', 'union', 'void', 'volatile']
delimitadores = [' ', '	', '.', ',', '\n', ';', '(', ')', '<', '>', '{', '}', '[', ']']


in_PalavrasReservadas = []
in_spl_Simbolos= []
in_operadores_logicos=[]
in_operadores_aritmeticos= []
in_operadores_relacionais = []
in_tipo_variaveis = []
in_simb_atribuicao = []
in_tipo_constantes = []
in_loops = []
in_condicionais = []
in_digitos = []
in_delimitadores = []
in_identificadores = []
in_entremaiormenor = []
in_constantes = []

tokens = []
isString = False
isWord = False
isCmt = 0
token = ''

for i in text:
	if i == '/': #FAZ O TESTE PARA VERIFICAR SE É UM COMENTÁRIO
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
    
	elif (i in delimitadores) or (i in operadores_aritmeticos) or (i in operadores_logicos) or (i in operadores_relacionais) or (i in loops) or (i in condicionais):
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

	elif token in operadores_relacionais:
		in_operadores_relacionais.append(token)
	
	elif token in operadores_aritmeticos:
		in_operadores_aritmeticos.append(token)
	
	elif token in operadores_logicos:
		in_operadores_logicos.append(token)

	elif token in tipo_variaveis:
		in_tipo_variaveis.append(token)
	
	elif token in simb_atribuicao:
		in_simb_atribuicao.append(token)
	
	elif token in loops:
		in_loops.append(token)
	elif token in condicionais:
		in_condicionais.append(token)
	
	elif token in digitos:
		in_digitos.append(token)
	
	elif token in PalavrasReservadas:
		in_PalavrasReservadas.append(token)

	#O USO DO [] CORRESPONDE QUE QUEREMOS PEGAR UM CONJUNTO DE CARACTERES			
	elif re.search("^[_a-zA-Z][_a-zA-Z]*$",token):  
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

print("\nNUMERO DE OPERADORES LÓGICOS  = ",len(in_operadores_logicos))
print(in_operadores_logicos);

print("\nNUMERO DE OPERADORES ARITMÉTICOS  = ",len(in_operadores_aritmeticos))
print(in_operadores_aritmeticos);

print("\nNUMERO DE OPERADORES RELACIONAIS  = ",len(in_operadores_relacionais))
print(in_operadores_relacionais);

print("\nNUMERO DE TIPO DE VARIAVEIS  = ",len(in_tipo_variaveis))
print(in_tipo_variaveis);

print("\nNUMERO DE SIMBULOS DE ATRIBUICAO = ",len(in_simb_atribuicao))
print(in_simb_atribuicao);

print("\nNUMERO DE LOOPS = ",len(in_loops))
print(in_loops);

print("\nNUMERO DE SIMBULOS CONDICIONAIS= ",len(in_condicionais))
print(in_condicionais);

print("\nNUMERO DE DIGITOS  = ",len(in_digitos))
print(in_digitos);

print("\nNUMERO DE IDENTIFICADROES = ",len(in_identificadores))
print(in_identificadores);

print("\nNUMERO DE CONSTANTES = ",len(in_constantes))
print(in_constantes);

#VERIFICAR COM O GIU SOBRE ESSE CONSTANTES, PQ ME PARECE Q ELE TÁ IMPRIMINDO OUTRAS COISAS
#print("\nNUMERO DE CONSTANTES = ",len(in_constantes))
#print(in_constantes);

print("\nNUMERO DE DELIMITADORES = ",len(in_delimitadores))
print(in_delimitadores);
f.close()   
