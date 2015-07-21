def solution(string,markers):
	
    for i in range(len(markers)):
        marker_index = -1
		
        if (string == markers[i]):
            return ''
			
        while (string.find(markers[i], marker_index + 1) != -1):		
            marker_index = string.find(markers[i], marker_index + 1)
            newline_index = string.find('\n', marker_index + 1) # finds the next \n after a marker     			
            if (newline_index == -1):
                string = string[:marker_index].rstrip(' ')
                break
            else:
                string = string[:marker_index].rstrip(' ') + string[newline_index:len(string)]   		
				
    return string 