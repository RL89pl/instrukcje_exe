# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instrukcje.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_uploader(object):
    def setupUi(self, uploader):
        uploader.setObjectName("uploader")
        uploader.resize(324, 182)
        uploader.setSizeGripEnabled(False)
        uploader.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(uploader)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(uploader)
        self.textBrowser.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.accept = QtWidgets.QPushButton(uploader)
        self.accept.setObjectName("accept")
        self.verticalLayout.addWidget(self.accept)

        self.retranslateUi(uploader)
        QtCore.QMetaObject.connectSlotsByName(uploader)

    def retranslateUi(self, uploader):
        _translate = QtCore.QCoreApplication.translate
        uploader.setWindowTitle(_translate("uploader", "Instrukcje"))
        self.accept.setText(_translate("uploader", "Wgraj"))

