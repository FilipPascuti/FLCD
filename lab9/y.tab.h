/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     INTEGER = 258,
     STRING = 259,
     IF = 260,
     ELSE = 261,
     WHILE = 262,
     READINT = 263,
     READ = 264,
     PRINT = 265,
     ID = 266,
     CONST = 267,
     SEMI_COLON = 268,
     COMMA = 269,
     OPEN_CURLY_BRACKET = 270,
     CLOSED_CURLY_BRACKET = 271,
     OPEN_ROUND_BRACKET = 272,
     CLOSED_ROUND_BRACKET = 273,
     OPEN_SQUARE_BRACKET = 274,
     CLOSED_SQUARE_BRACKET = 275,
     ADD = 276,
     SUB = 277,
     MUL = 278,
     DIV = 279,
     MOD = 280,
     LT = 281,
     GT = 282,
     LTE = 283,
     GTE = 284,
     NOT_EQUAL = 285,
     EQUAL = 286,
     ASSIGN = 287,
     AND = 288,
     OR = 289
   };
#endif
/* Tokens.  */
#define INTEGER 258
#define STRING 259
#define IF 260
#define ELSE 261
#define WHILE 262
#define READINT 263
#define READ 264
#define PRINT 265
#define ID 266
#define CONST 267
#define SEMI_COLON 268
#define COMMA 269
#define OPEN_CURLY_BRACKET 270
#define CLOSED_CURLY_BRACKET 271
#define OPEN_ROUND_BRACKET 272
#define CLOSED_ROUND_BRACKET 273
#define OPEN_SQUARE_BRACKET 274
#define CLOSED_SQUARE_BRACKET 275
#define ADD 276
#define SUB 277
#define MUL 278
#define DIV 279
#define MOD 280
#define LT 281
#define GT 282
#define LTE 283
#define GTE 284
#define NOT_EQUAL 285
#define EQUAL 286
#define ASSIGN 287
#define AND 288
#define OR 289




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

