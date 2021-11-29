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
        #result = parse and lex here btw
        if not result == None:
            print(result)
