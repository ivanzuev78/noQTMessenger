# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designTrue.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.SenMessageButton = QtWidgets.QPushButton(self.centralwidget)
        self.SenMessageButton.setAutoDefault(False)
        self.SenMessageButton.setDefault(False)
        self.SenMessageButton.setObjectName("SenMessageButton")
        self.gridLayout.addWidget(self.SenMessageButton, 13, 0, 1, 2)
        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_3.setContentsMargins(1, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.gridWidget)
        self.label_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridWidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit_2.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_2.setSizePolicy(sizePolicy)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout_3.addWidget(self.dateTimeEdit_2, 2, 2, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        self.dateTimeEdit.setInputMethodHints(QtCore.Qt.ImhDate|QtCore.Qt.ImhTime)
        self.dateTimeEdit.setFrame(True)
        self.dateTimeEdit.setReadOnly(False)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_3.addWidget(self.dateTimeEdit, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 3, 0, 1, 3)
        self.gridLayout.addWidget(self.gridWidget, 3, 1, 1, 1)
        self.ChoseReceiver = QtWidgets.QLineEdit(self.centralwidget)
        self.ChoseReceiver.setText("")
        self.ChoseReceiver.setObjectName("ChoseReceiver")
        self.gridLayout.addWidget(self.ChoseReceiver, 1, 1, 1, 1)
        self.YourMessage = QtWidgets.QLineEdit(self.centralwidget)
        self.YourMessage.setEnabled(False)
        self.YourMessage.setText("")
        self.YourMessage.setObjectName("YourMessage")
        self.gridLayout.addWidget(self.YourMessage, 12, 0, 1, 2)
        self.AcceptReceiverButton = QtWidgets.QPushButton(self.centralwidget)
        self.AcceptReceiverButton.setObjectName("AcceptReceiverButton")
        self.gridLayout.addWidget(self.AcceptReceiverButton, 2, 1, 1, 1)
        self.ListReceivers = QtWidgets.QListWidget(self.centralwidget)
        self.ListReceivers.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListReceivers.sizePolicy().hasHeightForWidth())
        self.ListReceivers.setSizePolicy(sizePolicy)
        self.ListReceivers.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ListReceivers.setObjectName("ListReceivers")
        self.gridLayout.addWidget(self.ListReceivers, 6, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.Dialogue = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Dialogue.setEnabled(False)
        self.Dialogue.setReadOnly(True)
        self.Dialogue.setPlainText("")
        self.Dialogue.setObjectName("Dialogue")
        self.gridLayout.addWidget(self.Dialogue, 0, 0, 12, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def receiver_selected(self, item):
        self.ChoseReceiver.setText(item.text())

    def receiver_accepted(self):
        pass

    def send_message(self):
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SenMessageButton.setText(_translate("MainWindow", "Send Message"))
        self.label_3.setText(_translate("MainWindow", "For"))
        self.label.setText(_translate("MainWindow", "Show History:"))
        self.label_2.setText(_translate("MainWindow", "Since"))
        self.pushButton.setText(_translate("MainWindow", "Show"))
        self.AcceptReceiverButton.setText(_translate("MainWindow", "Open the dialogue"))
        self.label_4.setText(_translate("MainWindow", "Chose the interlocatur:"))
