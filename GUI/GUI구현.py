import sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from SubWindow import SubWindow
from 가마SubWindow import 가마SubWindow
from 누들송SubWindow import 누들송SubWindow
from 인터쉐프SubWindow import 인터쉐프SubWindow
from 데일리밥SubWindow import 데일리밥SubWindow

# 메인 윈도우 창.
class MainWindow(QMainWindow):

    dialog = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main')
        self.setGeometry(100, 100, 850, 600)
        self.initUI()

    def initUI(self):
        Reservation_btn = QPushButton('학교 시설 예약하기', self)
        btn1 = QPushButton('가마', self)
        btn2 = QPushButton('누들송(면)', self)
        btn3 = QPushButton('인터쉐프', self)
        btn4 = QPushButton('데일리밥', self)

        Reservation_btn.clicked.connect(self.clicked_Button)
        Reservation_btn.setGeometry(400, 80, 400, 50)
        btn1.clicked.connect(self.clicked_btn1)
        btn1.setGeometry(400, 200, 200, 100)
        btn2.clicked.connect(self.clicked_btn2)
        btn2.setGeometry(600, 200, 200, 100)
        btn3.clicked.connect(self.clicked_btn3)
        btn3.setGeometry(400, 380, 200, 100)
        btn4.clicked.connect(self.clicked_btn4)
        btn4.setGeometry(600, 380, 200, 100)

        label1 = QLabel('Bookmin', self)
        label1.move(20, 5)
        font1 = label1.font()
        font1.setPointSize(35)
        label1.setFont(font1)
        font1.setBold(True)

        label2 = QLabel('오늘의 메뉴', self)
        label2.move(20, 120)
        font2 = label2.font()
        font2.setPointSize(15)
        label2.setFont(font2)

        #
        label2_2 = QLabel('오늘의 메뉴 정보출력 창', self)
        label2_2.move(20, 180)
        font2_2 = label2_2.font()
        label2_2.setFont(font2_2)
        #

        label3 = QLabel('식당별 혼잡도', self)
        label3.move(20, 280)
        font3 = label3.font()
        font3.setPointSize(15)
        label3.setFont(font3)

        #혼잡도 출력==================================================================================================
        label3_2 = QTextEdit()
        label3_2.setText("test")
        label3_2.move(20, 320)
        font3_2 = label3_2.font()
        label3_2.setFont(font3_2)
        #

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label2_2)
        vbox.addWidget(label3)
        vbox.addWidget(label3_2)

        self.setLayout(vbox)

        label1.setFixedSize(400, 150)
        label2.setFixedSize(400, 80)
        label2_2.setFixedSize(400, 100)
        label3.setFixedSize(400, 80)
        label3_2.setFixedSize(400, 100)

        self.show()

    # 학교 시설 예약하기 버튼을 누르면 실행되는 새로운 예약 창
    def clicked_Button(self):
        subwin = SubWindow()
        r = subwin.showModal()

        if r:
            text = subwin.edit.text()
            self.label.setText(text)

    # 가마 예약 버튼을 누르면 실행되는 새로운 창
    def clicked_btn1(self):
        가마subwin = 가마SubWindow()
        r = 가마subwin.showModal()

        if r:
            text = 가마subwin.edit.text()
            self.label.setText(text)

    # 누들송 예약 버튼을 누르면 실행되는 새로운 창
    def clicked_btn2(self):
        누들송subwin = 누들송SubWindow()
        r = 누들송subwin.showModal()

        if r:
            text = 누들송subwin.edit.text()
            self.label.setText(text)

    # 인터쉐프 예약 버튼을 누르면 실행되는 새로운 창
    def clicked_btn3(self):
        인터쉐프subwin = 인터쉐프SubWindow()
        r = 인터쉐프subwin.showModal()

        if r:
            text = 인터쉐프subwin.edit.text()
            self.label.setText(text)

    # 데일리밥 예약 버튼을 누르면 실행되는 새로운 창
    def clicked_btn4(self):
        데일리밥subwin = 데일리밥SubWindow()
        r = 데일리밥subwin.showModal()

        if r:
            text = 데일리밥subwin.edit.text()
            self.label.setText(text)

    def show(self):
        super().show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    sys.exit(app.exec_())
