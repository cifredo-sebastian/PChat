import ply.lex as lex

reserve = {
    'set' : 'SET',
    'connect' : 'CONNECT',
    'open' : 'OPEN',
    'close' : 'CLOSE',
    'send' : 'SEND'
    }

tokens = ['PERIOD','ID','NUMBER','STRING','LPAREN', 'RPAREN']  + list(reserve.values())

t_PERIOD = r'\.'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_ID(token):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    token.type = reserve.get(token.value, 'ID')
    return token

def t_NUMBER(token):
    r'\d+'
    token.value = int(token.value)    
    return token

def t_NLINE(token):
    r'\n+'
    token.lexer.lineno += len(token.value)
    return token


def t_S(t):
    r' [ ]+ '
    
def t_STRING(token):
    r"'([^\\']+|\\'|\\\\)*'"
    token.value = token.value[1:-1]
    return token


# Error handling rule
def t_error(token):
    print("Illegal character '%s'" % token.value[0], token.lineno)
    token.lexer.skip(1)


lexer = lex.lex()