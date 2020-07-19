import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication, QMainWindow,
                             QAction, qApp,
                             QHBoxLayout, QVBoxLayout, QMessageBox,
                             QLineEdit, QTableWidget, QTableWidgetItem,
                             QGridLayout, QPlainTextEdit,
                             QDesktopWidget, QLabel, QRadioButton,
                             QGroupBox, QSizePolicy, QCheckBox, QFileDialog,
                             QTextEdit, QTextBrowser)
from PyQt5.QtGui import QFont, QColor

class Files_Number_Handler():
    #gets a folder path as an argument and searches for files that end with
    #.fasta or .tsv and saves them in the corresponding Array
    def Identify_Files_Numbers(folder_path):
        fasta_files=[]
        tsv_files = []
        mzML_files = []
        idXML_files= []
        ini_files = []
        mzMLLoaded = 0
        idXMLLoaded = 0
        fileslist = sorted(os.listdir(folder_path))
        #print(sorted(fileslist))
        for file in fileslist:
            if file.endswith(".fasta"):
                fasta_files.append(file)

            if file.endswith(".tsv"):
                tsv_files.append(file)

            if file.endswith(".mzML"):
                mzML_files.append(file)

            if file.endswith(".idXML"):
                idXML_files.append(file)

            if file.endswith(".ini"):
                ini_files.append(file)

        if len(mzML_files) == 0 and len(idXML_files) == 0:
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("No mzML and idXML files found. Pleas select another folder.")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()
            mzMLLoaded = 0
            idXMLLoaded =0

        if  len(mzML_files) == 0 and len(idXML_files) != 0:
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("No mzML files found. Pleas select another folder.")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()
            mzMLLoaded = 0
            idXMLLoaded = 1

        if len(mzML_files) != 0 and len(idXML_files) == 0:
            User_Warning = QMessageBox()
            User_Warning.setIcon(QMessageBox.Information)
            User_Warning.setText("No idXML files found. Pleas select another folder.")
            User_Warning.setWindowTitle("Information")
            Information = User_Warning.exec_()
            mzMLLoaded = 1
            idXMLLoaded = 0
        if len(mzML_files) != 0 and len(idXML_files) != 0:
            mzMLLoaded = 1
            idXMLLoaded = 1



        return fasta_files,tsv_files,mzML_files,idXML_files,ini_files, mzMLLoaded, idXMLLoaded

    #checks if array contains only on element, it is important because if
    #more than 1 user needs to select the on file he wants to use
    def Check_If_More_Than_One(arraytotest):
        if len(arraytotest)>1:
            return True
        else :
            return False

    def Check_If_Less_Than_One(arraytotest):
        if len(arraytotest)==0:
            return True
        else :
            return False
    def Check_If_One(arraytotest) :
        if len(arraytotest) == 1:
            return True
        else:
            return False           
