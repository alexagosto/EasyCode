import LexPars as shell
import LexNatLan 
print('Initializing EasyCode')
while(True):
    text = input('EasyCode > ')
    text = LexNatLan.run(text)
    result, error = shell.run('<stdin>', text)
    if error:
        print(error.as_string)
    else:
        print(result)
