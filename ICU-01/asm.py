############################
# ICU-01 Assembler by Stev #
############################

import os

global offset

DIGITS = '0123456789'
mem_location = 0
offset = 0

test = 'commit-test'

changelog = ['6/18/23 (1.30):\n-fixed bugs\n-added cfile command\n-added file compiling', '3/1/23 (1.21):\n-fixed bugs', '3/1/23 (1.20):\n-set up OS interface\n-changed input method\n-added commands',
             '2/28/23 (1.10):\n-added start address output\n-added changelog']

commands = {'jz':'0000', 'ld':'0001', 'wrt':'0010', 'hlt':'0011', 'and':'0100', 'or':'0101', 'xor':'0110',
            'wrc':'0111', 'ldc':'1000', 'ldi':'1001', 'out':'1010', 'in':'1011', 'jmp':'1111'}

numbers_bin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000',
               '9':'1001', '10':'1010', '11':'1011', '12':'1100', '13':'1101', '14':'1110', '15':'1111'}

version = '1.30'
fl = 'out.txt'

if __name__ == '__main__':
    fl = input("Enter save file: ")

    print(f"OS {version}\n")
    print("type \"//help\" for help with commands")

out = []
cmds = []
for i in range(16):
    cmds.append('')

def compile_():
    global offset
    for i in range(len(cmds)):
        opcode = ''
        operand = ''
        space = False
        comment = False
        for j in cmds[i]:
            if j == ';':
                comment = True
            if j not in DIGITS and j != ' ' and space == False and comment == False and cmds[i] != '\n':
                opcode += j
            elif j != ' ' and space == True and comment == False:
                operand += j
            elif j == ' ' and comment == False:
                space = True

        if opcode in commands and comment == False:
            if int(operand) <= len(numbers_bin) - 1:
                if opcode == 'jz' or opcode == 'jmp': out.append([commands[opcode], numbers_bin[str(int(operand) + offset)]])
                else: out.append([commands[opcode], numbers_bin[operand.replace('\n', '')]])
            else:
                print('Error: overflow')
                out.clear()
                break
    
    with open(fl, 'w') as f:
        for i in out:
            f.write(f'{i[0]} {i[1]}\n')

def compile_file(file_to_open):
    global mem_location

    if file_to_open in os.listdir():
        f = open(file_to_open, 'r')

        cmd = ''

        for i in f.read():
            cmd += i

            if i == '\n':
                cmds.pop(mem_location)
                cmds.insert(mem_location, cmd)

                cmd = ''
                mem_location += 1

        compile_()

        f.close()

        mem_location = 0
    else:
        print("Error: file doesn't exist")

def addr(a):
    global mem_location
    str_ = ''
    for i in a:
        if i in DIGITS:
            str_ += i
    mem_location = int(str_)

def list_():
    for i in out:
        print(i[0], i[1])

if __name__ == '__main__':
    while True:
        cmd = input(f'{mem_location}: ')
        if '//' in cmd:
            if 'compile' in cmd:
                compile_()
            elif 'run' in cmd:
                print(f'Running a program is not supported on version {version}.')
            elif 'list' in cmd:
                list_()
            elif 'help' in cmd:
                print('Commands:\ncompile\nrun\nlist\nhelp\nquit\nchangelog\naddr\ncfile')
                print("\nInstructions:")
                for i in commands:
                    print(i)
                print("***NOTE: IN ORDER FOR THE \"hlt\" COMMAND TO WORK, YOU NEED TO PUT \"hlt 0\"!!!***")
            #elif 'loadbin' in cmd:
            #    for i in cmds:
            #        out.append(i)
            elif 'quit' in cmd:
                quit()
            elif 'addr' in cmd:
                addr(cmd)
            elif 'changelog' in cmd:
                print('Changelog:')
                for i in changelog:
                    print(i)
            elif 'cfile' in cmd:
                file_to_open = input("Enter file: ")
                compile_file(file_to_open)
            else:
                print("Command not recognized.")
        else:
            cmds.pop(mem_location)
            cmds.insert(mem_location, cmd)
        
            mem_location += 1