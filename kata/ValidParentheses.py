def valid_parentheses(string):

    left_count = 0 # (
    right_count = 0 # )
    
    for i in string:
        if (i == '('): left_count = left_count + 1
        if (i == ')'): right_count = right_count + 1
    if left_count != right_count:
        return False
    
    
    left_p = [] # (
    right_p = [] # )
    
    for i in string:
        if i == '(':
            left_p.append(i)
        if i == ')': 
            if len(left_p) > 0:
                left_p.pop()
            else:
                return False
    return True
