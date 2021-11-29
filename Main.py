import Parser as parser

print('Initializing EasyCode')
while(True):
    try:
        text = input('EasyCode > ')
    except EOFError:
        break
    except KeyboardInterrupt:
        break
    if not text: continue
    result = parser.parser.parse(text)
    if not result == None:
        print(result)
