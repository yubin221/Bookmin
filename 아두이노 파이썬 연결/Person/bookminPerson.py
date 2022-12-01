import serial

class Person:

    def __init__(self):
        self.ser = serial.Serial("COM4", 1000000)
        self.var = ''
        self.congestionLevel = ''

    def getPerson(self):
        self.var = self.ser.readline().decode()

        if int(self.var) <= 10:
            self.congestionLevel = '여유'
        elif int(self.var) <= 20:
            self.congestionLevel = '보통'
        else:
            self.congestionLevel = '혼잡'

        print("식당내 인원수: " + self.var, end='')
        print("혼잡도: " + self.congestionLevel)

if __name__ == '__main__':
    p = Person()
    while True:
        p.getPerson()