# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orion.ui'
#
# Created: Tue Apr 16 10:33:32 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName(_fromUtf8("window"))
        window.resize(746, 572)
        self.verticalLayout_2 = QtGui.QVBoxLayout(window)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tableWidget = QtGui.QTableWidget(window)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.groupBox = QtGui.QGroupBox(window)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.labelAX = QtGui.QLabel(self.groupBox)
        self.labelAX.setObjectName(_fromUtf8("labelAX"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelAX)
        self.lineEditAX = QtGui.QLineEdit(self.groupBox)
        self.lineEditAX.setObjectName(_fromUtf8("lineEditAX"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditAX)
        self.labelBX = QtGui.QLabel(self.groupBox)
        self.labelBX.setObjectName(_fromUtf8("labelBX"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelBX)
        self.lineEditBX = QtGui.QLineEdit(self.groupBox)
        self.lineEditBX.setObjectName(_fromUtf8("lineEditBX"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditBX)
        self.labelCX = QtGui.QLabel(self.groupBox)
        self.labelCX.setObjectName(_fromUtf8("labelCX"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelCX)
        self.lineEditCX = QtGui.QLineEdit(self.groupBox)
        self.lineEditCX.setObjectName(_fromUtf8("lineEditCX"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditCX)
        self.labelDX = QtGui.QLabel(self.groupBox)
        self.labelDX.setObjectName(_fromUtf8("labelDX"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelDX)
        self.lineEditDX = QtGui.QLineEdit(self.groupBox)
        self.lineEditDX.setObjectName(_fromUtf8("lineEditDX"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditDX)
        self.labelAH = QtGui.QLabel(self.groupBox)
        self.labelAH.setObjectName(_fromUtf8("labelAH"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.labelAH)
        self.lineEditAH = QtGui.QLineEdit(self.groupBox)
        self.lineEditAH.setObjectName(_fromUtf8("lineEditAH"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEditAH)
        self.labelBH = QtGui.QLabel(self.groupBox)
        self.labelBH.setObjectName(_fromUtf8("labelBH"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.labelBH)
        self.lineEditBH = QtGui.QLineEdit(self.groupBox)
        self.lineEditBH.setObjectName(_fromUtf8("lineEditBH"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEditBH)
        self.labelAC = QtGui.QLabel(self.groupBox)
        self.labelAC.setObjectName(_fromUtf8("labelAC"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.labelAC)
        self.lineEditAC = QtGui.QLineEdit(self.groupBox)
        self.lineEditAC.setObjectName(_fromUtf8("lineEditAC"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEditAC)
        self.labelIR = QtGui.QLabel(self.groupBox)
        self.labelIR.setObjectName(_fromUtf8("labelIR"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.labelIR)
        self.lineEditIR = QtGui.QLineEdit(self.groupBox)
        self.lineEditIR.setObjectName(_fromUtf8("lineEditIR"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEditIR)
        self.labelPC = QtGui.QLabel(self.groupBox)
        self.labelPC.setObjectName(_fromUtf8("labelPC"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.LabelRole, self.labelPC)
        self.lineEditPC = QtGui.QLineEdit(self.groupBox)
        self.lineEditPC.setObjectName(_fromUtf8("lineEditPC"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.lineEditPC)
        self.labelSTS = QtGui.QLabel(self.groupBox)
        self.labelSTS.setObjectName(_fromUtf8("labelSTS"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.LabelRole, self.labelSTS)
        self.lineEditSTS = QtGui.QLineEdit(self.groupBox)
        self.lineEditSTS.setObjectName(_fromUtf8("lineEditSTS"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.FieldRole, self.lineEditSTS)
        self.labelStatus = QtGui.QLabel(self.groupBox)
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.formLayout_2.setWidget(11, QtGui.QFormLayout.LabelRole, self.labelStatus)
        self.lineEditStatus = QtGui.QLineEdit(self.groupBox)
        self.lineEditStatus.setReadOnly(True)
        self.lineEditStatus.setObjectName(_fromUtf8("lineEditStatus"))
        self.formLayout_2.setWidget(11, QtGui.QFormLayout.FieldRole, self.lineEditStatus)
        self.pushButtonNext = QtGui.QPushButton(self.groupBox)
        self.pushButtonNext.setObjectName(_fromUtf8("pushButtonNext"))
        self.formLayout_2.setWidget(12, QtGui.QFormLayout.FieldRole, self.pushButtonNext)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        window.setWindowTitle(_translate("window", "Orion", None))
        self.labelAX.setText(_translate("window", "AX", None))
        self.labelBX.setText(_translate("window", "BX", None))
        self.labelCX.setText(_translate("window", "CX", None))
        self.labelDX.setText(_translate("window", "DX", None))
        self.labelAH.setText(_translate("window", "AH", None))
        self.labelBH.setText(_translate("window", "BH", None))
        self.labelAC.setText(_translate("window", "AC", None))
        self.labelIR.setText(_translate("window", "IR", None))
        self.labelPC.setText(_translate("window", "PC", None))
        self.labelSTS.setText(_translate("window", "STS", None))
        self.labelStatus.setText(_translate("window", "Status", None))
        self.lineEditStatus.setText(_translate("window", "Início", None))
        self.pushButtonNext.setText(_translate("window", "Próximo", None))

