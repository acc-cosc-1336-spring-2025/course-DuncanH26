#
import dictionary
def main():

 inventory = {}
 while True:
        print('1-Add or update item')
        print('2-Delete Item')
        print('3-Exit')

        option = input('Select an option: ')

        if option == '1':
            item_name = (input('Enter widget name: '))
            amount = int(input('Enter widget quantity: '))
            dictionary.add_inventory(inventory, item_name, amount )
            print(inventory)

        elif option == '2':
           widget_name = (input('Enter widget name: '))
           result =  dictionary.remove_inventory_widget(inventory, widget_name)
           print(result)
           print(f'Updated Inventory: {widget_name}')
            

        elif option == '3':
            print('Program exiting...')
            exit()
            
            

main()

        