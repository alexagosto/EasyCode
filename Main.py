import LexPars as shell

print('Initializing EasyCode')
while(True):
    text = input('EasyCode > ')
    result, error = shell.run('<stdin>', text)
    if error: print(error.as_string)
    else: print(result)
