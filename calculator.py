from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QValidator, QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression


class Ui_Form(object):
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.setFixedSize(425, 425)

        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 381, 81))

        validator = QRegularExpressionValidator(QRegularExpression("^[0-9+\\-*/().]*$"), self.lineEdit)
        self.lineEdit.setValidator(validator)

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(0, 132, 423, 291))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")


        #BUTONLAR
        self.pushButton_0 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 4, 0, 1, 1)

        self.pushButton_1 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 3, 0, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_7 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_8 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_9 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.pushButton_10 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 4, 3, 1, 1)

        self.pushButton_11 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 3, 3, 1, 1)

        self.pushButton_12 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 2, 3, 1, 1)

        self.pushButton_13 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 1, 3, 1, 1)

        self.pushButton_14 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 4, 2, 1, 1)

        self.pushButton_15 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 4, 1, 1, 1)

        self.pushButton_16 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 0, 0, 1, 1)

        self.pushButton_17 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 0, 1, 1, 1)

        self.pushButton_18 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 0, 2, 1, 1)

        self.pushButton_19 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 0, 3, 1, 1)
        
        self.pushButton_0.clicked.connect(self.PushButton0)
        self.pushButton_1.clicked.connect(self.PushButton1)
        self.pushButton_2.clicked.connect(self.PushButton2)
        self.pushButton_3.clicked.connect(self.PushButton3)
        self.pushButton_4.clicked.connect(self.PushButton4)
        self.pushButton_5.clicked.connect(self.PushButton5)
        self.pushButton_6.clicked.connect(self.PushButton6)
        self.pushButton_7.clicked.connect(self.PushButton7)
        self.pushButton_8.clicked.connect(self.PushButton8)
        self.pushButton_9.clicked.connect(self.PushButton9)
        self.pushButton_10.clicked.connect(self.ButtonPlus)
        self.pushButton_11.clicked.connect(self.ButtonMinus)
        self.pushButton_12.clicked.connect(self.ButtonMultiply)
        self.pushButton_13.clicked.connect(self.ButtonDivide)
        self.pushButton_14.clicked.connect(self.ButtonEqual)
        self.pushButton_15.clicked.connect(self.ButtonDot)
        self.pushButton_16.clicked.connect(self.ButtonLeftParenthesis)
        self.pushButton_17.clicked.connect(self.ButtonRightParenthesis)
        self.pushButton_18.clicked.connect(self.ButtonAC)
        self.pushButton_19.clicked.connect(self.ButtonC)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Hesap Makinesi", "Hesap Makinesi"))
        self.pushButton_0.setText(_translate("Form", "0"))
        self.pushButton_1.setText(_translate("Form", "1"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_9.setText(_translate("Form", "9"))
        self.pushButton_10.setText(_translate("Form", "+"))
        self.pushButton_11.setText(_translate("Form", "-"))
        self.pushButton_12.setText(_translate("Form", "*"))
        self.pushButton_13.setText(_translate("Form", "/"))
        self.pushButton_14.setText(_translate("Form", "="))
        self.pushButton_15.setText(_translate("Form", "."))
        self.pushButton_16.setText(_translate("Form", "("))
        self.pushButton_17.setText(_translate("Form", ")"))
        self.pushButton_18.setText(_translate("Form", "AC"))
        self.pushButton_19.setText(_translate("Form", "C"))

    def PushButton0(self):
        yazi = self.lineEdit.text() + "0"
        self.lineEdit.setText(yazi)

    def PushButton1(self):
        yazi = self.lineEdit.text() + "1"
        self.lineEdit.setText(yazi)

    def PushButton2(self):
        yazi = self.lineEdit.text() + "2"
        self.lineEdit.setText(yazi)

    def PushButton3(self):
        yazi = self.lineEdit.text() + "3"
        self.lineEdit.setText(yazi)

    def PushButton4(self):
        yazi = self.lineEdit.text() + "4"
        self.lineEdit.setText(yazi)

    def PushButton5(self):
        yazi = self.lineEdit.text() + "5"
        self.lineEdit.setText(yazi)

    def PushButton6(self):
        yazi = self.lineEdit.text() + "6"
        self.lineEdit.setText(yazi)

    def PushButton7(self):
        yazi = self.lineEdit.text() + "7"
        self.lineEdit.setText(yazi)

    def PushButton8(self):
        yazi = self.lineEdit.text() + "8"
        self.lineEdit.setText(yazi)

    def PushButton9(self):
        yazi = self.lineEdit.text() + "9"
        self.lineEdit.setText(yazi)

    def ButtonPlus(self):
        yazi = self.lineEdit.text() + "+"
        self.lineEdit.setText(yazi)

    def ButtonMinus(self):
        yazi = self.lineEdit.text() + "-"
        self.lineEdit.setText(yazi)

    def ButtonMultiply(self):
        yazi = self.lineEdit.text() + "*"
        self.lineEdit.setText(yazi)

    def ButtonDivide(self):
        yazi = self.lineEdit.text() + "/"
        self.lineEdit.setText(yazi)

    def ButtonEqual(self):
        try:
            result = eval(self.lineEdit.text())
            self.lineEdit.setText(str(result))
        except:
            self.lineEdit.setText("HATALI")

    def ButtonDot(self):
        yazi = self.lineEdit.text() + "."
        self.lineEdit.setText(yazi)

    def ButtonLeftParenthesis(self):
        yazi = self.lineEdit.text() + "("
        self.lineEdit.setText(yazi)

    def ButtonRightParenthesis(self):
        yazi = self.lineEdit.text() + ")"
        self.lineEdit.setText(yazi)

    def ButtonAC(self):
        self.lineEdit.setText("")

    def ButtonC(self):
        yazi = self.lineEdit.text()[:-1]
        self.lineEdit.setText(yazi)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
