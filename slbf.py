import sys
import argparse

prg = ""
memSize = 50

parser = argparse.ArgumentParser("Stackless Brainfuck")
parser.add_argument("file", help="The .bf file to execute", type=str)
parser.add_argument("-mem_size", help="Size of the internal Memory (Default: 50)", type=int)
parser.add_argument("-debug", help="Prints out debug information.", action='store_true')
parser.add_argument("-max", help="Limits the number of instructions that're run.", type=int)
parser.add_argument("-mem_print", help="Prints out memory contents after max is reached.", action='store_true')
args = parser.parse_args()

if (args.file == ""):
    print("No brainfuck program was passed!")
    exit()

if (args.mem_size is not None):
    memSize = args.mem_size
    print(memSize)

if (args.max is not None):
    maxInstructions = args.max

with open(args.file, 'r') as file:
    prg = file.read()

if (prg == ""):
    print("Empty program loaded!")
    exit()

mem = []
mem = [0 for i in range(memSize)] 

pc = 0
ptr = 0
bracketCounter = 0
goalBracket = 0
debug = args.debug

while (pc < len(prg)):
    inst = prg[pc]

    if (debug):
        print(str(pc) + ": " + str(inst) + "; ", end='')
    # Classic Code Interpretation
    if(inst=="<"):
        if (ptr-1 < 0):
            ptr = memSize-1
        else:
            ptr -= 1
    elif(inst==">"):
        if (ptr+1 > memSize-1):
            ptr = 0
        else:
            ptr += 1
    elif(inst=="+"):
        if (mem[ptr]-1 > 255):
            mem[ptr] = 0
        else:
            mem[ptr] += 1
    elif(inst=="-"):
        if (mem[ptr]-1 < 0):
            mem[ptr] = 255
        else:
            mem[ptr] -= 1
    elif(inst=="."):
        print(chr(mem[ptr]), end='')
    elif(inst==","):
        getInput = input("?:")
        if (getInput != ""):
            mem[ptr] = ord(getInput[0])
    elif(inst=="["):
        bracketCounter += 1
        if (mem[ptr]==0):
            goalBracket = bracketCounter
            # Search for the matching bracket
            searching = True
            while(searching):
                pc += 1
                if (prg[pc]=="["):
                    bracketCounter += 1
                elif (prg[pc]=="]"):
                    bracketCounter -= 1
                if (goalBracket == bracketCounter+1):
                    searching = False
    elif(inst=="]"):
        bracketCounter -= 1
        if (mem[ptr]!=0):
            goalBracket = bracketCounter
            # Search for the matching bracket
            searching = True
            while(searching):
                pc -= 1
                if (prg[pc]=="["):
                    bracketCounter += 1
                elif (prg[pc]=="]"):
                    bracketCounter -= 1
                if (goalBracket == bracketCounter-1):
                    searching = False
    pc += 1
    if (debug):
        print(str(bracketCounter) + "; " + (str(goalBracket)))
        print(mem)

    if (args.max is not None):
        if (maxInstructions <= 0):
            break
        else:
            maxInstructions -= 1

print("")
if (args.mem_print):
    print(mem)