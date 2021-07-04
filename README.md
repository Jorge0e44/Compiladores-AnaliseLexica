<p><b>UNIOESTE – Universidade Estadual do Oeste do Paraná </p>
<p>Curso de Ciência da Computação</p>
<p>Disciplina de Compiladores</p>
<p>Prof. Newton Spolaôr</p></b>

Alunos : Giuliano Augusto
         Jorge Augusto



Implementar um software que simula um compilador capaz de realizar a análise léxica: Ao ser executado, pedir para o usuário digitar ou selecionar o nome do arquivo fonte (Ex: 
fonte1.txt, fonte2.txt);

Ler o código fonte a partir do arquivo selecionado;

Reconhecer classes de tokens no código fonte por meio da análise léxica;

Realizar tratamento de erro léxico, mostrando na tela qual o tipo de erro e apontando a posição do erro. Para ter uma maior cobertura de erros diferentes, é útil pesquisar os tipos de erros léxicos mais comuns em linguagens populares;

O software deve ser implementado em qualquer linguagem, com ou sem o apoio de ferramentas auxiliares como Lex, Yacc e Javacc.


<b>Software   : Almost a compiler</b>

Integrantes: Jorge Augusto S. Freitas
	     Giuliano Augusto
 
Descrição  : A linguagem X é um subconjunto da linguagem C
			 inclui : símbolos, caracteres inválidos, códigos de formato, operadores lógicos
				operadores aritméticos, operadores relacionais, tipo de variáveis, 				simbolos de atribuição, Loops, Estruturas condicionais, dígitos, 				Palavras Reservadas, delimitadores

*************************************************************************************************************
***************************************      EXPRESSÕES REGULARES     ***************************************
*************************************************************************************************************

TOKEN: // Expressão regular utilizada pra reconhecer operação aritmetica
{
		<operadores_aritmeticos= "+" | "-" | "*" | "/" | "%">
} 


TOKEN: // Expressão regular utilizada pra reconhecer operação lógica
{
	<operadores_logicos= "&&" | "||"| "^"|"!">
}


TOKEN: // Expressão regular utilizada pra reconhecer operação relacional
{
	<operadores_relacionais ="+=" | "!=" | "-=" |"==" | "<" | ">" |"<="| ">=">
}

TOKEN: // Expressão regular utilizada pra reconhecer os tipos de variáveis da nossa linguagem
{
	<tipo_variaveis= "int" | "float"| "long"| "double" | "short" | "char" | "unsigned" | "signed" >
}

TOKEN: // Aqui são várias expressões utilizadas pra reconhecer palavras reservadas
{
	<STRUCT = "struct"> | <AUTO= "auto"> | <BREAK = "break"> | <CASE = "case"> | <CONST = "const">| 
	<CONTINUE = "continue"> | <"DEFAULT = "default"> | <"ENUM ="enum" | <"EXTERN = "extern" | <"GOTO" ="goto"> | <"DEFINE = "define"> | <"REGISTER = "register">| <"RETURN = "return"> | <"SIZEOF = "sizeof">| <"STATIC = "static"> | <"INCLUDE = "include"> | <"MAIN = "main"> | <"TYPEDEF = "typedef"> | <"UNION = "union"> | <"VOID = "void"> | <"VOLATILE = "volatile">  

}


TOKEN: // Aqui são várias expressões utilizadas pra reconhecer simbolos
{

	<CERQUILHA = "#"> | <CIFRAO ="$"> | <AMPERSAND = "&"> | <TIL ="^">	
}

<ABRE_PAREN = "("> | <FECHA_PAREN= ")"> |<WHILE= "while"> | 
	<FOR= "for"> | <TO= "to"> | <DO= "do"> | <IF= "if"> | <ELSE= "else"> | <THEN= "then"> | 
	<PTO_VIRG: ";"> | <VIRGULA: ","> | <FINAL_END: "end."> | <VAR: "var"> | <UNDERLINE: "_">
	| <DOIS_PTOS: ":"> | <PROGRAM: "program"> | <FUNCTION: "function">

}

TOKEN: // Expressão regular utilizada pra reconhecer o comando de atribuição em C
{
	<ATRIBUICAO= "=">
}


TOKEN: // Expressão regular utilizada pra reconhecer os digitos de 0 a 9
{
	<DIGITOS= (["0"-"9"])>
}

TOKEN: // Expressão regular utilizada pra reconhecer a nomeação dos identificadores
{
	<LETRA> = ("a..z" | "A..Z")>
	<IDENTIFICADOR= (<UNDERLINE>)(<LETRA>|<DIGITOS|<UNDERLINE>)*| (<LETRA>)(<LETRA>|<DIGITOS> <UNDERLINE>)* 

}
 

*************************************************************************************************************
***************************************   DESCRIÇÃO DO FUNCIONAMENTO  ***************************************
*************************************************************************************************************

Com o auxilio do Python 3 ou versões superiores, fazer os seguintes passos:
EXECUTAR:

// execute o comando a seguir no prompt de comando (CMD) ou Powershell:
python lex.py

// se tudo ocorreu bem ele executa direto o programa
// Será solicitado ao usuário que digite o nome do arquivo a ser analisado
// É apresentado



