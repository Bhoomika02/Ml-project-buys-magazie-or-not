# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'heartdisease.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#This is the project that I have used to implement heart disease prediction using logistic regression.
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(675, 629)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("background-color:rgb(255, 160, 7)")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 70, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 120, 51, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 280, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(80, 330, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 380, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 450, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(380, 70, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(330, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(380, 210, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(270, 580, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color:white")
        self.label_12.setObjectName("label_12")
        self.fixed_acidity = QtWidgets.QLineEdit(Form)
        self.fixed_acidity.setGeometry(QtCore.QRect(90, 80, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.fixed_acidity.setFont(font)
        self.fixed_acidity.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.fixed_acidity.setObjectName("fixed_acidity")
        self.age = QtWidgets.QLineEdit(Form)
        self.age.setGeometry(QtCore.QRect(170, 130, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.age.setFont(font)
        self.age.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.age.setObjectName("age")
        self.education = QtWidgets.QLineEdit(Form)
        self.education.setGeometry(QtCore.QRect(130, 180, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.education.setFont(font)
        self.education.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.education.setObjectName("education")
        self.currentSmoker = QtWidgets.QLineEdit(Form)
        self.currentSmoker.setGeometry(QtCore.QRect(190, 230, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.currentSmoker.setFont(font)
        self.currentSmoker.setStyleSheet("background-color:rgb(255, 255, 255)\n"
"")
        self.currentSmoker.setObjectName("currentSmoker")
        self.cigsPerDay = QtWidgets.QLineEdit(Form)
        self.cigsPerDay.setGeometry(QtCore.QRect(160, 290, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.cigsPerDay.setFont(font)
        self.cigsPerDay.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.cigsPerDay.setObjectName("cigsPerDay")
        self.BPMeds = QtWidgets.QLineEdit(Form)
        self.BPMeds.setGeometry(QtCore.QRect(180, 340, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.BPMeds.setFont(font)
        self.BPMeds.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.BPMeds.setObjectName("BPMeds")
        self.prevalentStroke = QtWidgets.QLineEdit(Form)
        self.prevalentStroke.setGeometry(QtCore.QRect(190, 390, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.prevalentStroke.setFont(font)
        self.prevalentStroke.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.prevalentStroke.setObjectName("prevalentStroke")
        self.prevalentHyp = QtWidgets.QLineEdit(Form)
        self.prevalentHyp.setGeometry(QtCore.QRect(190, 460, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.prevalentHyp.setFont(font)
        self.prevalentHyp.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.prevalentHyp.setObjectName("prevalentHyp")
        self.diabetes = QtWidgets.QLineEdit(Form)
        self.diabetes.setGeometry(QtCore.QRect(500, 80, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.diabetes.setFont(font)
        self.diabetes.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.diabetes.setObjectName("diabetes")
        self.totChol = QtWidgets.QLineEdit(Form)
        self.totChol.setGeometry(QtCore.QRect(430, 150, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.totChol.setFont(font)
        self.totChol.setStyleSheet("background-color:rgb(255, 255, 255)\n"
"")
        self.totChol.setObjectName("totChol")
        self.sysBP = QtWidgets.QLineEdit(Form)
        self.sysBP.setGeometry(QtCore.QRect(470, 210, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.sysBP.setFont(font)
        self.sysBP.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.sysBP.setObjectName("sysBP")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(110, 20, 491, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color:rgb(191, 255, 117)")
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 530, 171, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(191, 255, 117)")
        self.pushButton.setObjectName("pushButton")
        self.diaBP = QtWidgets.QLineEdit(Form)
        self.diaBP.setGeometry(QtCore.QRect(450, 280, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.diaBP.setFont(font)
        self.diaBP.setStyleSheet("background-color:rgb(255, 255, 255)\n"
"")
        self.diaBP.setObjectName("diaBP")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(350, 270, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.BMI = QtWidgets.QLineEdit(Form)
        self.BMI.setGeometry(QtCore.QRect(500, 350, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.BMI.setFont(font)
        self.BMI.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.BMI.setObjectName("BMI")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(410, 330, 51, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.heartRate = QtWidgets.QLineEdit(Form)
        self.heartRate.setGeometry(QtCore.QRect(460, 400, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.heartRate.setFont(font)
        self.heartRate.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.heartRate.setObjectName("heartRate")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(350, 390, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.glucose = QtWidgets.QLineEdit(Form)
        self.glucose.setGeometry(QtCore.QRect(510, 470, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.glucose.setFont(font)
        self.glucose.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.glucose.setObjectName("glucose")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(400, 460, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(110, 100, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("font:8pt")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(210, 250, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("font:8pt")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(200, 360, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("font:8pt")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(210, 410, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("font:8pt")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(210, 480, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("font:8pt")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(520, 100, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("font:8pt")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(290, 610, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("font:8pt")
        self.label_24.setObjectName("label_24")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "male"))
        self.label_2.setText(_translate("Form", "age"))
        self.label_3.setText(_translate("Form", "education"))
        self.label_4.setText(_translate("Form", "currentSmoker"))
        self.label_5.setText(_translate("Form", "cigsPerDay"))
        self.label_6.setText(_translate("Form", "BPMeds"))
        self.label_7.setText(_translate("Form", "prevalentStroke"))
        self.label_8.setText(_translate("Form", " prevalentHyp"))
        self.label_9.setText(_translate("Form", "diabetes"))
        self.label_10.setText(_translate("Form", "totChol"))
        self.label_11.setText(_translate("Form", "sysBP"))
        self.label_12.setText(_translate("Form", "TenYearCHD"))
        self.label_13.setText(_translate("Form", "Predict Person Gets Heart disease or not"))
        self.pushButton.setText(_translate("Form", "Predict CHD"))
        self.label_14.setText(_translate("Form", "diaBP"))
        self.label_15.setText(_translate("Form", "BMI"))
        self.label_16.setText(_translate("Form", "heartRate"))
        self.label_17.setText(_translate("Form", " glucose"))
        self.label_18.setText(_translate("Form", "0- No,1-Yes"))
        self.label_19.setText(_translate("Form", "0- No,1-Yes"))
        self.label_20.setText(_translate("Form", "0- No,1-Yes"))
        self.label_21.setText(_translate("Form", "0- No,1-Yes"))
        self.label_22.setText(_translate("Form", "0- No,1-Yes"))
        self.label_23.setText(_translate("Form", "0- No,1-Yes"))
        self.label_24.setText(_translate("Form", "0- No,1-Yes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
