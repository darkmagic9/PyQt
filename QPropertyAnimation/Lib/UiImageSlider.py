# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiImageSlider.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(656, 612)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = SlidingStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.verticalLayout.addWidget(self.stackedWidget)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBoxSpeed = QtWidgets.QSpinBox(self.groupBox)
        self.spinBoxSpeed.setMinimum(100)
        self.spinBoxSpeed.setMaximum(5000)
        self.spinBoxSpeed.setProperty("value", 500)
        self.spinBoxSpeed.setObjectName("spinBoxSpeed")
        self.horizontalLayout.addWidget(self.spinBoxSpeed)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButtonHor = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonHor.setChecked(True)
        self.radioButtonHor.setObjectName("radioButtonHor")
        self.horizontalLayout_2.addWidget(self.radioButtonHor)
        self.radioButtonVer = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonVer.setObjectName("radioButtonVer")
        self.horizontalLayout_2.addWidget(self.radioButtonVer)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBoxEasing = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBoxEasing.setObjectName("comboBoxEasing")
        self.horizontalLayout_3.addWidget(self.comboBoxEasing)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonPrev = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.horizontalLayout_4.addWidget(self.pushButtonPrev)
        self.pushButtonNext = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout_4.addWidget(self.pushButtonNext)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButtonStart = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.horizontalLayout_5.addWidget(self.pushButtonStart)
        self.pushButtonStop = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.horizontalLayout_5.addWidget(self.pushButtonStop)
        self.verticalLayout.addWidget(self.groupBox_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Picture carousel animation"))
        self.groupBox.setTitle(_translate("Form", "Animation speed"))
        self.groupBox_2.setTitle(_translate("Form", "Animation direction (default is landscape)"))
        self.radioButtonHor.setText(_translate("Form", "Landscape"))
        self.radioButtonVer.setText(_translate("Form", "Portrait"))
        self.groupBox_3.setTitle(_translate("Form", "Animation curve type"))
        self.groupBox_4.setTitle(_translate("Form", "Page turning"))
        self.pushButtonPrev.setText(_translate("Form", "Previous page"))
        self.pushButtonNext.setText(_translate("Form", "Next page"))
        self.groupBox_5.setTitle(_translate("Form", "Carousel"))
        self.pushButtonStart.setText(_translate("Form", "Carousel begins"))
        self.pushButtonStop.setText(_translate("Form", "Carousel stop"))

from Lib.SlidingStackedWidget import SlidingStackedWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

