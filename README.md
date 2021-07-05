<p><b>UNIOESTE – Universidade Estadual do Oeste do Paraná </p>
<p>Curso de Ciência da Computação</p>
<p>Disciplina de Compiladores</p>
<p>Prof. Newton Spolaôr</p></b>

<b>Software   : Almost a compiler</b>

<i>Integrantes:
	Jorge Augusto S. Freitas <br>
	Giuliano Augusto </i>
 
<b>Descrição  : A linguagem X é um subconjunto da linguagem C
			 inclui : símbolos, caracteres inválidos, códigos de formato, operadores lógicos
				operadores aritméticos, operadores relacionais, tipo de variáveis, simbolos de atribuição, Loops, Estruturas condicionais, dígitos, 				Palavras Reservadas, delimitadores </B>

*************************************************************************************************************
***************************************      EXPRESSÕES REGULARES     ***************************************
*************************************************************************************************************

TOKEN: // Expressão regular utilizada pra reconhecer operação aritmetica <BR>
{
		<operadores_aritmeticos= "+" | "-" | "*" | "/" | "%">
} 

TOKEN: // Expressão regular utilizada pra reconhecer operação lógica
{<br>
	<operadores_logicos= "&&" | "||"| "^"|"!">
}


TOKEN: // Expressão regular utilizada pra reconhecer operação relacional
{<br>
	<operadores_relacionais ="+=" | "!=" | "-=" |"==" | "<" | ">" |"<="| ">=">
}

TOKEN: // Expressão regular utilizada pra reconhecer os tipos de variáveis da nossa linguagem
{<br>
	<tipo_variaveis= "int" | "float"| "long"| "double" | "short" | "char" | "unsigned" | "signed" >
}

TOKEN: // Aqui são várias expressões utilizadas pra reconhecer palavras reservadas
{<br>
	<STRUCT = "struct"> | <AUTO= "auto"> | <BREAK = "break"> | <CASE = "case"> | <CONST = "const">| 
	<CONTINUE = "continue"> | <DEFAULT = "default"> | <ENUM ="enum" | <EXTERN = "extern" | <GOTO="goto"> | <DEFINE = "define"> | <REGISTER = "register">| <RETURN = "return"> | <SIZEOF = "sizeof">| <STATIC = "static"> | <INCLUDE = "include"> | <MAIN = "main"> | <TYPEDEF = "typedef"> | <UNION = "union"> | <VOID = "void"> | <VOLATILE = "volatile">  

}


TOKEN: // Aqui são várias expressões utilizadas pra reconhecer simbolos
{<br>

	<CERQUILHA = "#"> | <CIFRAO ="$"> | <AMPERSAND = "&">">	
}

<ABRE_PAREN = "("> | <FECHA_PAREN= ")"> |<WHILE= "while"> | 
	<FOR= "for"> | <DO= "do"> | <IF= "if"> | <ELSE= "else"> |
	<PTO_VIRG= ";"> | <VIRGULA= ","> | <UNDERLINE= "_">
	| <DOIS_PTOS= ":">

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
	<LETRA = ("a..z" | "A..Z")>
	<IDENTIFICADOR= (<UNDERLINE>)(<LETRA>|<DIGITOS|<UNDERLINE>)*| (<LETRA>)(<LETRA>|<DIGITOS> <UNDERLINE>)*>

}
 

*************************************************************************************************************
***************************************   DESCRIÇÃO DO FUNCIONAMENTO  ***************************************
*************************************************************************************************************
Documentação Python 3:
https://docs.python.org/pt-br/3/tutorial/index.html

Com o auxilio do Python 3 ou versões superiores, fazer os seguintes passos:
EXECUTAR:
// Execute o comando a seguir no prompt de comando (CMD) ou Powershell na pasta onde contenham os arquivos:
python lex.py

// se tudo ocorreu bem ele executa direto o programa
// Será solicitado ao usuário que digite o nome do arquivo a ser analisado
// É apresentado para o usuário os resultados



