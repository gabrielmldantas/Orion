from memory import Memory

class Bus:
    def __init__(self, memory):
        self._memory = memory

    def transfer(self, address, data, operation):
        return self._memory.operate(address, data, operation)
