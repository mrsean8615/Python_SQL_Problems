# Sean Payne

import os

vacname = 'Farm Bunny'
guesses = []

x = 1
while x:
    if x != 4:
        
        #repeat output for incorrect guesses       
        if x > 1: 
            print('Try Again')
            print(f'{4 - x} guesses left')
            
        print(f'Attempt {x}')
        uinput = input('Guess my favorite vacuum cleaner: ')
        guesses.append(uinput)
        os.system('clear')

        #logic
        if uinput.casefold() == vacname.casefold():
            os.system('clear')
            print('Good Job!')
            print(f'It took you {x} try(s).')
            break
        
    #Outputs if user is correct
    else:
        os.system('clear')
        print('You have failed.')
        print(f'The answer is {vacname}')
        print(f'Your Guesses: {guesses[0]}, {guesses[1]}, {guesses[2]}.')
        break
    x += 1


        


        