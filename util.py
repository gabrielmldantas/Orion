def load_program(memory):
    with open('program.txt') as program:
        for line in program:
            address, word = line.split(':')
            memory.operate(int(address, 16), int(word, 16), 1)
