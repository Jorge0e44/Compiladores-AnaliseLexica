#https://docs.python.org/pt-br/3/library/re.html
#https://github.com/python/cpython/blob/main/Lib/re.py
#https://docs.python.org/3/library/os.html
# Links para estudo da Biblioteca RE

#O uso do import os serve para portabilizar a utilização em qualquer Sistema Operacional
#O uso do import re serve para utilizarmos a biblioteca expressão regular do Python
import re
import os

s = input("Enter filename : ")
f = open(s, 'r')
text = f.read()

######################################		DEFINIÇÃO DAS CLASSES DE TOKENS		#################################

##### Lista de Tokens para definição de Simbolos especiais #######
simbolos = ['#', '$', '&', '^']

##### Lista de Tokens para definição de Caracteres inválidos #######
caracteres_invalidos = ['@','ç','º','£']

##### Lista de Tokens para definição de Códigos de formato #######
codigos_formato = ['%c','%d','%f','%s']

##### Lista de Tokens para definição de Operadores Lógicos #######
operadores_logicos = ['&&','||','!','^'] # AND OR NOT XOR

##### Lista de Tokens para definição de Operadores Aritméticos ######
operadores_aritmeticos=['+','-','*','/','%']

##### Lista de Tokens para definição de Operadores Relacionais #######
operadores_relacionais = [ '+=','!=','-=', '==', '<', '>', '<=', '>=']

##### Lista de Tokens para definição de Tipos de Variáveis #######
tipo_variaveis=['int','float','long','double','short','char','long','unsigned','signed',]

##### Lista de Token para Símbolo de Atribuição #######
simb_atribuicao = ['=']

##### Lista de Tokens para Repetição do tipo Loop #######
loops = ['for','while', 'do']

##### Lista de Tokens para Repetição do Tipo Condicionais #######
condicionais = ['if','else','switch']

##### Lista de Tokens para o Tipo Dígito #######
digitos = ['0','1','2','3','4','5','6','7','8','9']

##### Lista de Tokens para o tipo palavras Reservadas #######
PalavrasReservadas = ['auto','break', 'case', 'const', 'continue', 'default', 
			'enum', 'extern', 'goto','define','struct',
			  'register', 'return', 'sizeof', 'static','include','main'
			'typedef', 'union', 'void', 'volatile']

##### Lista de Tokens para Delimitadores ########
delimitadores = [' ', '	', '.', ',', '\n', ';', '(', ')', '<', '>', '{', '}', '[', ']']


################# Definição de Listas para Tokens de cada tipo ####################
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
in_comentarios = []
in_constantes = []
in_codigos_formato = []
in_codigos_estruturas = []
in_caracteres_invalidos = []

tokens = []
isString = False
isWord = False
isCmt = 0
token = ''


#################### INÍCIO DOS TESTES A FIM DE VERIFICAR CADA TOKEN AO SEU RESPECTIVO TIPO ####################################################
for i in text:
    #FAZ UM TESTE PARA VERIFICAR SE O CARACTER / É UM COMENTÁRIO OU UM OPERADOR ARITMÉTICO	
	if i == '/': 
		isCmt = isCmt+1

	elif isCmt == 2:
		if i == '\n':
			token = ''
			isCmt = 0
	
	#FAZ A VERIFICAÇÃO DOS CARACTERES " OU ' PARA VERIFICAR O TIPO
	elif i == '"' or i == "'":
		if isString:
			tokens.append(token)
			token = ''
		isString = not isString

	#FAZ A VERIFICAÇÃO PARA UMA STRING
	elif isString:
		token = token+i

    #FAZ A VERIFICAÇÃO PARA UMA SIMBOLO
	elif i in simbolos:
		tokens.append(i)

	#FAZ A VERIFICAÇÃO PARA UMA PALAVRA       
	elif i.isalnum() and not isWord:
		isWord = True
		token = i
    
	#FAZ UMA SÉRIE DE COMPARAÇÕES PARA VERIFICAR ALGUNS TIPOS DE CLASSE DE TOKENS A FIM COLOCAR ESSES TIPOS EM UMA LISTA
	elif (i in delimitadores) or (i in caracteres_invalidos) or (i in operadores_aritmeticos) or (i in operadores_logicos) or (i in operadores_relacionais) or (i in loops) or (i in condicionais) or (i in codigos_formato):
		if token:
			tokens.append(token)
			token = ''
        
		if not (i==' ' or i=='\n' or i=='	'):
			tokens.append(i)

	elif isWord:
		token = token+i

