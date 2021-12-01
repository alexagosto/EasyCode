import LexPars 

print('Initializing EasyCode')
while(True):
    text = input('EasyCode > ')
    result, error = LexPars.run('<stdin>', text)
    if error: print(error.as_string)
    elif result: print(repr(result))

# Run this python file and enjoy EasyCode. The following are possible operations and syntax that EasyCode allows you to do!