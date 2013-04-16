class Memory:
    def __init__(self):
        self._data = []
        for i in range(1, 0xFFF + 1):
            self._data.append(None)
        
    def operate(self, address, data, operation):
        if operation == 0:
            return self._data[address]
        elif operation == 1:
            self._data[address] = data

    def __len__(self):
        return len(self._data)
