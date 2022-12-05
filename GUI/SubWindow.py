from PyQt5.QtWidgets import *
from PyQt5.Qt import *

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ON국민예약.onKookminBookGUI import *

class SubWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('학교시설 예약 시스템')
        self.setFixedSize(QSize(850, 600))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        btn1 = QPushButton('도서관', self)
        btn2 = QPushButton('카페', self)
        btn3 = QPushButton('운동장', self)
        btn4 = QPushButton('체육관', self)
        btn5 = QPushButton('빈 강의실', self)
        btn6 = QPushButton('기타시설 예약', self)
        btn7 = QPushButton('예약(ON국민)', self)

        btn1.clicked.connect(self.clicked_btn1)
        btn1.setGeometry(400, 80, 200, 100)
        btn2.clicked.connect(self.clicked_btn2)
        btn2.setGeometry(600, 80, 200, 100)
        btn3.clicked.connect(self.clicked_btn3)
        btn3.setGeometry(400, 200, 200, 100)
        btn4.clicked.connect(self.clicked_btn4)
        btn4.setGeometry(600, 200, 200, 100)
        btn5.clicked.connect(self.clicked_btn5)
        btn5.setGeometry(400, 320, 200, 100)
        btn6.clicked.connect(self.clicked_btn6)
        btn6.setGeometry(600, 320, 200, 100)
        btn7.clicked.connect(self.clicked_btn7)
        btn7.setGeometry(400, 440, 400, 100)

        label = QLabel('학교시설 예약 시스템', self)
        label.move(130, 260)

        layout.addWidget(label)

        self.show()

    def onActivated(self, text):
        self.label.setText(text)

    def clicked_btn1(self):
        self.dialog = QDialog()
        self.dialog.setWindowTitle("도서관 예약")
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(800, 500)
        self.dialog.show()

    def clicked_btn2(self):
        self.dialog = QDialog()
        self.dialog.setWindowTitle("카페 예약")
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(800, 500)
        self.dialog.show()

    def clicked_btn3(self):
        self.ub = UnivBook()
        self.ub.show()

    def clicked_btn4(self):
        self.dialog = QDialog()
        self.dialog.setWindowTitle("체육관 예약")
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(800, 500)
        self.dialog.show()

    def clicked_btn5(self):
        self.dialog = QDialog()
        self.dialog.setWindowTitle("빈 강의실 예약")
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(800, 500)
        self.dialog.show()

    def clicked_btn6(self):
        self.dialog = QDialog()
        self.dialog.setWindowTitle("예약")
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(800, 500)
        self.dialog.show()

    def clicked_btn7(self):
        self.ub = UnivBook()
        self.ub.show()


    def showModal(self):
        return super().exec_()
