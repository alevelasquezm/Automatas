import ply.lex as lex 
import re
import codecs
import os
import sys


tokens = ['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
'ODD','ASSIGN','NE','LOQ','LT','GT','MOQ','LPARENT',
'RPARENT','COMMA','SEMMICOLOM','DOT','KEY_R','KEY_L','COR_R','COR_L', 'UNI_CH', 'EXCL','UPDATE'
]

reservadas= {
	'begin':'BEGIN',
	'end':'END',
	'if': 'IF',
	'then ':'THEN',
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
	'actions': 'ACTIONS',
	'reservadas': 'RESERVADAS',
	'program': 'PROGRAM',
	'include': 'INCLUDE',
	'const': 'CONST',
	'type': 'TYPE',
	'var': 'VAR',
	'record': 'RECORD',
	'array': 'ARRAY',
	'of': 'OF',
	'function': 'FUNCTION',
	'for': 'FOR',
	'to': 'TO',
	'exit': 'EXIT',
	'case': 'CASE',
	'break':'BREAK',
	'downto': 'DOWNTO'


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
t_LOQ= r'<='
t_GT= r'>'
t_MOQ= r'>='
t_LPARENT= r'\('
t_RPARENT= r'\)'
t_COMMA= r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_KEY_R= r'\}'
t_KEY_L= r'\{'
t_COR_R= r'\]'
t_COR_L= r'\['
t_UPDATE= r':='
t_UNI_CH= r'\''
t_EXCL= r'!'

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
	print ("caracter invalido '%j'" % t.value[0])
	t.lexer.skip(1)

def t_ccode_nonspace(t):
	r'\s+'
	pass


archivo = 'C:/Users/aleve/Desktop/proyect/ply/test/prueba_2-1.txt'

lectura = codecs.open(archivo,"r","utf-8")
cadena = lectura.read()
lectura.close()
analizador= lex.lex ()
analizador.input(cadena)

while True:
	tok= analizador.token()
	if not tok: break
	print (tok)


