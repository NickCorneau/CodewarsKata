def luck_check(string):

    # if odd length, remove middle element
    if (len(string) % 2 != 0):
        string = string[:len(string)/2] + string[len(string)/2 + 1:]
  
    left_half = string[:len(string)/2]
    right_half = string[len(string)/2:]
    
    left_sum = sum(int(v) for v in left_half)
    right_sum = sum(int(v) for v in right_half)
    
    if (left_sum == right_sum):
        return True
    else:
        return False