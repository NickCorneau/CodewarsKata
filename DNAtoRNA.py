def DNAtoRNA(dna):
    array = []
    for i in dna:
        if (i == 'T'):
            i = 'U'
        array.append(i)
    return ''.join(array)
