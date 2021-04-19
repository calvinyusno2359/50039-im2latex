# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1120, 950)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.appTitleLabel = QtWidgets.QLabel(Form)
        self.appTitleLabel.setGeometry(QtCore.QRect(4, 10, 1111, 101))
        font = QtGui.QFont()
        font.setPointSize(31)
        self.appTitleLabel.setFont(font)
        self.appTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.appTitleLabel.setObjectName("appTitleLabel")
        self.loadImageButton = QtWidgets.QPushButton(Form)
        self.loadImageButton.setGeometry(QtCore.QRect(10, 130, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loadImageButton.setFont(font)
        self.loadImageButton.setObjectName("loadImageButton")
        self.filePathEdit = QtWidgets.QLineEdit(Form)
        self.filePathEdit.setGeometry(QtCore.QRect(200, 130, 721, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filePathEdit.setFont(font)
        self.filePathEdit.setObjectName("filePathEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 600, 1101, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.inputImageLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.inputImageLayout.setContentsMargins(0, 0, 0, 0)
        self.inputImageLayout.setObjectName("inputImageLayout")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 190, 1101, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.canvasLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.canvasLayout_2.setContentsMargins(0, 0, 0, 0)
        self.canvasLayout_2.setObjectName("canvasLayout_2")
        self.filePathEdit_2 = QtWidgets.QLineEdit(Form)
        self.filePathEdit_2.setGeometry(QtCore.QRect(10, 540, 1101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filePathEdit_2.setFont(font)
        self.filePathEdit_2.setObjectName("filePathEdit_2")
        self.translateButton = QtWidgets.QPushButton(Form)
        self.translateButton.setGeometry(QtCore.QRect(930, 130, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.translateButton.setFont(font)
        self.translateButton.setObjectName("translateButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.appTitleLabel.setText(_translate("Form", "Image to Latex App"))
        self.loadImageButton.setText(_translate("Form", "Browse Image"))
        self.translateButton.setText(_translate("Form", "Translate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())