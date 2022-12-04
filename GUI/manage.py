from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

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
        self.gamaText.setObjectName("gama")
        self.gridLayout.addWidget(self.gamaText, 1, 0, 1, 1)

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
        self.dailyText.setObjectName("daily")
        self.gridLayout.addWidget(self.dailyText, 1, 3, 1, 1)

        self.dailyBtn = QPushButton()
        self.dailyBtn.setObjectName("dailyBtn")
        self.gridLayout.addWidget(self.dailyBtn, 2, 3, 1, 1)
        self.dailyBtn.setText("데일리밥 호출")

        self.gamaBtn.clicked.connect(self.buttonClicked)
        self.noodleBtn.clicked.connect(self.buttonClicked)
        self.interBtn.clicked.connect(self.buttonClicked)
        self.dailyBtn.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        print(key)
        """
        if key == '=':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + key)
        """


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    manage = Manage()
    manage.show()
    sys.exit(app.exec_())

