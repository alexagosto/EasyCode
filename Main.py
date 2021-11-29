import Lexer as lexer
import Parser as parser

print('Initializing EasyCode')
while(True):
    text = input('EasyCode > ')
    result, error = lexer.run('<stdin>', text)
    #result = parser.parser.parse(text)
    if error: print(error.as_string)
    else: print(result)
