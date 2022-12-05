from datetime import datetime

from qtconsole.qt import QtGui

from ON국민예약.onKookminBook import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QAbstractItemView, QHeaderView, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QLineEdit, QToolButton, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

class Button(QToolButton):
    def __init__(self, text, Event):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(Event)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class UnivBook(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.okb = OnKookminBook()
        self.setWindowTitle("ON국민 예약")

        mainLayout = QGridLayout()
        leftLayout = QGridLayout()
        rightVBox = QVBoxLayout()
        rightUpLayout = QGridLayout()
        rightDownLayout = QGridLayout()
        rightVBox.addLayout(rightUpLayout)
        rightVBox.addStretch(2)
        rightVBox.addLayout(rightDownLayout)
        mainLayout.addLayout(leftLayout,0,0)
        mainLayout.addLayout(rightVBox,0,1)

        tempDate = datetime.today()

        yearLabel = QLabel("년")
        self.yearEdit = QLineEdit(str(tempDate.year))
        self.yearEdit.setReadOnly(True)
        rightUpLayout.addWidget(yearLabel, 0,1,1,1)
        rightUpLayout.addWidget(self.yearEdit, 0,0,1,1)

        monthLabel = QLabel("월")
        self.monthEdit = QLineEdit(str(tempDate.month))
        self.monthEdit.setReadOnly(True)
        rightUpLayout.addWidget(monthLabel, 1,1,1,1)
        rightUpLayout.addWidget(self.monthEdit, 1,0,1,1)

        dayLabel = QLabel("일")
        self.dayEdit = QLineEdit()
        rightUpLayout.addWidget(dayLabel, 2,1,1,1)
        rightUpLayout.addWidget(self.dayEdit, 2,0,1,1)

        checkDateBtn = Button("일정\n확인", self.checkButtonClicked)
        rightUpLayout.addWidget(checkDateBtn,0,2,3,1)

        self.dateTable = QTableWidget()
        self.dateTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.dateTable.setRowCount(24)
        self.dateTable.setColumnCount(2)
        self.dateTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.dateTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.dateTable.setHorizontalHeaderLabels(["시간대" ,"예약자"])
        self.TableInit()
        leftLayout.addWidget(self.dateTable,0,0,1,1)

        idLabel = QLabel("ID:")
        self.idEdit = QLineEdit()
        rightDownLayout.addWidget(idLabel,0,0,1,1)
        rightDownLayout.addWidget(self.idEdit,1,0,1,2)

        pwLabel = QLabel("PW:")
        self.pwEdit = QLineEdit()
        self.pwEdit.setEchoMode(QLineEdit.Password)
        rightDownLayout.addWidget(pwLabel,2,0,1,1)
        rightDownLayout.addWidget(self.pwEdit,3,0,1,2)

        displayLabel = QLabel("시스템 메시지")
        displayEdit = QLineEdit()
        displayEdit.setReadOnly(True)
        rightDownLayout.addWidget(displayLabel,4,0,1,1)
        rightDownLayout.addWidget(displayEdit,5,0,1,2)

        purposeLabel = QLabel("이용목적")
        self.purposeEdit = QLineEdit()
        rightDownLayout.addWidget(purposeLabel,6,0,1,1)
        rightDownLayout.addWidget(self.purposeEdit,7,0,1,1)

        bookBtn = Button("예약하기", self.bookButtonClicked)
        rightDownLayout.addWidget(bookBtn,6,1,2,1)

        self.setLayout(mainLayout)

    def TableInit(self):
        for cnt, i in enumerate(self.okb.dateTable.keys()):
            self.dateTable.setItem(cnt, 0, QTableWidgetItem(i))
            self.dateTable.setItem(cnt, 1, QTableWidgetItem(self.okb.dateTable[i]))

    def checkButtonClicked(self):
        if self.dayEdit.text() != "":
            try:
                if 1 <= int(self.dayEdit.text()) <= 31:
                    self.okb.setDriver()
                    self.okb.loginOnkookmin(self.okb.driver, self.idEdit.text(), self.pwEdit.text())
                    self.okb.toPortal(self.okb.driver)
                    self.okb.getDateSchedule(self.okb.driver, int(self.yearEdit.text()), int(self.monthEdit.text()), int(self.dayEdit.text()))
                    self.okb.quitDriver()
                    self.TableInit()
            except:
                pass

    def bookButtonClicked(self):
        if self.purposeEdit.text() != "":
            indexList = []
            for i in self.dateTable.selectedItems():
                if i.column()==1:
                    if i.text() != "":
                        return None
                    indexList.append(int(i.row()))
            self.okb.setDriver()
            self.okb.loginOnkookmin(self.okb.driver, self.idEdit.text(), self.pwEdit.text())
            self.okb.toPortal(self.okb.driver)
            self.okb.bookTime(self.okb.driver, int(self.yearEdit.text()), int(self.monthEdit.text()),int(self.dayEdit.text()), indexList, self.purposeEdit.text())
            self.okb.quitDriver()


if __name__ == '__main__':
    #16일 9~12
    import sys
    app = QApplication(sys.argv)
    ub = UnivBook()
    ub.show()
    sys.exit(app.exec_())
