def DNAtoRNA(dna):
    # create a function which returns an RNA sequence from the given DNA sequence
    array = []
    for i in dna:
        if (i == 'T'):
            i = 'U'
        array.append(i)
    return ''.join(array)