#
import lists

def main():
    
    number_list = []

    while True:
        print("1 - Show list low/high values")
        print("2 - Exit")

        option = input("Enter option: ")

        if option == "1":
            
            while True:
                    value = int(input("Enter a list value: "))
                    number_list.append(value)
                    if len(number_list) >= 3:
                        other = input("Do you want to enter another value? (y/n): ")
                        if other != "y":
                            break
                    else:
                        other = input("Do you want to enter another value? (y/n): ")
                        if other != "y":
                            break
                    continue
            
            if number_list:
                print("List values:", number_list)
                print("Lowest value:", lists.get_lowest_list_value(number_list))
                print("Highest value:", lists.get_highest_list_value(number_list))

        elif option == "2":
            print("Program Exiting...")
            break
main()
                

                  

             
    

                
