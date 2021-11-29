#imports for lexer
import sys
sys.path.insert(0, "../..")
import ply.lex as lex

#General use words for language
tokens = [
    'NUMBER',
    'ID',
    'LPAREN',
    'RPAREN'
]
#Specific purpose words for language
reserved = {
    'plus': 'PLUS',
    'minus': 'MINUS',
    'times': 'TIMES',
    'dividedBy': 'DIVIDEDBY',
    'display': 'DISPLAY',
    'for': 'FOR',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'greaterThan': 'GREATERTHAN',
    'lessThan': 'LESSTHAN',
    'equals': 'EQUALS',
    'end': 'END',
    'and': 'AND',
    'or': 'OR',
    'between': 'BETWEEN',
    'endBlock': 'ENDBLOCK',
    'att': 'ATTRIBUTE'
}
#Added values of reserved words to list.
+list(reserved.values())

#Token Specifications
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
t_LPAREN = r'\('
t_RPAREN = r'\)'

#Check for reserved words. 
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

#CleanUp and extra declarations for ease of use.
t_ignore = " \t" 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_error(t):
    print("Illegal Character '%s'" % t.value[0])
    t.lexer.skip(1)
reserved_map = { }
for r in reserved:
    reserved_map[r.lower()] = r

#Construct lexer
lexer = lex.lex()

