def is_valid_IP(string):
    string = string.split(".")
    
    
    if (len(string) != 4):
        return False
    
    
    for section in string:
        if ' ' in section:
            return False
        if len(section) > 4:
            return False
        if section.isalpha() == True:
            return False
        if (0 <= int(section) <= 255) == False:
            return False
        if (section[0] == '0') and (section != 0):
            return False
    return True
