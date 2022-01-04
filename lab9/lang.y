%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1

int yylex();
int yyerror(char *);
int strcmp(const char *, const char *);
%}

%token INTEGER
%token STRING
%token IF
%token ELSE
%token WHILE
%token READINT
%token READ
%token PRINT

%token ID

%token CONST

%token SEMI_COLON
%token COMMA
%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET
%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token OPEN_SQUARE_BRACKET
%token CLOSED_SQUARE_BRACKET

%token ADD
%token SUB
%token MUL
%token DIV
%token MOD
%token LT
%token GT
%token LTE
%token GTE
%token NOT_EQUAL
%token EQUAL
%token ASSIGN
%token AND
%token OR


%start program


%%

program : statement_list
        ;
statement_list : statement statement_list | statement
        ;
statement : simple_statement SEMI_COLON | compound_statement
        ;
simple_statement : assignment_statement | declaration_statement | io_statement
        ;
compound_statement : if_statement | while_statement
        ;
primitive_type : INTEGER | STRING
        ;
list_type : primitive_type OPEN_SQUARE_BRACKET CONST CLOSED_SQUARE_BRACKET
        ;
type : primitive_type | list_type
        ;
relational_operator : AND | OR | LT | GT | LTE | GTE | EQUAL | NOT_EQUAL
        ;
expression : term ADD expression | term SUB expression | term MOD expression | term
        ;
term : factor MUL term | factor DIV term | factor
        ;
factor : ID | CONST | OPEN_ROUND_BRACKET expression CLOSED_ROUND_BRACKET
        ;
condition : expression relational_operator expression
        ;
declaration_statement : type ID | type ID ASSIGN expression
        ;
assignment_statement : ID ASSIGN expression
        ;
io_statement : ID ASSIGN READINT OPEN_ROUND_BRACKET CLOSED_ROUND_BRACKET
             | ID ASSIGN READ OPEN_ROUND_BRACKET CLOSED_ROUND_BRACKET
             | PRINT OPEN_ROUND_BRACKET expression CLOSED_ROUND_BRACKET
        ;
if_statement : IF OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET OPEN_CURLY_BRACKET statement_list CLOSED_CURLY_BRACKET
             | IF OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET OPEN_CURLY_BRACKET statement_list CLOSED_CURLY_BRACKET ELSE OPEN_CURLY_BRACKET statement_list CLOSED_CURLY_BRACKET
while_statement : WHILE OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET OPEN_CURLY_BRACKET statement_list CLOSED_CURLY_BRACKET

%%
int yyerror(char *s)
{
        printf("%s\n",s);
}

extern FILE *yyin;

int main(int argc, char **argv)
{
	if(argc>1) yyin :  fopen(argv[1],"r");
	if(argc>2 && !strcmp(argv[2],"-d")) yydebug: 1;
	if(!yyparse()) fprintf(stderr, "\tO.K.\n");
}

