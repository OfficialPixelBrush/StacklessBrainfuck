
import argparse

prg = ""
memSize = 50

parser = argparse.ArgumentParser("Stackless Brainfuck")
parser.add_argument("file", help="The .bf file to execute", type=str)
parser.add_argument("-mem", help="Size of the internal Memory (Default: 50)", type=int)
args = parser.parse_args()

if (args.file == ""):
    print("No brainfuck program was passed!")
    exit()

if (args.mem is not None):
    memSize = args.mem
    print(memSize)

with open(args.file, 'r') as file:
    prg = file.read()

if (prg == ""):
    print("Empty program loaded!")
    exit()

mem = []
mem = [0 for i in range(30000)] 

pc = 0
ptr = 0
bracketCounter = 0
goalBracket = 0
debug = False

while (pc < len(prg)):
    inst = prg[pc]

    if (debug):
        print(str(pc) + ": " + str(inst) + "; ", end='')
    # Classic Code Interpretation
    if(inst=="<"):
        ptr -= 1
    elif(inst==">"):
        ptr += 1
    elif(inst=="+"):
        mem[ptr] += 1
    elif(inst=="-"):
        mem[ptr] -= 1
    elif(inst=="."):
        print(chr(mem[ptr]), end='')
    elif(inst==","):
        pc = pc
        # Nothing
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