import collections

def get_score(dice): 
    print(dice)
 
    score = 0
    
    counter = collections.Counter(dice)
    

    if (sorted(dice) == range(1,7)):
        return 1000

    
    arr = []
    for key, values in counter.iteritems():
    
        if (values == 1):
            if (key == 1):
                score = score + 100
            elif (key == 5):
                score = score + 50
            
        if (values == 2):
            arr.append(values)
            if (sum(arr) == 6):
                return 750
            elif (key == 1):
                score = score + 200
            elif (key == 5):
                score = score + 100
                
        if (values == 3):
            if (key == 1):
                score = score + 1000
            else:
                score = score + (key * 100)
                
        elif (values == 4):
            if (key == 1):
                score = (score + 1000) * 2
            else:
                score = score + ((key * 100) * 2)
                
        elif (values == 5):
            if (key == 1):
                score = (score + 1000) * 3
            else:
                score = score + ((key * 100) * 3)
                
        elif (values == 6):
            if (key == 1):
                return 4000
            else:
                return ((key * 100) * 4)
    

      
    return score or "Zonk"
