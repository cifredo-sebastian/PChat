from lexer import tokens
import ply.yacc as yacc
import client as client
import server as server

def p_set(p):
    'expression : SET LPAREN NUMBER PERIOD NUMBER PERIOD NUMBER PERIOD NUMBER RPAREN'
    client.host = "{0}.{1}.{2}.{3}".format(p[3],p[5],p[7],p[9])
    p[0] = "Server IP Address set to " + client.host

def p_connect(p):
    'expression : CONNECT'
    client.connect()
    p[0] = "Connected to server " + client.host

def p_open(p):
    'expression : OPEN'
    server.openserver()

def p_close(p):
    'expression : CLOSE'
    client.close()

def p_send(p):
    'expression : SEND STRING'
    client.send(p[2])
    p[0] = "Sent: " + p[2]
    

parser = yacc.yacc()


while True:
    try:
        s = input('PChat > ')
        s.lower()
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
    
    
    
