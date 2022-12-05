from 번호표시스템.twilioTest import TwilioSMS

class Manager:
    def __init__(self, name):
        self.msgObj = TwilioSMS()
        self.name = name
        self.currentNum = 0  # 현재 번호표
        self.callNum = 0  # 마지막으로 부른 번호표
        self.waitingTime = 0  # 예상 대기시간 (단위 : 분)

    # 1명당 대기 시간 설정
    def setWaitingTime(self, waitingTime):
        self.waitingTime = waitingTime

    def getWaitingTime(self):
        return self.waitingTime

    # 현재 대기자수 * 예상대기시간 = 예상 대기시간 리턴
    def getTime(self):
        temp = self.getWaitingPeople() * self.waitingTime
        return temp

    # 마지막으로 부른 번호표 리턴
    def callNumber(self):
        return self.callNum

    # 불러야 할 번호표 리턴
    def mustCallNumber(self):
        if self.callNum == self.currentNum:
            return '없음'
        return self.callNum + 1

    # 현재 번호표 리턴
    def currentNumber(self):
        return self.currentNum

    # 현재 대기자 수 리턴
    def getWaitingPeople(self):
        return self.currentNum - self.callNum

    # 번호표 뽑으면 번호 리턴
    def getNum(self):
        self.currentNum += 1
        return self.currentNum

    # 대기자 호출
    def call(self):
        if self.callNum < self.currentNum:
            self.callNum += 1
            message = str(self.callNum) + "번님 " + str(self.name) + " 학식이 준비되었습니다."
            print(message)
            self.msgObj.sendSMS(message)
        else:
            print("대기자가 없습니다.")

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