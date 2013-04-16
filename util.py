def load_program(memory):
    with open('program.txt') as program:
        for line in program:
            address, word = line.split(':')
            memory.operate(int(address, 16), int(word, 16), 1)

instrucoes = {
    0x1: "ADD",
    0x2: "SUB",
    0x3: "MOV",
    0x4: "JMP",
    0x5: "HLT",
    0x6: "JNE",
    0x7: "JE",
    0x0: "NOP"
}