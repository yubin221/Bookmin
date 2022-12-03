import serial
from multiprocessing import Process

class Person:

    def __init__(self):
        self.ser = serial.Serial("COM3", 1000000)
        self.complexityLevel = '데이터 갱신중'

    def getPerson(self):
        while True:
            self.var = self.ser.readline().decode()

            if int(self.var) <= 10:
                self.congestionLevel = '여유'
            elif int(self.var) <= 20:
                self.congestionLevel = '보통'
            else:
                self.congestionLevel = '혼잡'

            self.complexityLevel = "식당내 인원수: " + self.var + "혼잡도: " + self.congestionLevel
            #print(self.complexityLevel)

    def printPerson(self):
        print(self.complexityLevel)
        return self.complexityLevel

if __name__ == '__main__':
    p = Person()

    p1 = Process(target=p.getPerson())
    p1.start
    p1.join

    p2 = Process(target=p.printPerson())
    p2.start()
    p2.join