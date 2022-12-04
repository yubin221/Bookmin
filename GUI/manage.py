import time

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from foodManager import *

class Updator(QThread):
    finished = pyqtSignal()
    def run(self):
        while True:
            self.finished.emit()
            time.sleep(1)

class Manage(QWidget):

    def __init__(self):
        super().__init__()

        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)
        self.resize(1200, 600)
        self.setWindowTitle("식당용 GUI")
        self.onlyInt = QIntValidator()

        # 가마
        self.gamaTitle = QLabel()
        self.gridLayout.addWidget(self.gamaTitle, 0, 0, 1, 1)
        self.gamaTitle.setText("가마")

        self.gamaText = QTextEdit()
        self.gamaText.setReadOnly(True)
        self.gridLayout.addWidget(self.gamaText, 1, 0, 1, 1)

        self.gamaBtn = QPushButton()
        self.gridLayout.addWidget(self.gamaBtn, 2, 0, 1, 1)
        self.gamaBtn.setText("가마 호출")

        self.gamaTitle2 = QLabel()
        self.gridLayout.addWidget(self.gamaTitle2, 3, 0, 1, 1)
        self.gamaTitle2.setText("1명당 대기시간 설정")

        self.gamaWaiting = QLineEdit()
        self.gamaWaiting.setMaxLength(1)
        self.gamaWaiting.setValidator(self.onlyInt)
        self.gridLayout.addWidget(self.gamaWaiting, 4, 0, 1, 1)

        self.gamaWaitingBtn = QPushButton()
        self.gridLayout.addWidget(self.gamaWaitingBtn, 5, 0, 1, 1)
        self.gamaWaitingBtn.setText("가마 1명당 대기시간 설정")

        # 누들송
        self.noodleTitle = QLabel()
        self.gridLayout.addWidget(self.noodleTitle, 0, 1, 1, 1)
        self.noodleTitle.setText("누들송(면)")

        self.noodleText = QTextEdit()
        self.noodleText.setReadOnly(True)
        self.gridLayout.addWidget(self.noodleText, 1, 1, 1, 1)

        self.noodleBtn = QPushButton()
        self.gridLayout.addWidget(self.noodleBtn, 2, 1, 1, 1)
        self.noodleBtn.setText("누들송 호출")

        self.noodleTitle2 = QLabel()
        self.gridLayout.addWidget(self.noodleTitle2, 3, 1, 1, 1)
        self.noodleTitle2.setText("1명당 대기시간 설정")

        self.noodleWaiting = QLineEdit()
        self.noodleWaiting.setMaxLength(1)
        self.noodleWaiting.setValidator(self.onlyInt)
        self.gridLayout.addWidget(self.noodleWaiting, 4, 1, 1, 1)

        self.noodleWaitingBtn = QPushButton()
        self.gridLayout.addWidget(self.noodleWaitingBtn, 5, 1, 1, 1)
        self.noodleWaitingBtn.setText("누들송 1명당 대기시간 설정")

        # 인터쉐프
        self.interTitle = QLabel()
        self.gridLayout.addWidget(self.interTitle, 0, 2, 1, 1)
        self.interTitle.setText("인터쉐프")

        self.interText = QTextEdit()
        self.interText.setReadOnly(True)
        self.gridLayout.addWidget(self.interText, 1, 2, 1, 1)

        self.interBtn = QPushButton()
        self.gridLayout.addWidget(self.interBtn, 2, 2, 1, 1)
        self.interBtn.setText("인터쉐프 호출")

        self.interTitle2 = QLabel()
        self.gridLayout.addWidget(self.interTitle2, 3, 2, 1, 1)
        self.interTitle2.setText("1명당 대기시간 설정")

        self.interWaiting = QLineEdit()
        self.interWaiting.setMaxLength(1)
        self.interWaiting.setValidator(self.onlyInt)
        self.gridLayout.addWidget(self.interWaiting, 4, 2, 1, 1)

        self.interWaitingBtn = QPushButton()
        self.gridLayout.addWidget(self.interWaitingBtn, 5, 2, 1, 1)
        self.interWaitingBtn.setText("인터쉐프 1명당 대기시간 설정")

        # 데일리밥
        self.dailyTitle = QLabel()
        self.gridLayout.addWidget(self.dailyTitle, 0, 3, 1, 1)
        self.dailyTitle.setText("데일리밥")

        self.dailyText = QTextEdit()
        self.dailyText.setReadOnly(True)
        self.gridLayout.addWidget(self.dailyText, 1, 3, 1, 1)

        self.dailyBtn = QPushButton()
        self.gridLayout.addWidget(self.dailyBtn, 2, 3, 1, 1)
        self.dailyBtn.setText("데일리밥 호출")

        self.dailyTitle2 = QLabel()
        self.gridLayout.addWidget(self.dailyTitle2, 3, 3, 1, 1)
        self.dailyTitle2.setText("1명당 대기시간 설정")

        self.dailyWaiting = QLineEdit()
        self.dailyWaiting.setMaxLength(1)
        self.dailyWaiting.setValidator(self.onlyInt)
        self.gridLayout.addWidget(self.dailyWaiting, 4, 3, 1, 1)

        self.dailyWaitingBtn = QPushButton()
        self.gridLayout.addWidget(self.dailyWaitingBtn, 5, 3, 1, 1)
        self.dailyWaitingBtn.setText("데일리밥 1명당 대기시간 설정")

        # 연결
        self.gamaBtn.clicked.connect(self.buttonClicked)
        self.noodleBtn.clicked.connect(self.buttonClicked)
        self.interBtn.clicked.connect(self.buttonClicked)
        self.dailyBtn.clicked.connect(self.buttonClicked)
        self.gamaWaitingBtn.clicked.connect(self.buttonClicked)
        self.noodleWaitingBtn.clicked.connect(self.buttonClicked)
        self.interWaitingBtn.clicked.connect(self.buttonClicked)
        self.dailyWaitingBtn.clicked.connect(self.buttonClicked)

        self.updator = Updator()
        self.updator.finished.connect(self.updateText)
        self.updator.start()

        self.foodList = ['gama', 'noodle', 'inter', 'daily']

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

        if key == '가마 호출':
            gama.call()
        elif key == '누들송 호출':
            noodle.call()
        elif key == '인터쉐프 호출':
            inter.call()
        elif key == '데일리밥 호출':
            daily.call()
        elif key == "가마 1명당 대기시간 설정":
            if self.gamaWaiting.text() != '':
                gama.setWaitingTime(int(self.gamaWaiting.text()))
                self.gamaWaiting.setText('')
        elif key == "누들송 1명당 대기시간 설정":
            if self.noodleWaiting.text() != '':
                noodle.setWaitingTime(int(self.noodleWaiting.text()))
                self.noodleWaiting.setText('')
        elif key == "인터쉐프 1명당 대기시간 설정":
            if self.interWaiting.text() != '':
                inter.setWaitingTime(int(self.interWaiting.text()))
                self.interWaiting.setText('')
        elif key == "데일리밥 1명당 대기시간 설정":
            if self.dailyWaiting.text() != '':
                daily.setWaitingTime(int(self.dailyWaiting.text()))
                self.dailyWaiting.setText('')

    def updateText(self):
        for i in self.foodList:
            command = eval('self.' + i + 'Text')
            command.setText('누적 번호: ' + str(eval(i).currentNumber()))
            command.append('현재 대기자 수: ' + str(eval(i).getWaitingPeople()) + '\n')
            command.append('마지막으로 호출한 번호: ' + str(eval(i).callNumber()))
            command.append('호출할 번호: ' + str(eval(i).mustCallNumber()) + '\n')
            command.append('현재 1명당 대기시간: ' + str(eval(i).getWaitingTime()) + '분')
            command.append('현재 대기시간: ' + str(eval(i).getTime()) + '분')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    manage = Manage()
    manage.show()
    sys.exit(app.exec_())

