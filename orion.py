from PyQt4.QtGui import *
from gui import Ui_window
from util import load_program
from bus import Bus
from memory import Memory
from cpu import Cpu


class Orion(QWidget):
    def __init__(self):
        super(Orion, self).__init__()
        self.ui = Ui_window()
        self.ui.setupUi(self)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Endereço', 'Palavra'])
        memory = Memory()
        load_program(memory)
        self.ui.tableWidget.setRowCount(len(memory))
        self._init_cpu(memory)
        self._fill_table(memory)
        self.ui.pushButtonNext.clicked.connect(self.next_cpu)

    def next_cpu(self):
        try:
            info = self.gen.send(None)
            self.ui.lineEditPC.setText(hex(self.cpu.pc))
            self.ui.lineEditIR.setText(hex(self.cpu.ir))
        except StopIteration:
            QMessageBox.information(self, "Orion", "Execução Finalizada")

    def _init_cpu(self, memory):
        bus = Bus(memory)
        self.cpu = Cpu(bus)
        self.cpu.pc = 0x200
        self.gen = self.cpu.start()

    def _fill_table(self, memory):
        for i in range(1, len(memory)):
            item_endereco = QTableWidgetItem(hex(i))
            data = memory.operate(i, None, 0)
            if data:
                data = hex(data)
            item_palavra = QTableWidgetItem(data)
            self.ui.tableWidget.setItem(i-1, 0, item_endereco)
            self.ui.tableWidget.setItem(i-1, 1, item_palavra)

if __name__ == '__main__':
    app = QApplication([])
    w = Orion()
    w.show()
    app.exec_()
