### ICU-01 CPU ###

ICU-01 was something I made probably about a year ago, and just recently I discovered it again. I uploaded it here so that others could use it, and maybe get some use out of it. It was intended to be a compiler for a 1-bit CPU I was making at the time, but I never finished the project.  
  
There's only 16 (0 - 15) lines/addresses you can use, for a more realistic experience. Realistically, I would be too lazy to implement more than 16 addresses in memory.  
  
(also there's only 8 (0 - 7) different addresses in the output memory)

## How to Use BPL ##

If you want to use BPL, I'll have the instructions listed in the "BPL - Instructions" segment, but for now I'll just assume you've made your script. Once you run "bpl.py", you will see the prompt "File: ". This is where you enter the file you saved your BPL code to. Once it finishes compiling your script to assembly (and output some debug info I don't know if I removed that), it will give you the prompt "Save File: ". This is where you want the assembly version of your BPL program to be stored. After specifying that file, you will see the prompt "Enter file to save binary to: ". This is where you specify where you want to save the binary of your BPL program. After that, the program will exit, and you will be able to run the binary file with the emulator (emulator.py).

## How to Use The Assembly Language ##

The assembly instructions will be listed in the "ASM - Instructions" segment. I'm going to assume you've made a program already, so I won't be going over how to make a program in ASM. If you want, you could enter the entire program in the asm interface, but it's easier to make your program in a text file. In the case you've already made a program, just open up the "asm.py" file and type in "//cfile". Then, once given the prompt "File: ", enter the name of the file that your assembly program is in.

In the case you've entered your program in the asm interface, just type in "//compile" and it will compile your code.

## How to Use The Emulator ##

Once you start the emulator, it will give the prompt "File: ". This is where you put the file that contains the binary version of your code. After that, all you have to do is watch your code run.

## BPL - Instructions ###

zero? - checks if the result of the previous operation is zero  
load - loads either 1 or 0 into the A register  
write - writes the contents of the A register into specified memory address.  
stop - stops execution of the program  
&& - ANDs the A register with specified memory address  
|| - ORs the A register with specified memory address  
X - XORs the A register with specified memory address (must be capital "X")  
!write - writes the inverse of the A register to the specified memory address  
!load - loads the inverse of the specified memory address to the A register (value of memory address must be either 1 or 0)  
loadim - loads the specified value (either 1 or 0) into the A register  
-> - outputs to specified location  
<- - inputs from specified location (not fully implemented in the emulator)
goto - jumps to a specific location

## ASM - Instructions ##

jz - checks if the result of the previous operation is zero  
ld - loads either 1 or 0 into the A register  
wrt - writes the contents of the A register into specified memory address.  
hlt 0 - stops execution of the program  
and - ANDs the A register with specified memory address  
or - ORs the A register with specified memory address  
xor - XORs the A register with specified memory address (must be capital "X")  
wrc - writes the inverse of the A register to the specified memory address  
ldc - loads the inverse of the specified memory address to the A register (value of memory address must be either 1 or 0)  
ldi - loads the specified value (either 1 or 0) into the A register  
out - outputs to specified location  
in - inputs from specified location (not fully implemented in the emulator)
jmp - jumps to a specific location  
  
Note: "hlt" is "hlt 0" because of how operands work in the assembler.

## Thanks For Reading! ##