input_instruction = ''
while 1==1:
    input_instruction = input('Enter Command ')
    print(input_instruction.upper())
    if input_instruction.upper() == 'START':
        print('Car Started')
        break
    elif input_instruction.upper() == 'STOP':
        print('Car Stopped')
        break
    elif input_instruction.upper() == 'QUIT':
        print('Quit Game')
        break
    else:
        print('Please enter correct command')