#
def get_hamming_distance(dna1, dna2):
    distance = 0
    for i in range(len(dna1)):
       if dna1[i] != dna2[i]:
          distance += 1
    return distance

        
    

def get_dna_complement(dna):
    complement = ''
    for character in (dna):
        if character == 'A':
            complement += 'T'
        elif character == 'T':
            complement += 'A'
        elif character == 'C':
            complement += 'G'
        elif character == 'G':
            complement += 'C'
            return complement

        
    

    



    