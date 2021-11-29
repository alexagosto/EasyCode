# Imports for parser
import sys
sys.path.insert(0, "../..")
import ply.yacc as yacc
# v this import gives us tokens from each line of code 
from Lexer import tokens 

# Made to hold tuples
names = {}
# Int to know how many indents/spaces were used in file. 
spaces = 0

# Intermediate code location
f = open('D:\\Programming stuff\\VSC\\PL4030 Project\\test.py','w')

#
# The following lines of code will declare operands
# for token names that will be used in intermediate code,
# This will include math, prints, attributes, among others.
#
# Simple ones will not be explained, complex operands will
# have a comment explaining what they do. 
#

def p_expression_plus(p):


def p_expression_minus(p):


def p_expression_times(p):


def p_expression_db(p):


def p_expression_equals(p):


def p_expression_att(p):


def p_expression_display(p):


def p_for(p):


def p_condition_while(p):


def p_condition_if(p):


def p_condition_else(p):


def p_condition_gt(p):


def p_condition_lt(p):


def p_condition_exact(p):


# End of syntax analysis. 
def p_endblock(p):



# Following operands convert inputs of other operands.
def p_term_ID(p):


def p_expression_term(p):


def p_term_factor(p):


def p_factor_num(p):


def p_factor_expr(p):  


# End of converting operands.



# Used to change indents/spaces of next line. 
def p_expression_end(p):

# Helping operands to clean up and error check intermediate code.
def indent ():


def variable_verify():


def p_error(p):




# Generate Parser. 
parser = yacc.yacc() 
