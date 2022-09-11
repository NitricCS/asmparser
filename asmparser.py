# ASM file parser
#
# Kirill Borisov, 108144

import re

def getcode():
    code = []
    f = open("asm")
    while (True):
        line = f.readline()
        if line[0] == "[":
            code.append(line[11:])
        if ("Kernel Text Segment" in line) or (not line):
            break
    f.close()
    return code


def format(code):
    f = open("memory.txt", "w")

    inst = "16\'d00 : inst = 32\'h34000000;  // ori  $0, $0, 0\n"
    inst += "16\'d01 : inst = 32\'h10000000;  // beq  $0, $0, 0\n"
    f.write(inst)
    
    inst_index = 2
    for line in code:
        if ("jr" in line) and ("$ra" in line):
            offset = hex(65536 - inst_index)
            offset = "1000" + offset[2:]
            inst = "16\'d" + str(inst_index) + " : inst = 32\'h"
            inst += offset + ";  // beq $0, $0, -" + str(inst_index);
        else:
            inst = "16\'d" + "{:02}".format(inst_index) + " : inst = 32\'h" + line[:8] + ";"
            if ";" in line:
                cut = re.split("; ", line)[1]
                cut = re.split(": ", cut)[1]
                inst += "  // " + cut
            else:
                inst += "  // " + line[10:]
        
        if not (inst.endswith("\n")):
            inst += "\n"
        f.write(inst)
        inst_index += 1
    
    f.close()


if __name__ == "__main__":
    code = getcode()
    format(code)