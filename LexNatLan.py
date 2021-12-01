
from LexPars import Number


COMANDS = [
    '_plus', '_minus', '_divide', '_multiply', '_pow', '_equal',
    '_notEqual', '_lessThan', '_greaterThan', '_module',
    '_exact', '_lparen', '_rparen', '_min', '_power', '_exponent',
    '_lbracket', '_rbracket', '_lcurl', '_rcurl', '_divideBy',
    '_multiplyBy', '_powerOF', '_incrementBy', '_substractBy',
    '_append', '_concat', '_removePos', '_SEMICOL'
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
    if(mathOperation(text, '_plus')):
        return text.replace('_plus', '+')
    elif(mathOperation(text, '_minus')):
        return text.replace('_minus', '-')
    elif(mathOperation(text, '_divide')):
        return text.replace('_divide', '/')
    elif(mathOperation(text, '_multiply')):
        return text.replace('_multiply', '*')
    elif(mathOperation(text, '_min')):
        return text.replace('_min', '-')
    elif(mathOperation(text, '_power')):
        return text.replace('_power', '^')
    elif(mathOperation(text, '_pow')):
        return text.replace('_power', '^')
    elif(mathOperation(text, '_exponent')):
        return text.replace('_exponent', '^')
    elif(mathOperation(text, '_module')):
        return text.replace('_module', '%')
    elif(mathOperation(text, '_exact')):
        return text.replace('_exact', '==')
    elif(mathOperation(text, '_lessThan')):
        return text.replace('_lessThan', '<')
    elif(mathOperation(text, '_greaterThan')):
        return text.replace('_greatThan', '>')
    elif(mathOperation(text, '_equal')):
        return text.replace('_equal', '=')
    elif(mathOperation(text, '_notEqual')):
        return text.replace('_notEqual', '!=')
    elif(mathOperation(text, '_lparen')):
        return text.replace('_lparen', '(')
    elif(mathOperation(text, '_rparen')):
        return text.replace('_rparen', ')')
    elif(mathOperation(text, '_lbracket')):
        return text.replace('_lbracket', '[')
    elif(mathOperation(text, '_rbracket')):
        return text.replace('_rbracket', ']')
    elif(mathOperation(text, '_lcurl')):
        return text.replace('_lcurl', '{')
    elif(mathOperation(text, '_rcurl')):
        return text.replace('_rcurl', '}')
    elif(mathOperation(text, '_divideBy')):
        return text.replace('_divideBy', '/')
    elif(mathOperation(text, '_multiplyBy')):
        return text.replace('_multiplyBy', '*')
    elif(mathOperation(text, '_powerOff')):
        return text.replace('_powerOff', '^')
    elif (mathOperation(text, '_incrementBy')):
        return text.replace('_incrementBy', '+')
    elif(mathOperation(text, '_substractBy')):
        return text.replace('_substractBy', '-')
    elif (mathOperation(text, '_append')):
        return text.replace('_append', '+')
    elif (mathOperation(text, '_concat')):
        return text.replace('_concat', '*')
    elif (mathOperation(text, '_removePos')):
        return text.replace('_removePos', '-')
    elif (mathOperation(text, '_SEMICOL')):
        return text.replace('_SEMICOL', ';')


def run(text):
    txt = text
    while(verify_commands(txt)):
        txt = lang_to_op(txt)
    return txt