os.system("PAUSE")
for token in tokens:
    #VERIFICA SE O CONTEUDO DE TOKEN ESTÁ CONTIDO DENTRO DAS DEFINIÇÕES DA LISTA DE SIMBOLOS
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA DE SIMBOLOS
	if token in simbolos:
		in_spl_Simbolos.append(token)

	#VERIFICA SE O CONTEUDO DE TOKEN ESTÁ CONTIDO DENTRO DAS DEFINIÇÕES DA LISTA DE CARACTERES INVALIDOS
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA DE CARACTERES INVÁLIDOS
	elif token in caracteres_invalidos:
    		in_caracteres_invalidos.append(token)

	#PROCURA O %f EM TOKEN
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA CODIGOS DE FORMATO
	elif re.findall("^%f",token):
		in_codigos_formato.append(token)
	#PROCURA O %c EM TOKEN
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA CODIGOS DE FORMATO
	elif re.findall("^%c",token):
    		in_codigos_formato.append(token)
	#PROCURA O %d EM TOKEN
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA CODIGOS DE FORMATO
	elif re.findall("^%d",token):
    		in_codigos_formato.append(token)
	#PROCURA O %s EM TOKEN
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA CODIGOS DE FORMATO
	elif re.findall("^%s",token):
    		in_codigos_formato.append(token)

	#VERIFICA SE O CONTEUDO DE TOKEN ESTÁ CONTIDO DENTRO DAS DEFINIÇÕES DA LISTA DE OPERADORES RELACIONAIS
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA DE OPERADORES RELACIONAIS
	elif token in operadores_relacionais:
		in_operadores_relacionais.append(token)
	
	#VERIFICA SE O CONTEUDO DE TOKEN ESTÁ CONTIDO DENTRO DAS DEFINIÇÕES DA LISTA DE OPERADORES ARITMÉTICOS
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA DE OPERADORES ARITMÉTICOS
	elif token in operadores_aritmeticos:
		in_operadores_aritmeticos.append(token)
	
	#VERIFICA SE O CONTEUDO DE TOKEN ESTÁ CONTIDO DENTRO DAS DEFINIÇÕES DA LISTA DE OPERADORES LÓGICOS
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA DE OPERADORES LÓGICOS
	elif token in operadores_logicos:
		in_operadores_logicos.append(token)

	#VERIFICA SE O CONTEUDO DE TOKEN ESTÁ CONTIDO DENTRO DAS DEFINIÇÕES DA LISTA DE TIPOS DE VARIÁVEIS
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA DE TIPOS DE VARIÁVEIS
	elif token in tipo_variaveis:
		in_tipo_variaveis.append(token)
	
	#VERIFICA SE O CONTEUDO DE TOKEN ESTÁ CONTIDO DENTRO DAS DEFINIÇÕES DA LISTA DE SIMB DE ATRIBUIÇÃO
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA DE SIMB DE ATRIBUIÇÃO
	elif token in simb_atribuicao:
		in_simb_atribuicao.append(token)
	
	#VERIFICA SE O CONTEUDO DE TOKEN ESTÁ CONTIDO DENTRO DAS DEFINIÇÕES DA LISTA DE LOOPS
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA DE TIPOS LOOPS
	elif token in loops:
		in_loops.append(token)

	#VERIFICA SE O CONTEUDO DE TOKEN ESTÁ CONTIDO DENTRO DAS DEFINIÇÕES DA LISTA DE CONDICIONAIS
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA DE CONDICIONAIS
	elif token in condicionais:
		in_condicionais.append(token)
	
	#VERIFICA SE O CONTEUDO DE TOKEN ESTÁ CONTIDO DENTRO DAS DEFINIÇÕES DA LISTA DE DÍGITOS
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA DE DÍGITOS
	elif token in digitos:
		in_digitos.append(token)
	
	#VERIFICA SE O CONTEUDO DE TOKEN ESTÁ CONTIDO DENTRO DAS DEFINIÇÕES DA LISTA DE PALAVRAS RESERVADAS
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA DE PALAVRAS RESERVADAS
	elif token in PalavrasReservadas:
		in_PalavrasReservadas.append(token)


	#PROCURA CARACTERES DENTRO DO RANGE DE A-Z OU a-z
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA DE IDENTIFICADORES
	#O USO DO [] CORRESPONDE QUE QUEREMOS PEGAR UM CONJUNTO DE CARACTERES
	# O uso do ^ corresponde ao inicio da String
	# O uso do * corresponde a 0 ou mais repetições na String 
	# $ corresponde ao final da string ou imediatamente antes da nova linha
	elif re.search("^[_a-zA-Z][_a-zA-Z0-9]*$",token):  
		in_identificadores.append(token)

	#VERIFICA SE O CONTEUDO DE TOKEN ESTÁ CONTIDO DENTRO DAS DEFINIÇÕES DA LISTA DE DELIMITADORES
	#SE ESTIVER CONTIDO, FAZ UMA INCLUSÃO NA LISTA DE DELIMITADORES	
	elif token in delimitadores:
		in_delimitadores.append(token)

	#SE NÃO CORRESPONDER A NENHUMA DAS OUTRAS DEFINIÇÕES ANTERIORES, FAZ UMA INCLUSÃO NA LISTA DE CONSTANTES
	else:
		in_constantes.append(token)
	

#############	APRESENTA NA TELA OS RESULTADOS COM O TIPO DE TOKEN ENCONTRADO E A QUANTIDADE	############################				
print("NUMERO DE TOKENS  = ", len(tokens))  

print("\nNUMERO DE CODIGOS DE FORMATO = ",len(in_codigos_formato))
print(in_codigos_formato);

print("\nNUMERO DE PALAVRAS RESERVADAS  = ",len(in_PalavrasReservadas))
print(in_PalavrasReservadas);

print("\nNNUMERO DE CARACTERES INVALIDOS = ",len(in_caracteres_invalidos))
print(in_caracteres_invalidos);

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

print("\nNUMERO DE DELIMITADORES = ",len(in_delimitadores))
print(in_delimitadores);

os.system("PAUSE");
f.close()   
#FIM DO PROGRAMA
