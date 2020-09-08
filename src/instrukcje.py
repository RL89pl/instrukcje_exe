from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtWidgets import *
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject
from win32com import client
import sys
import os
import re
import instrukcje_ui
class Instrukcje(QDialog, instrukcje_ui.Ui_uploader):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.accept.clicked.connect(self.upload)
        self.textBrowser.setText("Kliknij przycisk, by zacząć")
    def showInfo(self, text):
        self.textBrowser.setText(text)
    def clean(self, nazwa):
        self.textBrowser.setText("Sprzątam po sobie...")
        app.processEvents()
        os.remove(nazwa)
        os.rename('INSTRUKCJA.pdf', nazwa)
        self.textBrowser.setText("Operacja zakończona poprawnie")
        app.processEvents()

    def upload(self):
        self.textBrowser.setText("Rozpoczynam pracę")
        app.processEvents()
        cursor = self.textBrowser.textCursor()
        cursor.insertHtml('''<p><span style="color: red;">.</span>''')

        self.textBrowser.toPlainText
        directory = os.getcwd()
        word = client.DispatchEx('Word.Application')
        self.textBrowser.setText("Przerabiam plik Worda...")
        app.processEvents()
        for file in os.listdir(directory):
            if (file.endswith('.doc') or file.endswith('.docx')):
                ending = ""
                if file.endswith('.doc'):
                    ending = '.doc'
                if file.endswith('.docx'):
                    ending = '.docx'
                new_name = file.replace(ending,r".pdf")
                in_file = os.path.abspath(directory + '\\' + file)
                new_file = os.path.abspath(directory + '\\' + new_name)
                doc = word.Documents.Open(in_file)
                doc.SaveAs(new_file,FileFormat = 17)
                doc.Close()
        word.Quit()
        writer = PdfFileWriter()


        input1 = PdfFileReader(open("start.pdf", 'rb'))
        page1 = input1.getPage(0)


        inputFile = open(new_name, 'rb')
        input2 = PdfFileReader(inputFile)
        pagecount = input2.getNumPages()
        writer.addPage(page1)
        for i in range(0,pagecount):
            page2 = input2.getPage(i)
            writer.addPage(page2)
        self.textBrowser.setText("Zapisuję plik INSTRUKCJA.pdf")
        app.processEvents()



        strona = open("INSTRUKCJA.pdf", 'wb')
        self.textBrowser.setText("Sprzątam po sobie...")
        writer.write(strona)
        strona.close()
        inputFile.close()
        self.textBrowser.setText("Plik > INSTRUKCJA.pdf < gotowy")
        app.processEvents()
        self.clean(new_name)






app = QApplication(sys.argv)
edycja = Instrukcje()
edycja.show()
app.exec_()