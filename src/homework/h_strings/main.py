#
import strings

def main():
    
    print('1-Hamming Distance')
    print('2-Dna complement')
    print('3-Exit')


    option = input('Select an option: ')

    if option == '1':
        dna1 = input('Enter dna1: ')
        dna2 = input('Enter dna2: ')
        result = strings.get_hamming_distance(dna1, dna2)
        print(f'Hamming distance of string is {result}')

    elif option == '2':
        dna = input('Enter dna string: ')
        result = strings.get_dna_complement(dna)
        print(f'String dna complement is {result}')

    elif option == '3':
        print('Program Exiting...')
    else:
        print('Invalid Option')

main()


    

