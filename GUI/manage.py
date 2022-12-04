import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from foodManager import *

class Updator(QThread):
    finished = pyqtSignal()
    def run(self):
        while True:
            self.finished.emit()
            time.sleep(5)

class Manage(QWidget):

    def __init__(self):
        super().__init__()

        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)
        self.resize(1200, 300)
        self.setWindowTitle("식당용 GUI")

        # 가마
        self.gamaTitle = QLabel()
        self.gamaTitle.setObjectName("gamaTitle")
        self.gridLayout.addWidget(self.gamaTitle, 0, 0, 1, 1)
        self.gamaTitle.setText("가마")

        self.gamaText = QTextEdit()
        self.gamaText.setReadOnly(True)
        self.gamaText.setObjectName("gama")
        self.gridLayout.addWidget(self.gamaText, 1, 0, 1, 1)
        self.gamaText.setText('Test')

        self.gamaBtn = QPushButton()
        self.gamaBtn.setObjectName("gamaBtn")
        self.gridLayout.addWidget(self.gamaBtn, 2, 0, 1, 1)
        self.gamaBtn.setText("가마 호출")

        # 누들송
        self.noodleTitle = QLabel()
        self.noodleTitle.setObjectName("noodleTitle")
        self.gridLayout.addWidget(self.noodleTitle, 0, 1, 1, 1)
        self.noodleTitle.setText("누들송(면)")

        self.noodleText = QTextEdit()
        self.noodleText.setReadOnly(True)
        self.noodleText.setObjectName("noodle")
        self.gridLayout.addWidget(self.noodleText, 1, 1, 1, 1)

        self.noodleBtn = QPushButton()
        self.noodleBtn.setObjectName("noodleBtn")
        self.gridLayout.addWidget(self.noodleBtn, 2, 1, 1, 1)
        self.noodleBtn.setText("누들송 호출")

        # 인터쉐프
        self.interTitle = QLabel()
        self.interTitle.setObjectName("interTitle")
        self.gridLayout.addWidget(self.interTitle, 0, 2, 1, 1)
        self.interTitle.setText("인터쉐프")

        self.interText = QTextEdit()
        self.interText.setReadOnly(True)
        self.interText.setObjectName("inter")
        self.gridLayout.addWidget(self.interText, 1, 2, 1, 1)

        self.interBtn = QPushButton()
        self.interBtn.setObjectName("interBtn")
        self.gridLayout.addWidget(self.interBtn, 2, 2, 1, 1)
        self.interBtn.setText("인터쉐프 호출")

        # 데일리밥
        self.dailyTitle = QLabel()
        self.dailyTitle.setObjectName("dailyTitle")
        self.gridLayout.addWidget(self.dailyTitle, 0, 3, 1, 1)
        self.dailyTitle.setText("데일리밥")

        self.dailyText = QTextEdit()
        self.dailyText.setReadOnly(True)
        self.dailyText.setObjectName("daily")
        self.gridLayout.addWidget(self.dailyText, 1, 3, 1, 1)

        self.dailyBtn = QPushButton()
        self.dailyBtn.setObjectName("dailyBtn")
        self.gridLayout.addWidget(self.dailyBtn, 2, 3, 1, 1)
        self.dailyBtn.setText("데일리밥 호출")

        # 연결
        self.gamaBtn.clicked.connect(self.buttonClicked)
        self.noodleBtn.clicked.connect(self.buttonClicked)
        self.interBtn.clicked.connect(self.buttonClicked)
        self.dailyBtn.clicked.connect(self.buttonClicked)

        self.updator = Updator()
        self.updator.finished.connect(self.updateText)
        self.updator.start()

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        print(key)

        if key == '가마 호출':
            gama.call()
        elif key == '누들송 호출':
            noodle.call()
        elif key == '인터쉐프 호출':
            inter.call()
        elif key == '데일리밥 호출':
            daily.call()

    def updateText(self):
        self.gamaText.setText('마지막 번호표: ' + str(gama.callNumber()))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    manage = Manage()
    manage.show()
    sys.exit(app.exec_())

