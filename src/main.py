
instructions = {
 "NOP" : "0000",    # No Operation
 "LDA" : "0001",    # Load A Register
 "ADD" : "0010",    # Add 
 "SUB" : "0011",    # Subtract
 "STA" : "0100",    # Store A
 "LDI" : "0101",    # Load Immediate
 "JMP" : "0110",    # Jump
 "JC"  : "0111",    # Jump Carry
 "JZ"  : "1000",    # Jump Zero
 "OUT" : "1110",    # Enable Output
 "HLT" : "1111"     # Halt Clock
}

machine_code = {}

def print_code():
    for key, value in machine_code.items():
        print(key + " " + value)

while(True):
    
    print("Enter OpCode and Data: ")
    line = str(input())

    if (line == "print"):
        print_code()
        break

    line = line.split(" ", )

    if (len(line) != 2):
        print("Format must be: [OPCODE] [DATA]")
    else:
        opcode = line[0]
        data = line[1]

        if (opcode not in instructions or len(data) != 4):
            print("Invalid OpCode or Data")
        else:
            machine_code[instructions.get(opcode)] = data;




