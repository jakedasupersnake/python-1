""" This is my utility module"""

import colors as c

def ask(question):
    print(c.blue + "what is your name" + c.reset)
    answer = input("< " + c.base3).lower().strip()
    print(c.reset)
    return answer

    
