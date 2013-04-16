from PyQt4.QtGui import *
from PyQt4.QtCore import *
from gui import Ui_window
from util import load_program, instrucoes
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
        self._connect_edits()
        self.ui.pushButtonNext.clicked.connect(self.next_cpu)
        self.ui.tableWidget.itemChanged.connect(self._update_word)

    def next_cpu(self):
        try:
            info = self.gen.send(None)
            self.ui.lineEditStatus.setText(info)
            self.ui.lineEditPC.setText(hex(self.cpu.pc))
            self.ui.lineEditIR.setText(hex(self.cpu.ir))
            self.ui.lineEditAH.setText(hex(self.cpu.ula.ah))
            self.ui.lineEditBH.setText(hex(self.cpu.ula.bh))
            self.ui.lineEditAC.setText(hex(self.cpu.ula.ac))
            self.ui.lineEditAX.setText(hex(self.cpu.ax))
            self.ui.lineEditBX.setText(hex(self.cpu.bx))
            self.ui.lineEditCX.setText(hex(self.cpu.cx))
            self.ui.lineEditDX.setText(hex(self.cpu.dx))
            self.ui.lineEditSTS.setText(bin(self.cpu.sts))
            self.ui.lineEditInstruction.setText(instrucoes[self.cpu.ir])
            self._select_row(hex(self.cpu.pc))
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
            item_endereco.setFlags(item_endereco.flags() ^ Qt.ItemIsEditable)
            data = memory.operate(i, None, 0)
            if data is not None:
                data = hex(data)
            item_palavra = QTableWidgetItem(data)
            self.ui.tableWidget.setItem(i-1, 0, item_endereco)
            self.ui.tableWidget.setItem(i-1, 1, item_palavra)

    def _select_row(self, pc):
        item = self.ui.tableWidget.findItems(pc, Qt.MatchExactly)[0]
        self.ui.tableWidget.selectRow(item.row())
        self.ui.tableWidget.scrollToItem(item)

    def _update_word(self, item):
        self.cpu.bus.transfer(int(self.ui.tableWidget.item(item.row(), 0).text(), 16), int(item.text(), 16), 1)

    def _connect_edits(self):
        self.ui.lineEditAH.editingFinished.connect(self._update_register)
        self.ui.lineEditBH.editingFinished.connect(self._update_register)
        self.ui.lineEditAC.editingFinished.connect(self._update_register)

    def _update_register(self):
        sender = self.sender().objectName()
        value = int(self.sender().text(), 16)
        if sender == 'lineEditAH':
            self.cpu.ula.ah = value
        elif sender == 'lineEditBH':
            self.cpu.ula.bh = value
        elif sender == 'lineEditAC':
            self.cpu.ula.ac = value


if __name__ == '__main__':
    app = QApplication([])
    w = Orion()
    w.show()
    app.exec_()
