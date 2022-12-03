from PyQt5 import QtCore, QtGui, QtWidgets
from SubWindow import SubWindow
from 가마SubWindow import 가마SubWindow
from 누들송SubWindow import 누들송SubWindow
from 인터쉐프SubWindow import 인터쉐프SubWindow
from 데일리밥SubWindow import 데일리밥SubWindow
from crawlingclass import Crawling

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 380, 981, 211))

        self.menuHorizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.menuHorizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.menuVerticalLayout = QtWidgets.QVBoxLayout()
        self.gamaTitle = QtWidgets.QLabel(self.widget)
        self.menuVerticalLayout.addWidget(self.gamaTitle)
        self.gamaMenu = QtWidgets.QTextEdit(self.widget)
        self.gamaMenu.setReadOnly(True)
        self.menuVerticalLayout.addWidget(self.gamaMenu)
        self.menuHorizontalLayout.addLayout(self.menuVerticalLayout)

        self.menuVerticalLayout_2 = QtWidgets.QVBoxLayout()
        self.noodleTitle = QtWidgets.QLabel(self.widget)
        self.menuVerticalLayout_2.addWidget(self.noodleTitle)
        self.noodleMenu = QtWidgets.QTextEdit(self.widget)
        self.noodleMenu.setReadOnly(True)
        self.noodleMenu.setObjectName("noodleMenu")
        self.menuVerticalLayout_2.addWidget(self.noodleMenu)
        self.menuHorizontalLayout.addLayout(self.menuVerticalLayout_2)

        self.menuVerticalLayout_3 = QtWidgets.QVBoxLayout()
        self.interTitle = QtWidgets.QLabel(self.widget)
        self.menuVerticalLayout_3.addWidget(self.interTitle)
        self.interMenu = QtWidgets.QTextEdit(self.widget)
        self.interMenu.setReadOnly(True)
        self.menuVerticalLayout_3.addWidget(self.interMenu)
        self.menuHorizontalLayout.addLayout(self.menuVerticalLayout_3)

        self.menuVerticalLayout_4 = QtWidgets.QVBoxLayout()
        self.dailyTitle = QtWidgets.QLabel(self.widget)
        self.menuVerticalLayout_4.addWidget(self.dailyTitle)
        self.dailyMenu = QtWidgets.QTextEdit(self.widget)
        self.dailyMenu.setReadOnly(True)
        self.menuVerticalLayout_4.addWidget(self.dailyMenu)
        self.menuHorizontalLayout.addLayout(self.menuVerticalLayout_4)

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 381, 361))

        self.BookminVerticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.BookminVerticalLayout.setContentsMargins(0, 0, 0, 0)

        self.title = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.title.setFont(font)
        self.title.setLineWidth(1)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.BookminVerticalLayout.addWidget(self.title)

        self.complexityTitle = QtWidgets.QLabel(self.widget1)
        self.BookminVerticalLayout.addWidget(self.complexityTitle)

        self.complexity = QtWidgets.QTextEdit(self.widget1)
        self.complexity.setLineWidth(1)
        self.complexity.setReadOnly(True)
        self.BookminVerticalLayout.addWidget(self.complexity)

        self.watingTitle = QtWidgets.QLabel(self.widget1)
        self.BookminVerticalLayout.addWidget(self.watingTitle)

        self.gamaWaiting = QtWidgets.QLineEdit(self.widget1)
        self.gamaWaiting.setReadOnly(True)
        self.BookminVerticalLayout.addWidget(self.gamaWaiting)

        self.noodleWaiting = QtWidgets.QLineEdit(self.widget1)
        self.noodleWaiting.setReadOnly(True)
        self.BookminVerticalLayout.addWidget(self.noodleWaiting)

        self.interWaiting = QtWidgets.QLineEdit(self.widget1)
        self.interWaiting.setReadOnly(True)
        self.BookminVerticalLayout.addWidget(self.interWaiting)

        self.dailyWaiting = QtWidgets.QLineEdit(self.widget1)
        self.dailyWaiting.setReadOnly(True)
        self.BookminVerticalLayout.addWidget(self.dailyWaiting)

        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(400, 10, 591, 361))

        self.btnGridLayout = QtWidgets.QGridLayout(self.widget2)
        self.btnGridLayout.setContentsMargins(0, 0, 0, 0)

        self.gamaBtn = QtWidgets.QPushButton(self.widget2)
        self.gamaBtn.setSizePolicy(sizePolicy)
        self.btnGridLayout.addWidget(self.gamaBtn, 2, 0, 1, 1)

        self.interBtn = QtWidgets.QPushButton(self.widget2)
        self.interBtn.setSizePolicy(sizePolicy)
        self.btnGridLayout.addWidget(self.interBtn, 3, 0, 1, 1)

        self.dailyBtn = QtWidgets.QPushButton(self.widget2)
        self.dailyBtn.setSizePolicy(sizePolicy)
        self.btnGridLayout.addWidget(self.dailyBtn, 3, 1, 1, 1)

        self.noodleBtn = QtWidgets.QPushButton(self.widget2)
        self.noodleBtn.setSizePolicy(sizePolicy)
        self.btnGridLayout.addWidget(self.noodleBtn, 2, 1, 1, 1)

        self.bookBtn = QtWidgets.QPushButton(self.widget2)
        self.bookBtn.setSizePolicy(sizePolicy)
        self.btnGridLayout.addWidget(self.bookBtn, 1, 0, 1, 2)

        self.gamaTitle.setText("가마")
        self.noodleTitle.setText("누들송(면)")
        self.interTitle.setText("인터쉐프")
        self.dailyTitle.setText("데일리밥")
        self.title.setText("Bookmin")
        self.complexityTitle.setText("식당별 혼잡도")
        self.watingTitle.setText("식당별 대기 인원")
        self.gamaBtn.setText("가마")
        self.interBtn.setText("인터쉐프")
        self.dailyBtn.setText("데일리밥")
        self.noodleBtn.setText("누들송(면)")
        self.bookBtn.setText("학교 시설 예약")
        #self.gamaMenu.setText("Test")
        self.gamaMenu.setText(Crawling().todayMenu("가마중식"))
        self.noodleMenu.setText(Crawling().todayMenu("누들송(면)중식"))
        self.interMenu.setText(Crawling().todayMenu("인터쉐프중식"))
        self.dailyMenu.setText(Crawling().todayMenu("데일리밥중식"))

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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

