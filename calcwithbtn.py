# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calcwithbtn.ui'
#
# Created: Wed Dec 24 19:45:14 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(364, 320)
        self.bclear = QtGui.QPushButton(Dialog)
        self.bclear.setGeometry(QtCore.QRect(10, 290, 251, 27))
        self.bclear.setObjectName(_fromUtf8("bclear"))
        self.num = QtGui.QLabel(Dialog)
        self.num.setGeometry(QtCore.QRect(40, 30, 271, 61))
        self.num.setText(_fromUtf8(""))
        self.num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.num.setObjectName(_fromUtf8("num"))
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(10, 130, 340, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.b1 = QtGui.QPushButton(self.splitter)
        self.b1.setObjectName(_fromUtf8("b1"))
        self.b2 = QtGui.QPushButton(self.splitter)
        self.b2.setObjectName(_fromUtf8("b2"))
        self.b3 = QtGui.QPushButton(self.splitter)
        self.b3.setObjectName(_fromUtf8("b3"))
        self.add = QtGui.QPushButton(self.splitter)
        self.add.setObjectName(_fromUtf8("add"))
        self.splitter_2 = QtGui.QSplitter(Dialog)
        self.splitter_2.setGeometry(QtCore.QRect(10, 170, 340, 27))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.b4 = QtGui.QPushButton(self.splitter_2)
        self.b4.setObjectName(_fromUtf8("b4"))
        self.b5 = QtGui.QPushButton(self.splitter_2)
        self.b5.setObjectName(_fromUtf8("b5"))
        self.b6 = QtGui.QPushButton(self.splitter_2)
        self.b6.setObjectName(_fromUtf8("b6"))
        self.sub = QtGui.QPushButton(self.splitter_2)
        self.sub.setObjectName(_fromUtf8("sub"))
        self.splitter_3 = QtGui.QSplitter(Dialog)
        self.splitter_3.setGeometry(QtCore.QRect(10, 210, 340, 27))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.b7 = QtGui.QPushButton(self.splitter_3)
        self.b7.setObjectName(_fromUtf8("b7"))
        self.b8 = QtGui.QPushButton(self.splitter_3)
        self.b8.setObjectName(_fromUtf8("b8"))
        self.b9 = QtGui.QPushButton(self.splitter_3)
        self.b9.setObjectName(_fromUtf8("b9"))
        self.mul = QtGui.QPushButton(self.splitter_3)
        self.mul.setObjectName(_fromUtf8("mul"))
        self.bspace = QtGui.QPushButton(Dialog)
        self.bspace.setGeometry(QtCore.QRect(270, 290, 81, 27))
        self.bspace.setObjectName(_fromUtf8("bspace"))
        self.splitter_4 = QtGui.QSplitter(Dialog)
        self.splitter_4.setGeometry(QtCore.QRect(10, 250, 340, 27))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.dotbtn = QtGui.QPushButton(self.splitter_4)
        self.dotbtn.setObjectName(_fromUtf8("dotbtn"))
        self.b0 = QtGui.QPushButton(self.splitter_4)
        self.b0.setObjectName(_fromUtf8("b0"))
        self.calc = QtGui.QPushButton(self.splitter_4)
        self.calc.setObjectName(_fromUtf8("calc"))
        self.div = QtGui.QPushButton(self.splitter_4)
        self.div.setObjectName(_fromUtf8("div"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.bclear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.num.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.bclear.setText(_translate("Dialog", "clear", None))
        self.b1.setText(_translate("Dialog", "1", None))
        self.b2.setText(_translate("Dialog", "2", None))
        self.b3.setText(_translate("Dialog", "3", None))
        self.add.setText(_translate("Dialog", "+", None))
        self.b4.setText(_translate("Dialog", "4", None))
        self.b5.setText(_translate("Dialog", "5", None))
        self.b6.setText(_translate("Dialog", "6", None))
        self.sub.setText(_translate("Dialog", "-", None))
        self.b7.setText(_translate("Dialog", "7", None))
        self.b8.setText(_translate("Dialog", "8", None))
        self.b9.setText(_translate("Dialog", "9", None))
        self.mul.setText(_translate("Dialog", "x", None))
        self.bspace.setText(_translate("Dialog", "<--", None))
        self.dotbtn.setText(_translate("Dialog", ".", None))
        self.b0.setText(_translate("Dialog", "0", None))
        self.calc.setText(_translate("Dialog", "=", None))
        self.div.setText(_translate("Dialog", "/", None))

