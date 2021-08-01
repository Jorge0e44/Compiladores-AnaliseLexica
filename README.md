<p><b>UNIOESTE – Universidade Estadual do Oeste do Paraná </p>
<p>Curso de Ciência da Computação</p>
<p>Disciplina de Compiladores</p>
<p>Prof. Newton Spolaôr</p></b>

<b>Software   : Almost a compiler</b>

<i>Integrantes:
	Jorge Augusto S. Freitas <br>
	Giuliano Augusto </i>
 
<b>Descrição  : A linguagem X é um subconjunto da linguagem Pascal
			 inclui : símbolos, caracteres inválidos, códigos de formato, operadores lógicos
				operadores aritméticos, operadores relacionais, tipo de variáveis, simbolos de atribuição, Loops, Estruturas condicionais, dígitos, 				Palavras Reservadas, delimitadores </B>

*************************************************************************************************************
***************************************      EXPRESSÕES REGULARES     ***************************************
*************************************************************************************************************
# Javacc - Almost a Compiler

Análise léxica e sintática de um subconjunto da linguagem de programação Pascal


## Gramática utilizada

```javascript
// Símbolos relacionais
<EQUAL> = "="
<GREATER> = ">"
<LESSER> = "<"

// Operadores
<ARITHMETIC_OPERATOR> = "+" | "-" | "*" | "/"
<LOGIC_OPERATOR_NOT> = "not"
<LOGIC_OPERATOR> = "and" | "or"
<RELATIONAL_OPERATOR> "<=" | <LESSER> | <GREATER> | ">=" | <EQUAL> | "<>"

// Chaves
<L_BRACKET> = "{"
<R_BRACKET> = "}"

// Pontuações
<SEMICOLON> = ";"
<COMMA> = ","
<PERIOD> = "."
<COLON> = ":"

// Palavras reservadas
<BEGIN> = "begin"
<END> = "end"
<WHILE> = "while"
<FOR> = "for"
<TO> = "to"
<DO> = "do"
<IF> = "if"
<ELSE> = "else"
<THEN> = "then"
<VAR> = "var"
<PROGRAM> = "program"
<FUNCTION> = "function"

// End's
<END_PERIOD> = <END><PERIOD>
<END_SEMICOLON> = <END><SEMICOLON>

// Tipo de dados
<TYPE> = "integer" | "real" | "char" | "bool" | "string"

// Valores de dados
<DIGIT> = ["0"-"9"]
<LETTER> = ["a"-"z","A"-"Z"]
<UNDERLINE> = "_"
<APOSTROPHE> = "'"
<OTHER_CHAR> = ["$","%","#","@","!","?","&","[","]","{","}"," "]
<SPECIAL_CHAR> = <UNDERLINE>|<COMMA>|<SEMICOLON>|<PERIOD>|<COLON>|<EQUAL>|<GREATER>|<LESSER>|<ARITHMETIC_OPERATOR>|<OTHER_CHAR>|<L_BRACKET>|<R_BRACKET>
<BOOL> = "true" | "false"
<NUMBER> = (<DIGIT>)+
<REAL_NUMBER> = (<DIGIT>)+<PERIOD>(<DIGIT>)+
<STRING> = <APOSTROPHE> (<LETTER>|<DIGIT>|<SPECIAL_CHAR>)* <APOSTROPHE>

// Símbolo de atribuição
<ASSIGNMENT> <COLON><EQUAL>

// Identificador
<IDENTIFIER> = (<UNDERLINE>)*(<LETTER>)+(<DIGIT>|<UNDERLINE>|<LETTER>)*

// Começo do código
<START> = <PROGRAM_HEADER><HEADER><BEGIN> (<INSTRUCTION>)* <END_PERIOD>

// Cabeçalho do programa
<PROGRAM_HEADER> = <PROGRAM><IDENTIFIER><SEMICOLON>

// Cabeçalho, declaração de variáveis e funções
<HEADER> = (<VAR_DECLARATION> | <FUNCTION_BLOCK>)*

// Declaração de variáveis
<VAR_GROUP> = <IDENTIFIER> (<COMMA><IDENTIFIER>)*
<VAR_GROUP_TYPE> = <VAR_GROUP><COLON><TYPE>
<VAR_DECLARATION> = <VAR> (<VAR_GROUP_TYPE><SEMICOLON>)+

// Funções
<FUNCTION_HEADER> = <FUNCTION><IDENTIFIER><L_BRACKET> (<VAR_GROUP_TYPE> (<SEMICOLON><VAR_GROUP_TYPE>)* )? <R_BRACKET> <COLON> <TYPE> <SEMICOLON>
<FUNCTION_BLOCK> = <FUNCTION_HEADER> (<VAR_DECLARATION>)* <BEGIN> (<INSTRUCTION>)* <END_SEMICOLON>
<FUNCTION_CALL> = <IDENTIFIER><L_BRACKET><FUNCTION_PARAMS><R_BRACKET>
<FUNCTION_PARAMS> = (<IDENTIFIER> | <NUMBER> | <REAL_NUMBER> | <STRING> | <BOOL>) (<COMMA> (<IDENTIFIER> | <NUMBER> | <REAL_NUMBER> | <STRING> | <BOOL>))*

// Operações
<LOGIC_OPERATION> = (<LOGIC_OPERATOR_NOT>)? <RELATIONAL_OPERATION> (<LOGIC_OPERATOR> ((<LOGIC_OPERATOR_NOT>)? <RELATIONAL_OPERATION>) )*
<RELATIONAL_OPERATION> = (<ARITHMETIC_OPERATION> | <BOOL>) (<RELATIONAL_OPERATOR> (<ARITHMETIC_OPERATION> | <BOOL>) )*
<ARITHMETIC_OPERATION> = (<IDENTIFIER> | <NUMBER> | <REAL_NUMBER>) (<ARITHMETIC_OPERATOR> (<IDENTIFIER> | <NUMBER> | <REAL_NUMBER>))*

// Instruções
<ASSIGNMENT_INSTRUCTION> = <IDENTIFIER><ASSIGNMENT> (<LOGIC_OPERATION> | <STRING>) <SEMICOLON>
<LOOP_FOR_INSTRUCTION> = <FOR><IDENTIFIER><ASSIGNMENT><ARITHMETIC_OPERATION><TO><ARITHMETIC_OPERATION><DO><BEGIN> (<INSTRUCTION>)* <END_SEMICOLON>
<IF_THEN_ELSE_INSTRUCTION> = <IF><L_BRACKET><LOGIC_OPERATION><R_BRACKET><THEN><BEGIN> (<INSTRUCTION>)* (<END><ELSE><BEGIN> (<INSTRUCTION>)* )* <END_SEMICOLON>
<INSTRUCTION> = <ASSIGNMENT_INSTRUCTION> | <LOOP_FOR_INSTRUCTION> | <IF_THEN_ELSE_INSTRUCTION> | <FUNCTION_CALL><SEMICOLON>
```

*************************************************************************************************************
***************************************   DESCRIÇÃO DO FUNCIONAMENTO  ***************************************
*************************************************************************************************************




