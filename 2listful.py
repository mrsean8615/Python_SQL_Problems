# Sean Payne
import os

names = []
x = True
entries = 0


#Appends user input the names list and checks if the user wants to input another name.
while x:
    uinput = input('Enter a First Name or press enter to end the list: ')
    if uinput:
        names.append(uinput)
        print(f'{uinput} has been added to the list')
        entries += 1
    else:
        print('First Name List: ')
        x = False

#Lists all inputs entered
for name in names:
    print(name)

#final output
print(f'You entered {entries} first names.')
