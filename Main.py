#Imports for main
import LexNatLan
import LexPars


#initialization of run function from lexpars
print('Initializing EasyCode')
while(True):
    #Console input + natural language change.
    text = input('EasyCode > ')
    text = LexNatLan.run(text)

    #Verifies for single line code
    if text.strip() == "": continue
    result, error = LexPars.run('<stdin>', text)

    if error: print(error.as_string)

    elif result:
        if len(result.elements) == 1: print(repr(result.elements[0]))
        else: print(repr(result))


# Run this python file and enjoy EasyCode. The following are possible operations and syntax that EasyCode allows you to do!
