from twilioTest import TwilioSMS

class Manager:
    menu = dict()

    def loadMenu(self):
        pass  # 크롤링한 메뉴 불러오는코드 필요함

    def __init__(self, name):
        self.msgObj = TwilioSMS()
        self.name = name
        self.currentNum = 0  # 현재 번호표
        self.callNum = 0  # 불러야하는 번호표
        self.waitingTime = 0  # 예상 대기시간 (단위 : 분)
        self.menu = dict()

    def setWaitingTime(self, waitingTime):
        self.waitingTime = waitingTime

    # 번호표 뽑으면 번호 리턴
    def getNum(self):
        self.currentNum += 1
        return self.currentNum

    # 현재 대기자수 * 예상대기시간 = 예상 대기시간 리턴
    def getTime(self):
        temp = self.getWaitingPeople() * self.waitingTime
        return temp

    # 대기자 호출
    def call(self):
        if self.callNum < self.currentNum:
            self.callNum += 1
            message = str(self.callNum) + "번님 학식이 준비되었습니다."
            self.msgObj.sendSMS(message)
        else:
            print("대기자가 없습니다.")

    # 현재 대기자 수 리턴
    def getWaitingPeople(self):
        return self.currentNum - self.callNum

    def requestWaitingPeople(self):
        message = "현재 대기자수는 " + str(self.getWaitingPeople()) +"명입니다."
        self.msgObj.sendSMS(message)

if __name__ == "__main__":
    gome = Manager("고메")
    gome.getNum()
    gome.getNum()
    gome.getNum()
    print(gome.callNum, gome.currentNum)
    gome.call()
    gome.call()
    gome.call()
    gome.call()
    print(gome.callNum, gome.currentNum)