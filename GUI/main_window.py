from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from SubWindow import SubWindow
from 가마SubWindow import 가마SubWindow
from 누들송SubWindow import 누들송SubWindow
from 인터쉐프SubWindow import 인터쉐프SubWindow
from 데일리밥SubWindow import 데일리밥SubWindow
from multiprocessing import Process
from threading import Thread

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Person.bookminPerson import Person
from 번호표시스템.manager import *
from 번호표시스템.twilioTest import *
from 오늘의메뉴.crawlingclass import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.gama = Manager("가마")
        self.noodle = Manager("누들송(면)")
        self.inter = Manager("인터쉐프")
        self.daily = Manager("데일리밥")

        self.gama.setWaitingTime(2)
        self.noodle.setWaitingTime(2)
        self.inter.setWaitingTime(2)
        self.daily.setWaitingTime(2)

        # 창 사이즈 강제 조정
        MainWindow.setFixedSize(QSize(1000, 600))

        # 메인 위젯 설정
        self.centralwidget = QWidget(MainWindow)

        # 공통 사이즈 정책
        sizePolicy = QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        # widget ==============================================================================
        # widget 설정 (UI상 하단, 식당별 메뉴)
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(10, 380, 980, 210)

        # 수평 레이아웃 생성 (widget 내부)
        self.menuHorizontalLayout = QHBoxLayout(self.widget)
        self.menuHorizontalLayout.setContentsMargins(0, 0, 0, 0)

        # 메뉴 수직1 레이아웃 (가마 title + 가마 메뉴 출력)
        self.menuVerticalLayout = QVBoxLayout()
        self.gamaTitle = QLabel(self.widget)
        self.menuVerticalLayout.addWidget(self.gamaTitle)
        self.gamaTitle.setText("가마")

        self.gamaMenu = QTextEdit(self.widget)
        self.gamaMenu.setReadOnly(True)
        self.menuVerticalLayout.addWidget(self.gamaMenu)
        self.menuHorizontalLayout.addLayout(self.menuVerticalLayout)
        self.gamaMenu.setText(Crawling().todayMenu("가마중식"))

        # 메뉴 수직2 레이아웃 (누들송 title + 누들송 메뉴 출력)
        self.menuVerticalLayout_2 = QVBoxLayout()
        self.noodleTitle = QLabel(self.widget)
        self.menuVerticalLayout_2.addWidget(self.noodleTitle)
        self.noodleTitle.setText("누들송(면)")

        self.noodleMenu = QTextEdit(self.widget)
        self.noodleMenu.setReadOnly(True)
        self.menuVerticalLayout_2.addWidget(self.noodleMenu)
        self.menuHorizontalLayout.addLayout(self.menuVerticalLayout_2)
        self.noodleMenu.setText(Crawling().todayMenu("누들송(면)중식"))

        # 메뉴 수직3 레이아웃 (인터쉐프 title + 인터쉐프 메뉴 출력)
        self.menuVerticalLayout_3 = QVBoxLayout()
        self.interTitle = QLabel(self.widget)
        self.menuVerticalLayout_3.addWidget(self.interTitle)
        self.interTitle.setText("인터쉐프")

        self.interMenu = QTextEdit(self.widget)
        self.interMenu.setReadOnly(True)
        self.menuVerticalLayout_3.addWidget(self.interMenu)
        self.menuHorizontalLayout.addLayout(self.menuVerticalLayout_3)
        self.interMenu.setText(Crawling().todayMenu("인터쉐프중식"))

        # 메뉴 수직4 레이아웃 (데일리밥 title + 데일리밥 메뉴 출력)
        self.menuVerticalLayout_4 = QVBoxLayout()
        self.dailyTitle = QLabel(self.widget)
        self.menuVerticalLayout_4.addWidget(self.dailyTitle)
        self.dailyTitle.setText("데일리밥")

        self.dailyMenu = QTextEdit(self.widget)
        self.dailyMenu.setReadOnly(True)
        self.menuVerticalLayout_4.addWidget(self.dailyMenu)
        self.menuHorizontalLayout.addLayout(self.menuVerticalLayout_4)
        self.dailyMenu.setText(Crawling().todayMenu("데일리밥중식"))

        # widget1 =============================================================================
        # widget1 설정 (UI상 상단 왼쪽, 식당 내 혼잡도, 식당별 대기 인원)
        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setGeometry(10, 10, 380, 360)

        # 수직 레이아웃 설정 (Bookmin Vertical Layout)
        self.BookminVerticalLayout = QVBoxLayout(self.widget1)
        self.BookminVerticalLayout.setContentsMargins(0, 0, 0, 0)

        # 메인 타이틀 (Bookmin)
        self.title = QLabel(self.widget1)

        # 메인 타이틀 폰트, 사이즈 정책 설정
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        # 메인 타이틀 추가
        self.title.setFont(font)
        self.title.setLineWidth(1)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.BookminVerticalLayout.addWidget(self.title)
        self.title.setText("Bookmin")

        # 식당 내 혼잡도 타이틀 (Label)
        self.complexityTitle = QLabel(self.widget1)
        self.BookminVerticalLayout.addWidget(self.complexityTitle)
        self.complexityTitle.setText("식당 내 혼잡도")

        # 식당 내 혼잡도 출력 (TextEdit)
        self.p = Person()

        self.complexity = QTextEdit(self.widget1)
        self.complexity.setLineWidth(1)
        self.complexity.setReadOnly(True)
        self.BookminVerticalLayout.addWidget(self.complexity)

        self.complexity.setText(self.p.printPerson())

        self.complexity.repaint()

        # 식당별 대기 인원 타이틀 (Label)
        self.watingTitle = QLabel(self.widget1)
        self.BookminVerticalLayout.addWidget(self.watingTitle)
        self.watingTitle.setText("식당별 대기자 수 및 예상 대기시간")

        # 식당별 대기 인원 출력 (가마, 누들송, 인터쉐프, 데일리밥 순서)
        self.gamaWaiting = QLineEdit(self.widget1)
        self.gamaWaiting.setReadOnly(True)
        self.BookminVerticalLayout.addWidget(self.gamaWaiting)
        self.gamaWaiting.setText("가마: " + str(self.gama.getWaitingPeople())
                                 +"명 대기 | 예상 대기시간 " + str(self.gama.getTime()) + "분")
        self.gamaWaiting.repaint()

        self.noodleWaiting = QLineEdit(self.widget1)
        self.noodleWaiting.setReadOnly(True)
        self.BookminVerticalLayout.addWidget(self.noodleWaiting)
        self.noodleWaiting.setText("누들송(면): " + str(self.noodle.getWaitingPeople())
                                 + "명 대기 | 예상 대기시간 " + str(self.noodle.getTime()) + "분")
        self.noodleWaiting.repaint()

        self.interWaiting = QLineEdit(self.widget1)
        self.interWaiting.setReadOnly(True)
        self.BookminVerticalLayout.addWidget(self.interWaiting)
        self.interWaiting.setText("인터쉐프: " + str(self.inter.getWaitingPeople())
                                 + "명 대기 | 예상 대기시간 " + str(self.inter.getTime()) + "분")
        self.interWaiting.repaint()

        self.dailyWaiting = QLineEdit(self.widget1)
        self.dailyWaiting.setReadOnly(True)
        self.BookminVerticalLayout.addWidget(self.dailyWaiting)
        self.dailyWaiting.setText("데일리밥: " + str(self.daily.getWaitingPeople())
                                 + "명 대기 | 예상 대기시간 " + str(self.daily.getTime()) + "분")
        self.dailyWaiting.repaint()

        # widget2 =============================================================================
        # widget2 설정 (UI상 상단 오른쪽, 예약 버튼 모음)
        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setGeometry(400, 10, 590, 360)

        # widget2 내부 그리드 레이아웃 생성
        self.btnGridLayout = QGridLayout(self.widget2)
        self.btnGridLayout.setContentsMargins(0, 0, 0, 0)

        # 학교 시설 예약 버튼
        self.bookBtn = QPushButton(self.widget2)
        self.bookBtn.setSizePolicy(sizePolicy)
        self.btnGridLayout.addWidget(self.bookBtn, 1, 0, 1, 2)
        self.bookBtn.setText("학교 시설 예약하기")

        # 가마 버튼
        self.gamaBtn = QPushButton(self.widget2)
        self.gamaBtn.setSizePolicy(sizePolicy)
        self.btnGridLayout.addWidget(self.gamaBtn, 2, 0, 1, 1)
        self.gamaBtn.setText("가마 번호표 뽑기")

        # 누들송 버튼
        self.noodleBtn = QPushButton(self.widget2)
        self.noodleBtn.setSizePolicy(sizePolicy)
        self.btnGridLayout.addWidget(self.noodleBtn, 2, 1, 1, 1)
        self.noodleBtn.setText("누들송(면) 번호표 뽑기")

        # 인터쉐프 버튼
        self.interBtn = QPushButton(self.widget2)
        self.interBtn.setSizePolicy(sizePolicy)
        self.btnGridLayout.addWidget(self.interBtn, 3, 0, 1, 1)
        self.interBtn.setText("인터쉐프 번호표 뽑기")

        # 데일리밥 버튼
        self.dailyBtn = QPushButton(self.widget2)
        self.dailyBtn.setSizePolicy(sizePolicy)
        self.btnGridLayout.addWidget(self.dailyBtn, 3, 1, 1, 1)
        self.dailyBtn.setText("데일리밥 번호표 뽑기")

        #스타일 시트 설정
        self.centralwidget.setStyleSheet(
            "background-color: #282828;"
            "color: white;"
            "font-family: 맑은 고딕"
        )
        self.complexity.setStyleSheet(
            "background-color: #004F9F;"
            "border-radius: 5px"
        )
        self.gamaWaiting.setStyleSheet(
            "background-color: #004F9F;"
            "border-radius: 5px"
        )
        self.noodleWaiting.setStyleSheet(
            "background-color: #004F9F;"
            "border-radius: 5px"
        )
        self.interWaiting.setStyleSheet(
            "background-color: #004F9F;"
            "border-radius: 5px"
        )
        self.dailyWaiting.setStyleSheet(
            "background-color: #004F9F;"
            "border-radius: 5px"
        )
        self.bookBtn.setStyleSheet(
            "background-color: #004F9F;"
            "border-radius: 5px"
        )
        self.gamaBtn.setStyleSheet(
            "background-color: #004F9F;"
            "border-radius: 5px"
        )
        self.noodleBtn.setStyleSheet(
            "background-color: #004F9F;"
            "border-radius: 5px"
        )
        self.interBtn.setStyleSheet(
            "background-color: #004F9F;"
            "border-radius: 5px"
        )
        self.dailyBtn.setStyleSheet(
            "background-color: #004F9F;"
            "border-radius: 5px"
        )
        self.gamaMenu.setStyleSheet(
            "background-color: #FFCE44;"
            "border-radius: 5px;"
            "color: black"
        )
        self.noodleMenu.setStyleSheet(
            "background-color: #F3953F;"
            "border-radius: 5px;"
            "color: black"
        )
        self.interMenu.setStyleSheet(
            "background-color: #95C23D;"
            "border-radius: 5px;"
            "color: black"
        )
        self.dailyMenu.setStyleSheet(
            "background-color: #00A470;"
            "border-radius: 5px;"
            "color: black"
        )

        self.bookBtn.clicked.connect(self.bookBtn_clicked)
        self.gamaBtn.clicked.connect(self.gamaBtn_clicked)
        self.noodleBtn.clicked.connect(self.noodleBtn_clicked)
        self.interBtn.clicked.connect(self.interBtn_clicked)
        self.dailyBtn.clicked.connect(self.dailyBtn_clicked)

        MainWindow.setWindowTitle("Bookmin")
        MainWindow.setCentralWidget(self.centralwidget)

    def bookBtn_clicked(self):
        subwin = SubWindow()
        r = subwin.showModal()

        if r:
            text = subwin.edit.text()
            self.label.setText(text)

    # 가마 예약 버튼을 누르면 실행되는 새로운 창
    def gamaBtn_clicked(self):
        가마subwin = 가마SubWindow()
        r = 가마subwin.showModal()

        if r:
            text = 가마subwin.edit.text()
            self.label.setText(text)

    # 누들송 예약 버튼을 누르면 실행되는 새로운 창
    def noodleBtn_clicked(self):
        누들송subwin = 누들송SubWindow()
        r = 누들송subwin.showModal()

        if r:
            text = 누들송subwin.edit.text()
            self.label.setText(text)

    # 인터쉐프 예약 버튼을 누르면 실행되는 새로운 창
    def interBtn_clicked(self):
        인터쉐프subwin = 인터쉐프SubWindow()
        r = 인터쉐프subwin.showModal()

        if r:
            text = 인터쉐프subwin.edit.text()
            self.label.setText(text)

    # 데일리밥 예약 버튼을 누르면 실행되는 새로운 창
    def dailyBtn_clicked(self):
        데일리밥subwin = 데일리밥SubWindow()
        r = 데일리밥subwin.showModal()

        if r:
            text = 데일리밥subwin.edit.text()
            self.label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())