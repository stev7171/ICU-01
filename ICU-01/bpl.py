############################
# BPL FOR ICU-01 (by stev) #
############################

import asm, os

file_to_open = input("File: ")

if file_to_open in os.listdir():
    fl = open(file_to_open, 'r')

    opcode = ''
    operand = ''
    is_operand = False

    label = ''
    is_label = False

    variable = ''
    is_var = False

    labels = {}
    variables = {}

    address = 0

    out = []

    commands = {'zero?':'jz', 'load':'ld', 'write':'wrt', 'stop':'hlt 0', '&&':'and', '||':'or', 'X':'xor',
                '!write':'wrc', '!load':'ldc', 'loadim':'ldi', '->':'out', '<-':'in', 'goto':'jmp'}

    for i in fl.read():
            if i == ' ':
                is_operand = True
            
            elif i != ' ' and is_operand == False:
                opcode += i
            elif i != ' ' and is_operand == True:
                operand += i

            if i == '\n':
                
                op = opcode.replace('\n', '')
                oper = operand.replace('\n', '')

                if op in commands:
                    if op == 'stop':
                        out.append(f'{commands[op]}')
                    else:
                        out.append(f'{commands[op]} {oper}')
                else:
                    print("Error: Unknown command")
                    out.clear()
                    quit()
                
                opcode = ''
                operand = ''
                is_operand = False

    fl.close()

    print(out)

    save_file = input("Save file: ")

    with open(save_file, 'w') as f:
            for i in out:
                f.write(i + '\n')

    bin_file = input("Enter file to save binary to: ")
    asm.fl = bin_file

    asm.compile_file(save_file)
else:
    print("Error: File does not exist.")
    quit()