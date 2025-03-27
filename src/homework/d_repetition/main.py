import repetition

def main():
    print('1-Factorial')
    print('2-Sum odd numbers')
    print('3-Exit')


    option = input('Select an option: ')

    if option == '1':
        num_str = int(input('Enter a number 1-9: '))
        num = int(num_str)
        if 1 <= num <= 9:
            result = repetition.get_factorial(num)
            print(f'The Factorial of {num} is {result}')
        else: 
           print('Invalid Number')

    elif option == '2':
        num_str = int(input('Enter a number 1-99: '))
        num = int(num_str)
        if 1 <= num <= 99:
            result = repetition.sum_odd_numbers(num)
            print(f'The sum of odd numbers for {num} is {result}')
                                                        
        else: 
         print('Invalid Number')

    elif option == '3':
       exit = input('Do you wish to exit? Y or N: ')
       if exit == 'Y':
          print('Program Exiting...')
          
       else: 
             print('Try again')

            
    
    
                
main()