def get_factorial(num):
    total = 0
    
    for val in range(0, num):
        total = 1

    for i in range(1, num +1):

            total *= i
    

    return total

def sum_odd_numbers(num):
     
     total = 0
     i = 1
     while i <= num:
          total += i
          i += 2

     return total
          

def display_menu():
     while True:
         print("1-Factorial")
         print("2-Sum odd numbers")
         print("3-Exit")

         option = input('Select an option: ')

         if option == '1':
              while True:
                   num_str = int(input('Enter Number (1-9):'))
                   num = int(num_str)
                   if 1<= num <= 9:
                        result = get_factorial(num)

    


   
    