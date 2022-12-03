from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLayout, QGridLayout, QDialog, QLabel, QSizePolicy, QLineEdit, QToolButton


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 50)
        size.setWidth(max(size.width(), size.height()))
        return size


class 인터쉐프SubWindow(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        password = QLabel("전화번호를 입력해 주세요: ")

        # 번호 입력 창
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        numPadList = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '', '0', ''
        ]
        operatorList = [
            'C',
            'Enter',
        ]

        # Digit Buttons
        numLayout = QGridLayout()

        r = 0
        c = 0
        for btnText in numPadList:
            button = Button(btnText, self.buttonClicked)
            numLayout.addWidget(button, r, c)
            c += 1
            if c > 2:
                c = 0
                r += 1

        opLayout = QGridLayout()
        r = 0
        c = 0
        for btnText in operatorList:
            button = Button(btnText, self.buttonClicked)
            opLayout.addWidget(button, r, c)
            c += 1
            if c > 1:
                c = 0
                r += 1

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(password, 0, 0, 1, 2)
        mainLayout.addWidget(self.display, 1, 0, 1, 2)
        mainLayout.addLayout(numLayout, 2, 0)
        mainLayout.addLayout(opLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("인터쉐프 예약 창")

    #
    def buttonClicked(self):

        button = self.sender()
        key = button.text()

        if key == 'Enter':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + key)

    # 화면 보여지게..
    def showModal(self):
        return super().exec_()




