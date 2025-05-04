#
import class_a

def main():

 d = class_a.die()

 while True:
  
  d.roll()
  print(d)

  option = input('Do you wish to continue?(Y/N): ')
  if option != 'Y':
   
   print('Program Exiting...')
   break
  
main()



