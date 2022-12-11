from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(968, 812)
        Form.setStyleSheet("background-color: rgb(207, 255, 223);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 10, 671, 71))
        self.label.setStyleSheet("color:rgb(85, 0, 0);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 110, 55, 16))
        self.label_2.setStyleSheet("font: 87 12pt \"Segoe UI Black\";color:rgb(124, 0, 0)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 160, 55, 16))
        self.label_3.setStyleSheet("font: 87 12pt \"Segoe UI Black\";color:rgb(124, 0, 0)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 220, 160, 16))
        self.label_4.setStyleSheet("font: 87 12pt \"Segoe UI Black\";color:rgb(124, 0, 0)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(110, 280, 160, 16))
        self.label_5.setStyleSheet("font: 87 12pt \"Segoe UI Black\";color:rgb(124, 0, 0)")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(110, 340, 160, 16))
        self.label_6.setStyleSheet("font: 87 12pt \"Segoe UI Black\";color:rgb(124, 0, 0)")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(110, 400, 160, 16))
        self.label_7.setStyleSheet("font: 87 12pt \"Segoe UI Black\";color:rgb(124, 0, 0)")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(110, 470, 160, 16))
        self.label_8.setStyleSheet("font: 87 12pt \"Segoe UI Black\";color:rgb(124, 0, 0)")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(110, 540, 160, 16))
        self.label_9.setStyleSheet("font: 87 12pt \"Segoe UI Black\";color:rgb(124, 0, 0)")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(560, 100, 170, 17))
        self.label_10.setStyleSheet("font: 87 12pt \"Segoe UI Black\";color:rgb(124, 0, 0)")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(560, 150, 160, 16))
        self.label_11.setStyleSheet("font: 87 12pt \"Segoe UI Black\";color:rgb(124, 0, 0)")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(560, 210, 160, 16))
        self.label_12.setStyleSheet("font: 87 12pt \"Segoe UI Black\";color:rgb(124, 0, 0)")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(560, 270, 160, 16))
        self.label_13.setStyleSheet("font: 87 12pt \"Segoe UI Black\";color:rgb(124, 0, 0)")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(560, 340, 160, 16))
        self.label_14.setStyleSheet("font: 87 12pt \"Segoe UI Black\";color:rgb(124, 0, 0)")
        self.label_14.setObjectName("label_14")






        self.age = QtWidgets.QLineEdit(Form)
        self.age.setGeometry(QtCore.QRect(280, 110, 113, 22))
        self.age.setObjectName("age")
        self.sex = QtWidgets.QLineEdit(Form)
        self.sex.setGeometry(QtCore.QRect(280, 160, 113, 22))
        self.sex.setObjectName("sex")
        self.cp = QtWidgets.QLineEdit(Form)
        self.cp.setGeometry(QtCore.QRect(280, 220, 113, 22))
        self.cp.setObjectName("cp")
        self.trest = QtWidgets.QLineEdit(Form)
        self.trest.setGeometry(QtCore.QRect(280, 280, 113, 22))
        self.trest.setObjectName("trest")
        self.chol = QtWidgets.QLineEdit(Form)
        self.chol.setGeometry(QtCore.QRect(280, 340, 113, 22))
        self.chol.setObjectName("chol")
        self.fast = QtWidgets.QLineEdit(Form)
        self.fast.setGeometry(QtCore.QRect(280, 400, 113, 22))
        self.fast.setObjectName("fast")
        self.rest = QtWidgets.QLineEdit(Form)
        self.rest.setGeometry(QtCore.QRect(280, 470, 113, 22))
        self.rest.setObjectName("rest")
        self.thalach = QtWidgets.QLineEdit(Form)
        self.thalach.setGeometry(QtCore.QRect(280, 530, 113, 22))
        self.thalach.setObjectName("thalach")
        self.exang = QtWidgets.QLineEdit(Form)
        self.exang.setGeometry(QtCore.QRect(730, 100, 113, 22))
        self.exang.setObjectName("exang")
        self.oldpeak = QtWidgets.QLineEdit(Form)
        self.oldpeak.setGeometry(QtCore.QRect(730, 150, 113, 22))
        self.oldpeak.setObjectName("oldpeak")
        self.slope = QtWidgets.QLineEdit(Form)
        self.slope.setGeometry(QtCore.QRect(730, 210, 113, 22))
        self.slope.setObjectName("slope")
        self.ca = QtWidgets.QLineEdit(Form)
        self.ca.setGeometry(QtCore.QRect(730, 270, 113, 22))
        self.ca.setObjectName("ca")
        self.thal = QtWidgets.QLineEdit(Form)
        self.thal.setGeometry(QtCore.QRect(730, 330, 113, 22))
        self.thal.setObjectName("thal")




        self.Btnpred = QtWidgets.QPushButton(Form)
        self.Btnpred.setGeometry(QtCore.QRect(470, 620, 161, 61))
        self.Btnpred.setStyleSheet("font: 87 20pt \"Segoe UI Black\";color:rgb(24, 50, 10)")
        self.Btnpred.setObjectName("Btnpred")
        self.result = QtWidgets.QLabel(Form)
        self.result.setGeometry(QtCore.QRect(260, 730, 661, 41))
        self.result.setStyleSheet("font: 87 24pt \"Segoe UI Black\";color:rgb(124, 0, 0)")
        
        self.result.setObjectName("result")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "HEART FAILURE PREDITION"))
        self.label_2.setText(_translate("Form", "AGE:"))
        self.label_3.setText(_translate("Form", "SEX :"))
        self.label_4.setText(_translate("Form", "CHEST_PAIN_TYPE:"))
        self.label_5.setText(_translate("Form", "RESTING_BP:"))
        self.label_6.setText(_translate("Form", "CHOLESTEROL:"))
        self.label_7.setText(_translate("Form", "FASTING_BS:"))
        self.label_8.setText(_translate("Form", "RESTING_ECG:"))
        self.label_9.setText(_translate("Form", "MAX_HR:"))
        self.label_10.setText(_translate("Form", "EXERSISE_ANGINA:"))
        self.label_11.setText(_translate("Form", "OLD PEAK:"))
        self.label_12.setText(_translate("Form", "ST_SLOPE:"))
        self.label_13.setText(_translate("Form", "CAA:"))
        self.label_14.setText(_translate("Form", "THAL_RATE:"))
        self.Btnpred.setText(_translate("Form", "Predict"))
        
        self.result.setText(_translate("Form", "Result"))
     
    

       
       



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
