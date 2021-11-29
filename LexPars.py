#imports for lexer
import sys
from typing import Text
from arrows import *
sys.path.insert(0, "../..")




####################################################################################
##                      START OF LEXER CODE
####################################################################################



#TOKENS
TT_INT = 'TT_INT'
TT_FLOAT = 'TT_FLOAT'
TT_PLUS = 'TT_PLUS'
TT_MINUS = 'TT_MINUS'
TT_MUL = 'TT_MUL'
TT_DIV = 'TT_DIV'
TT_LPAREN = 'TT_LPAREN'
TT_RPAREN = 'TT_RPAREN'
TT_EOF = 'EOF'

#CONSTANTS
DIGITS = '0123456789'


#ERRORS

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        errorLog = f'{self.error_name}: {self.details}\n'
        errorlog = errorLog + f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        errorlog = errorLog + '\n\n' + string_with_arrows(self.pos_start.ftxt, self.pos_start, self.pos_end)
        return errorLog

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

class InvalidSyntaxError(Error):
	def __init__(self, pos_start, pos_end, details=''):
		super().__init__(pos_start, pos_end, 'Invalid Syntax', details)


#POSITION
class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char=None):
        self.idx+=1
        self.col+=1

        if current_char == '\n':
            self.ln += 1
            self.col+= 0
        
        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)


class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()
        
        if pos_end:
            self.pos_end = pos_end

    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

#Lexer 

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char) 
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:

            if self.current_char in ' \t':
                self.advance()

            elif self.current_char in DIGITS:
                tokens.append(self.make_number())

            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS, pos_start=self.pos))
                self.advance()

            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS, pos_start=self.pos))
                self.advance()

            elif self.current_char == '*':
                tokens.append(Token(TT_MUL, pos_start=self.pos))
                self.advance()

            elif self.current_char == '/':
                tokens.append(Token(TT_DIV, pos_start=self.pos))
                self.advance()

            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN, pos_start=self.pos))
                self.advance()

            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN, pos_start=self.pos))
                self.advance()

            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [],IllegalCharError(pos_start, self.pos, "'" + char + "'")
        tokens.append(Token(TT_EOF, pos_start=self.pos))
        return tokens, None


    def make_number(self):
        num_str = ''
        period_count = 0
        pos_start = self.pos.copy()

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if period_count == 1: break 
                period_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()
            
        if period_count == 0:
            return Token(TT_INT, int(num_str), pos_start, self.pos)
        else:
            return Token(TT_FLOAT , float(num_str), pos_start, self.pos)
        


####################################################################################
##                      START OF PARSER CODE
####################################################################################

#NODES
class NumberNode:
    def __init__(self, tok):
        self.tok = tok
    
    def __repr__(self):
        return f'{self.tok}'

class BinaryOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'

class UnaryOpNode:
	def __init__(self, op_tok, node):
		self.op_tok = op_tok
		self.node = node

	def __repr__(self):
		return f'({self.op_tok}, {self.node})'


#PARSER RESULT 
class ParseResult:
	def __init__(self):
		self.error = None
		self.node = None

	def register(self, result):
		if isinstance(result, ParseResult):
			if result.error: self.error = result.error
			return result.node

		return result

	def success(self, node):
		self.node = node
		return self

	def failure(self, error):
		self.error = error
		return self

#PARSER CLASS

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self, ):
        self.tok_idx +=1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

    def parse(self):
        result = self.expression()
        if not result.error and self.current_tok.type != TT_EOF:
            return result.failure(InvalidSyntaxError(self.current_tok.pos_start, self.current_tok.pos_end, "Expected '+', '-', or '/'"))
        return result

    def factor(self):
        result = ParseResult()
        tok = self.current_tok

        if tok.type in (TT_PLUS, TT_MINUS):
            result.register(self.advance())
            factor = result.register(self.factor())
            if result.error: return result
            return result.success(UnaryOpNode(tok, factor))
        
        elif tok.type in (TT_INT, TT_FLOAT):
            result.register(self.advance())
            return result.success(NumberNode(tok))

        elif tok.type == TT_LPAREN:
            result.register(self.advance())
            expr = result.register(self.expression())
            if result.error: return result
            if self.current_tok.type == TT_RPAREN:
                result.register(self.advance())
                return result.success(expr)
            else: 
                return result.failure(InvalidSyntaxError(self.current_tok.pos_start, self.current_tok.pos_end, "Expected ')'"))

        return result.failure(InvalidSyntaxError(tok.pos_start, tok.pos_end, "Expected int or float."))


    def term(self):
        return self.binary_op(self.factor, (TT_MUL, TT_DIV))


    def expression(self):
        return self.binary_op(self.term, (TT_PLUS, TT_MINUS))

    def binary_op(self, func, ops):
        result = ParseResult()
        left = result.register(func())
        if result.error: return result

        while self.current_tok.type in ops:
            op_tok = self.current_tok
            result.register(self.advance())
            right = result.register(func())
            if result.error: return result
            left = BinaryOpNode(left, op_tok, right)
        return result.success(left)


####################################################################################
##                                     RUN CODE
####################################################################################


#RUN 
def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error  = lexer.make_tokens()
    if error: return None, error

    # GENERATE AST
    parser = Parser(tokens)
    ast = parser.parse()


    return ast.node, ast.error





# reserved = {
#     'display': 'DISPLAY',
#     'for': 'FOR',
#     'if': 'IF',
#     'else': 'ELSE',
#     'while': 'WHILE',
#     'greaterThan': 'GREATERTHAN',
#     'lessThan': 'LESSTHAN',
#     'equals': 'EQUALS',
#     'end': 'END',
#     'and': 'AND',
#     'exact': 'EXACT',
#     'between': 'BETWEEN',
#     'endBlock': 'ENDBLOCK',
#     'att': 'ATTRIBUTE'
# }




