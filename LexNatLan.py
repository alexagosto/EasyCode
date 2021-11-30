
COMANDS = ['plus', 'minus', 'divide', 'module', 'exact',
           'equal',
           'not-equal',
           'less-than',
           'greater-than',
           'less-than-equal',
           'greater-than-equal', ]


def verify_commands(txt):
    for op in COMANDS:
        if op in txt:
            return True


def lang_to_op(text):
    if('plus' in text):
        return text.replace('plus', '+')
    elif('minus' in text):
        return text.replace('minus', '-')
    elif('divide' in text):
        return text.replace('divide', '/')
    elif('module' in text):
        return text.replace('module', '%')
    elif('exact' in text):
        return text.replace('exact', '==')
    elif('equal' in text):
        return text.replace('equal', '=')
    elif('not-equal' in text):
        return text.replace('not-equal', '!=')
    elif('less-than' in text):
        return text.replace('less-than', '<')
    elif('more-than' in text):
        return text.replace('more-than', '>')
    elif('less-than-equal' in text):
        return text.replace('less-than-equal', '<=')
    elif('greater-than-equal' in text):
        return text.replace('greater-than-equal', '>=')


def run(text):
    txt = text
    while(verify_commands(txt)):
        txt = lang_to_op(txt)
    return txt
