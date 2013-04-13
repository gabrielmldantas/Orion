from memory import Memory
from bus import Bus
from cpu import Cpu

def load_program(memory):
    with open('program.txt') as program:
        for line in program:
            address, word = line.split(':')
            memory.operate(int(address, 16), int(word, 16), 1)

if __name__ == '__main__':
    memory = Memory()

    load_program(memory)

    bus = Bus(memory)
    cpu = Cpu(bus)
    cpu.pc = 0x200
    cpu.start()
