import handlers

def handle_nocmd(*args):
    print "Nie ma komendy"
    
def handle_msg(text):
    tokens = text.split()
    handle = getattr(handlers, 'handle_' + tokens[0], handle_nocmd)
    handle(*tokens[1:])

    
    

while True:
    text = raw_input('> ')
    handle_msg(text)


