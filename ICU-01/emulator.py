###########################
# ICU-01 Emulator by Stev #
###########################

import time, os

program_mem = []
data_mem = []
output_mem = []
result = '0'
a_register = '0'

def init():
    for i in range(16):
        program_mem.append('0000')
        data_mem.append('0000')

    for i in range(8):
        output_mem.append('0000')
    
def read_program_mem(addr):
    return program_mem[addr]

def read_data_mem(addr):
    return data_mem[addr]

def read_output_mem(addr):
    return output_mem[addr]

def write_mem(addr, val):
    data_mem.pop(addr)
    data_mem.insert(addr, val)

def write_program_mem(addr, val):
    program_mem.pop(addr)
    program_mem.insert(addr, val)

def write_output_mem(addr, val):
    output_mem.pop(addr)
    output_mem.insert(addr, val)

def to_decimal(number):
    bin_to_dec = {'0000':0, '0001':1, '0010':2, '0011':3, '0100':4, '0101':5, '0110':6, '0111':7, '1000':8,
                  '1001':9, '1010':10, '1011':11, '1100':12, '1101':13, '1110':14, '1111':15}
    
    return bin_to_dec[number]

def run():
    global result
    global a_register

    pc = 0

    while True:
        if read_program_mem(pc) == '0000':
            if result == '0':
                pc = to_decimal(read_data_mem(pc))
                continue
        
        if read_program_mem(pc) == '0001':
            a_register = read_data_mem(to_decimal(read_data_mem(pc)))
        
        if read_program_mem(pc) == '0010':
            write_mem(to_decimal(read_data_mem(pc)), a_register)
        
        if read_program_mem(pc) == '0100':
            if a_register == '0001' and read_data_mem(pc) == '0001':
                result = '1'
            else:
                result = '0'
        
        if read_program_mem(pc) == '0101':
            if a_register == '0001' or read_data_mem(pc) == '0001':
                result = '1'
            else:
                result = '0'
        
        if read_program_mem(pc) == '0110':
            if (a_register == '0001' or read_data_mem(pc) == '0001') and not (a_register and read_data_mem(pc) == '0001'):
                result = '1'
            else:
                result = '0'
        
        if read_program_mem(pc) == '0111':
            if a_register == '0001':
                write_mem(to_decimal(read_data_mem(pc)), '0000')
            if a_register == '0000':
                write_mem(to_decimal(read_data_mem(pc)), '0001')
        
        if read_program_mem(pc) == '1000':
            if read_data_mem(to_decimal(read_data_mem(pc))) == '0001':
                a_register = '0000'
            if read_data_mem(to_decimal(read_data_mem(pc))) == '0000':
                a_register = '0001'
        
        if read_program_mem(pc) == '1001':
            if read_data_mem(pc) == '0001':
                a_register = '0001'
            if read_data_mem(pc) == '0000':
                a_register = '0000'
        
        if read_program_mem(pc) == '1010':
            write_output_mem(to_decimal(read_data_mem(pc)), a_register)
        
        if read_program_mem(pc) == '1011':
            a_register = read_output_mem(to_decimal(read_data_mem(pc)))
        
        if read_program_mem(pc) == '1111':
            pc = to_decimal(read_data_mem(pc))
            continue
        
        if read_program_mem(pc) == '0011':
            break

        pc += 1

        print("Output:")
        print(output_mem)
        #print(a_register)
        #print("Program memory:")
        #print(program_mem)
        #print(pc)

        time.sleep(.5)

if __name__ == '__main__':
    init()

    idx = 0

    fl = input("Enter file to run: ")

    all_files = os.listdir()

    if fl in all_files:
        compiled = open(fl, 'r')
        opcode = ''
        operand = ''
        is_operand = False

        for i in compiled.read():
            if i == ' ':
                is_operand = True
            elif is_operand == False and i != ' ':
                opcode += i
            elif is_operand == True and i != ' ':
                operand += i

            if i == '\n':
                write_program_mem(idx, opcode)
                write_mem(idx, operand.replace('\n', ''))

                opcode = ''
                operand = ''
                is_operand = False

                idx += 1
        
        compiled.close()
        
        run()

        input("Press enter to exit\n")
    else:
        print("Error: No such file")
        quit()