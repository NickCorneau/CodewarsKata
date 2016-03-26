def Descending_Order(num):  
    # base case
    if (num == 0):
        return 0

    # initialize empty array
    arra = []

    # base 10 number so remove the last digit
    # using 10 as factor, append it to an array
    while (num > 0):
        digit = num % 10
        num /= 10
        arra.append(digit)
    
    # sort the array in reverse order        
    arra.sort(reverse = True)
    
    # takes list of ints and returns as single int
    def magic(number):
        return int(''.join(str(i) for i in number))
    
    ans = magic(arra)        
    return ans