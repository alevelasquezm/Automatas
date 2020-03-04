import ply.lex as lex 
import re
import codecs
import os
import sys


tokens = ['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
'ODD','ASSIGN','NE','LTE','LT','GT','GTE','LPARENT',
'RPARENT','COMMA','SEMMICOLOM','DOT','UPDATE'
]

reservadas= {
	'begin':'BEGIN',
	'end':'END',
	'if': 'IF',
	'then':'THEN',
	'while': 'WHILE',
	'set': 'SET',
	'do': 'DO',
	'call': 'CALL',
	'const': 'CONST',
	'int': 'INT',
	'procedure': 'PROCEDURE',
	'out': 'OUT',
	'in': 'IN',
	'else': 'ELSE',
	'token': 'TOKEN',
	'program': 'PROGRAM',
	'include': 'INCLUDE',
	'const': 'CONST'

}

tokens= tokens +list(reservadas.values())

t_ignore = '\t'
t_PLUS= r'\+'
t_MINUS= r'\-'
t_TIMES= r'\*'
t_DIVIDE= r'/'
t_ODD= r'ODD'
t_ASSIGN = r'='
t_NE= r'<>'
t_LT= r'<'
t_LTE= r'<='
t_GT= r'>'
t_GTE= r'>='
t_LPARENT= r'\('
t_RPARENT= r'\)'
t_COMMA= r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE= r':='

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value= t.value.upper()
		t.type= t.value
		return t


def t_COMMENT(t):
	r'\#.*'
	pass
	


def t_NUMBER(t):
	r'\d+'
	t.value= int(t.value)
	return t


def t_error(t):
	print ("caracter invalido '%s'" % t.value[0])
	t.lexer.skip(1)

def t_ccode_nonspace(t):
	r'\s+'
	pass


test = 'C:/Users/aleve/Desktop/proyect/ply/test/prueba0.pl0'

fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()
analizador= lex.lex ()
analizador.input(cadena)

while True:
	tok= analizador.token()
	if not tok: break
	print (tok)


