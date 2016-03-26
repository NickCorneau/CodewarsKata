import string
from codecs import encode as _dont_use_this_

def rot13(message):

    cap_letters = map(chr, range(65, 91))
    reg_letters = map(chr, range(97, 123))
    
    solution = []
    
    for i in message:
        if (i in cap_letters):
            i = chr((((ord(i) - 65) + 13) % 26) + 65)
        elif (i in reg_letters):
            i = chr((((ord(i) - 97) + 13) % 26) + 97)
        solution.append(i)
        
    return ''.join(solution)
