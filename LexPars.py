#imports for lexer
import sys
from typing import Text
from arrows import *
sys.path.insert(0, "../..")




####################################################################################
##                      START OF LEXER CODE
####################################################################################



#TOKENS
TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_EOF = 'EOF'
TT_EXPONENT = 'EXPONENT'
END = 'END'

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

class RTError(Error):
    def __init__(self, pos_start, pos_end, details, context):
        super().__init__(pos_start, pos_end, 'Runtime Error', details)
        self.context = context
    
    def as_string(self):
        errorLog = self.generate_TB()
        errorLog = f'{self.error_name}: {self.details}\n'
        errorlog = errorLog + '\n\n' + string_with_arrows(self.pos_start.ftxt, self.pos_start, self.pos_end)   
        return errorLog

    def generate_TB(self):
        errorLog = ''
        pos = self.pos_start
        ctx = self.context
        while ctx:
            errorLog = f' File {pos.fn}, line {str(pos.ln + 1)}, in {ctx.display_name}\n' + errorLog
            pos = ctx.parent_entry_pps
            ctx = ctx.parent
        return 'Traceback (most recent call last):\n' + errorLog


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

            elif self.current_char == '^':
                tokens.append(Token(TT_EXPONENT, pos_start=self.pos))
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
        


##############################################################################################################
##                      START OF PARSER CODE
##############################################################################################################

#NODES
class NumberNode:
    def __init__(self, tok):
        self.tok = tok
        self.pos_start = self.tok.pos_start
        self.pos_end = self.tok.pos_end
    
    def __repr__(self):
        return f'{self.tok}'

class BinaryOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node
        self.pos_start = self.left_node.pos_start
        self.pos_end = self.right_node.pos_end

    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'

class UnaryOpNode:
    def __init__(self, op_tok, node):
        self.op_tok = op_tok
        self.node = node
        self.pos_start = self.op_tok.pos_start
        self.pos_end = node.pos_end
        
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

    # Main parse function
    def parse(self):
        result = self.expression()
        if not result.error and self.current_tok.type != TT_EOF:
            return result.failure(InvalidSyntaxError(self.current_tok.pos_start, self.current_tok.pos_end, "Expected '+', '-', or '/'"))
        return result
    
    # Defenitions for each different type of expression, based on recursion. AKA GRAMMAR RULES
    def atom(self):
        result = ParseResult()
        tok = self.current_tok

        if tok.type in (TT_INT, TT_FLOAT):
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
        return result.failure(InvalidSyntaxError(self.current_tok.pos_start, self.current_tok.pos_end, "Expected int, float, '+', '-', or '('"))
    
    def power(self):
        return self.binary_op(self.atom, (TT_EXPONENT, ), self.factor)

    def factor(self):
        result = ParseResult()
        tok = self.current_tok

        if tok.type in (TT_PLUS, TT_MINUS):
            result.register(self.advance())
            factor = result.register(self.factor())
            if result.error: return result
            return result.success(UnaryOpNode(tok, factor))

        return self.power()

    
    def term(self):
        return self.binary_op(self.factor, (TT_MUL, TT_DIV))


    def expression(self):
        return self.binary_op(self.term, (TT_PLUS, TT_MINUS))

    def binary_op(self, funcA, ops, funcB=None):
        if funcB == None:
            funcB = funcA
        result = ParseResult()
        left = result.register(funcA())
        if result.error: return result

        while self.current_tok.type in ops:
            op_tok = self.current_tok
            result.register(self.advance())
            right = result.register(funcB())
            if result.error: return result
            left = BinaryOpNode(left, op_tok, right)
        return result.success(left)


##############################################################################################################
##                                  CONTEXT
##############################################################################################################
#Future proofing for function context, add in more code for it once language can hold functions
class Context:
    def __init__(self, display_name, parent=None, parent_entry_pos=None):
        self.display_name = display_name
        self.parent = parent
        self. parent_entry_pos = parent_entry_pos

##############################################################################################################
##                                  INTERPRETER
##############################################################################################################


#Runtime Results
class RTResult:
    def __init__(self):
        self.value = None
        self.error = None

    def register(self, res):
        if res.error: self.error = res.error
        return res.value

    def success(self, value):
        self.value =  value
        return self

    def failure(self, error):
        self.error = error
        return self



#NUMBER CLASS
class Number:
    def __init__(self, value):
        self.value = value
        self.set_pos()
        self.set_context()

    def set_context(self, context=None):
        self.context = context
        return self

    def set_pos(self, pos_start=None, pos_end=None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def added_to(self, different):
        if isinstance(different, Number):
            return Number(self.value + different.value).set_context(self.context), None

    def subtracted_by(self, different):
        if isinstance(different, Number):
            return Number(self.value - different.value).set_context(self.context), None

    def multiplied_by(self, different):
        if isinstance(different, Number):
            return Number(self.value * different.value).set_context(self.context), None

    def divided_by(self, different):
        if isinstance(different, Number):
            if different.value == 0:
                return None, RTError(different.pos_start, different.pos_end, 'Division by Zero', self.context)
            
            return Number(self.value / different.value).set_context(self.context), None
    
    def power_of(self, different):
        if isinstance(different, Number):
            return Number(self.value ** different.value).set_context(self.context), None

    def __repr__(self):
        return str(self.value)


#INTERPRETER CLASS
class Interpreter:
    def visit(self, node, context):
        method_name = f'visit_{type(node).__name__}' 
    #This line will create a method that makes a string with a different name depending on the type of node "visit_BinaryOpNode"
        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context)

    def no_visit_method(self,node, context):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    #Visit methods for each node type
    def visit_NumberNode(self, node, context):
        return RTResult().success(Number(node.tok.value).set_context(context).set_pos(node.pos_start, node.pos_end))

    def visit_BinaryOpNode(self, node, context):
        res = RTResult()
        left = res.register(self.visit(node.left_node, context))
        if res.error: return res
        right = res.register(self.visit(node.right_node, context))
        if res.error: return res

        if node.op_tok.type == TT_PLUS:
            result, error = left.added_to(right)

        elif node.op_tok.type == TT_MINUS:
            result, error = left.subtracted_by(right)  

        elif node.op_tok.type == TT_MUL:
            result, error = left.multiplied_by(right)   

        elif node.op_tok.type == TT_DIV:
            result, error = left.divided_by(right) 

        elif node.op_tok.type == TT_EXPONENT:
            result, error = left.power_of(right) 

        if error: return res.failure(error)
        else:
            return res.success(result.set_pos(node.pos_start, node.pos_end))
 
    def visit_UnaryOpNode(self, node, context):
        res = RTResult()
        number = res.register(self.visit(node.node, context))
        if res.error: return res

        error = None

        if node.op_tok.type == TT_MINUS:
            number, error = number.multiplied_by(Number(-1))

        if error: return res.failure(error)
        else: return res.success(number.set_pos(node.pos_start, node.pos_end))











##############################################################################################################
##                                     RUN CODE
##############################################################################################################


#RUN 
def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error  = lexer.make_tokens()
    if error: return None, error

    # GENERATE AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error

    #run interpreter
    interpreter = Interpreter()
    context = Context('<runningProgram>')
    result = interpreter.visit(ast.node, context)

    return result.value, result.error




# Possible operands for later
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




