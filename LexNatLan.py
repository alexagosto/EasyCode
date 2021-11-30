
from LexPars import Number


COMANDS = [
    'plus', 'minus', 'divide',
    'multiply', 'pow', 'equal', 'notEqual',
    'lessThan', 'greaterThan', 'module', 'exact',
    'lparen', 'rparen'
]


def mathOperation(text, op):
    if op in text:
        if(text.split(op, 1)[0].isnumeric()):
            return True


def verify_commands(text):
    for op in COMANDS:
        if op in text:
            return True


def lang_to_op(text):
    if(mathOperation(text, 'plus')):
        return text.replace('plus', '+')
    elif(mathOperation(text, 'minus')):
        return text.replace('minus', '-')
    elif(mathOperation(text, 'divide')):
        return text.replace('divide', '/')
    elif(mathOperation(text, 'multiply')):
        return text.replace('multiply', '*')
    elif(mathOperation(text, 'module')):
        return text.replace('module', '%')
    elif(mathOperation(text, 'exact')):
        return text.replace('exact', '==')
    elif(mathOperation(text, 'lessThan')):
        return text.replace('lessThan', '<')
    elif(mathOperation(text, 'greaterThan')):
        return text.replace('greatThan', '>')
    elif(mathOperation(text, 'equal')):
        return text.replace('equal', '=')
    elif(mathOperation(text, 'notEqual')):
        return text.replace('notEqual', '!=')
    elif(mathOperation(text, 'lparen')):
        return text.replace('lparen', '(')
    elif(mathOperation(text, 'rparen')):
        return text.replace('rparen', ')')


def run(text):
    txt = text
    while(verify_commands(txt)):
        txt = lang_to_op(txt)
    return txt
