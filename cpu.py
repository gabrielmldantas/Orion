from bus import Bus

class Ula:
    def __init__(self, cpu):
        self.ah = 0
        self.bh = 0
        self.ac = 0
        self._cpu = cpu

    def execute(self, opcode):
        if opcode == 0x1:
            self._add()
        elif opcode == 0x2:
            self._sub()
        elif opcode in (0x6, 0x7):
            self._cmp()

    def _add(self):
        self.ac = self.ah + self.bh

    def _sub(self):
        self.ac = self.ah - self.bh

    def _cmp(self):
        if self.ah != self.bh:
            self._cpu.sts |= 0x0001
        else:
            self._cpu.sts |= 0x0000

class InstructionDecoder:
    def __init__(self, cpu):
        self._cpu = cpu

    def decode(self, word):
        opcode = (word & 0xF000) >> 12
        address = word & 0x0FFF
        self._cpu.ir = opcode
        return address


class ExecutionUnit:
    def __init__(self, cpu):
        self._cpu = cpu

    def execute(self, opcode, address):
        if opcode == 0x4:
            self._jmp(address)
        elif opcode == 0x5:
            self._hlt()
        elif opcode == 0x0:
            self._nop()
        elif opcode == 0x3:
            self._mov(address)

    def _jmp(self, address):
        self._cpu.pc = address

    def _hlt(self):
       self._cpu.halt = True

    def _nop(self):
       pass

    def _mov(self, address):
       print("MOV", address)


class ControlUnit:
    def __init__(self, cpu):
        self._cpu = cpu

    def execution_cycle(self):
        while not self._cpu.halt:
            word = self._fetch_word()
            yield "Decodificação"
            address = self._cpu.instruction_decoder.decode(word)
            if self._is_ula_instruction(self._cpu.ir):
                yield "Execução na ULA"
                self._cpu.ula.execute(self._cpu.ir)
            else:
                yield "Execução na UE"
                self._cpu.execution_unit.execute(self._cpu.ir, address)
            if not self._verify_jump(self._cpu.ir, address) and not self._cpu.halt:
                self._cpu.pc += 1
                yield "PC Incrementado"
            yield

    def _fetch_word(self):
        return self._cpu.bus.transfer(self._cpu.pc, None, 0)

    def _is_ula_instruction(self, opcode):
        return opcode in (0x1, 0x2, 0x6, 0x7)

    def _verify_jump(self, opcode, address):
        if opcode == 0x4:
            return True
        if opcode == 0x6:
            if self._cpu.sts & 0x0001 == 1:
                self._cpu.pc = address
                return True
        if opcode == 0x7:
            if self._cpu.sts & 0x0001 == 0:
                self._cpu.pc = address
                return True
        return False

class Cpu:
    def __init__(self, bus):
        self.bus = bus
        self.ula = Ula(self)
        self.control_unit = ControlUnit(self)
        self.execution_unit = ExecutionUnit(self)
        self.instruction_decoder = InstructionDecoder(self)
        self.halt = False
        self.ax = 0
        self.bx = 0
        self.cx = 0
        self.dx = 0
        self.ir = 0
        self.pc = 0
        self.sts = 0

    def start(self):
        return self.control_unit.execution_cycle()

